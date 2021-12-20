# Github bigQuery Analysis

a python script for getting data from bigquery and display to user in a readable way. 

the data set used can be found here: https://cloud.google.com/blog/topics/public-datasets/github-on-bigquery-analyze-all-the-open-source-code

the anaysis tried to answer the following questions:
- what langauges have the most code in Github by byte? -> this question is relevant as it shows the user what is the "most used language" and for a student could inform where they should focus their effort as learning this progamming language could lead to a more useful skill set than learning a langauge that isn't used any more. one constraint of doing this anaysis is that not every business uses Github to store their code so the most popular langauge in Github might not be the most popular language in the industry.
- who are the top Github Commiters? -> this question is relevant as it shows people what the most "productive" people are doing so a person can judge their productivity off of data rather than the always looming idea that "I am not doing enough". one constraint of doing this anaysis with the data set used is that the dataset is a sample rather than the whole population (due to size/processing power constants) so while the data is better than "I am not doing enough" it might not be the real top Commiters.

# Installation

in order to get the scripts run: git clone https://github.com/RileyJRaso/Github_bigquery__analysis.git

important: all other libraries are installed with start up script, make sure you run the script in order to run the python code

git clone 

# Steps to run script

in order to run user needs a file called: Pathtojson.txt which contains the path to the big query service account key

Example of Pathtojson.txt:
User/Downloads/File.txt

once this file is made run the script by running the attached bash script:

./StartUpScript.sh (in the folder with the script)
