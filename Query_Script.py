from google.cloud import bigquery
import matplotlib.pyplot as plt

def query_table(querystring):
    BQclient = bigquery.Client()

    query_job = BQclient.query(querystring)

    results = query_job.result()

    return results

def Create_Results_Array(results, X_data, Y_data):
    x_axis = []
    y_axis = []

    for row in results:
        x_axis.append(row[X_data])
        y_axis.append(row[Y_data])

    Results_In_Array = [x_axis, y_axis]

    return Results_In_Array

def Display_Data(names, values):

    plt.bar(names, values)
    plt.xlabel('Languages')
    plt.ylabel('Number of Repos')
    plt.title("Top Languages used in Github")
    #plt.legend() might use if useful
    plt.show()

def Show_Total_Repo_By_Language():

    print("How many languages would you like to see (limit 15 languages)")
    Limit = int(input())

    # input validation for user input (input is also cast as an int so that SQL injection attacks will not work)
    while Limit > 15 or Limit < 0:
        print("Improper input please provide a number between 15 and 0")
        Limit = int(input())

    querystring = """
                  SELECT L.name, COUNT(*) AS `Total_Number_of_Repos`
                  FROM `bigquery-public-data.github_repos.languages`,
                  UNNEST(language) as L GROUP BY L.name
                  ORDER BY Total_Number_of_Repos DESC
                  LIMIT """ + str(Limit)

    results = query_table(querystring)

    Fixed_Results = Create_Results_Array(results, "name", "Total_Number_of_Repos")

    Display_Data(Fixed_Results[0], Fixed_Results[1])

def option_Select():

    print("\nWhat would you like to know? Select from the following options:\n\n")
    print("Enter \"languages\" for: A graph of top Github languages calculated by amount of Repos where language X is the main language of that Repo\n\n")

    option = str(input())

    if(option == "languages"):
        Show_Total_Repo_By_Language()
    else:
        print("I'm sorry that option isn't implemented yet please enter another option")
        option_Select()

if __name__ == "__main__":

    option_Select()
