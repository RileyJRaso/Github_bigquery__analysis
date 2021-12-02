from google.cloud import bigquery
import matplotlib.pyplot as plt

def query_table(querystring):
    BQclient = bigquery.Client()

    query_job = BQclient.query(querystring)

    results = query_job.result()

    return results

def Create_Array(results):
    Names = []
    Values = []

    for row in results:
        Names.append(row.name)
        Values.append(row.Total_Number_of_Repos)

    Results_In_Array = [Names, Values]

    return Results_In_Array

def Display_Data(names, values):
    plt.bar(names, values)
    plt.show()

if __name__ == "__main__":

    print("How many lanugages would you like to see (limit 15 Laugages)")
    Limit = int(input())

    querystring = """
                  SELECT L.name, COUNT(*) AS `Total_Number_of_Repos`
                  FROM `bigquery-public-data.github_repos.languages`,
                  UNNEST(language) as L GROUP BY L.name
                  ORDER BY Total_Number_of_Repos DESC
                  LIMIT """ + str(Limit)

    results = query_table(querystring)

    Fixed_Results = Create_Array(results)

    Display_Data(Fixed_Results[0], Fixed_Results[1])
