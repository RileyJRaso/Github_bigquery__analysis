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

def Display_Data_bar(names, values, x_label, y_label, Title):

    plt.bar(names, values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(Title)
    #plt.legend() might use if useful
    plt.show()

def Display_Data_line(names, values, x_label, y_label, Title):

    plt.scatter(names, values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(Title)
    #plt.legend() might use if useful
    plt.show()


def Show_Tread_Of_Langauge():

    querystring = """
                  SELECT EXTRACT(DATE FROM author.date) AS commitdate, languages.ProgrammingLanguage as language, Count(*) AS Commits
                  FROM `bigquery-public-data.github_repos.sample_commits` as commits
                  INNER JOIN(
                    SELECT repo_name, L.name as ProgrammingLanguage
                    FROM `bigquery-public-data.github_repos.languages`,
                    UNNEST(language) as L
                    ) as languages
                  ON commits.repo_name = languages.repo_name
                  WHERE EXTRACT(DATE FROM author.date) between DATE_SUB('2015-04-10', INTERVAL 10 DAY) and '2015-04-10'
                  AND languages.ProgrammingLanguage = 'Python'
                  GROUP BY EXTRACT(DATE FROM author.date), languages.ProgrammingLanguage
                  LIMIT 100
                  """
    results = query_table(querystring)

    Fixed_Results = Create_Results_Array(results, "commitdate", "Commits")

    Display_Data_line(Fixed_Results[0], Fixed_Results[1], 'Dates', 'Number of Commits', "How many Commits of Language between 2015-03-30 and 2015-04-10")

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

    Display_Data_bar(Fixed_Results[0], Fixed_Results[1], 'Languages', 'Number of Repos', "Top Languages used in Github")

def Show_Most_Commits_By_Person():

    print("How many people you would like to see (limit 15 people)")
    Limit = int(input())

    # input validation for user input (input is also cast as an int so that SQL injection attacks will not work)
    while Limit > 15 or Limit < 0:
        print("Improper input please provide a number between 15 and 0")
        Limit = int(input())

    querystring = """
                  SELECT author.name , COUNT(*) AS `Total_Number_of_Commits`
                  FROM `bigquery-public-data.github_repos.sample_commits`
                  GROUP BY author.name ORDER BY Total_Number_of_Commits DESC
                  LIMIT """ + str(Limit)

    results = query_table(querystring)

    Fixed_Results = Create_Results_Array(results, "name", "Total_Number_of_Commits")

    Display_Data_bar(Fixed_Results[0], Fixed_Results[1], 'Name of Person', 'Number of Commits', "Top Committers of Github (from sample data)")

def option_Select():

    print("\nWhat would you like to know? Select from the following options:\n\n")
    print("Enter \"Languages\" for: A graph of top Github languages calculated by amount of Repos where language X is the main language of that Repo\n")
    print("Enter \"Commiters\" for: A graph of top Github Commiters calculated by amount of Commits from a sample of total commits to Github, IMPORTANT this is done on a sample not all commits so results might not reflect the real top Committers of Github \n")
    print("Enter \"Exit\" to end program\n")

    option = str(input())

    if(option == "Languages"):
        Show_Total_Repo_By_Language()
    if(option == "Commiters"):
        Show_Most_Commits_By_Person()
    if(option == "Exit"):
        pass
    else:
        print("I'm sorry that option isn't implemented yet please enter another option")
        option_Select()

if __name__ == "__main__":

    option_Select()
    #Show_Tread_Of_Langauge()
