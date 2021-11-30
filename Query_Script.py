from google.cloud import bigquery


def query_table(querystring):
    BQclient = bigquery.Client()

    query_job = BQclient.query(querystring)

    results = query_job.result()

    return results

if __name__ == "__main__":
    querystring = """
                  SELECT L.name, COUNT(*) AS `Total_Number_of_Repos`
                  FROM `bigquery-public-data.github_repos.languages`,
                  UNNEST(language) as L GROUP BY L.name
                  ORDER BY Total_Number_of_Repos DESC
                  LIMIT 1000
                  """
    results = query_table(querystring)

    for row in results:
        print("{} Has {} repos on Github".format(row.name, row.Total_Number_of_Repos))
