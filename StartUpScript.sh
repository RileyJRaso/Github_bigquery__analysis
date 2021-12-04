#!/bin/bash

printf "\n\n----------------- Setting up environment -----------------\n\n"

#setting up global variables
input="Pathtojson.txt"
while IFS= read -r line
do
  export GOOGLE_APPLICATION_CREDENTIALS="$line"
  echo "$line was added as the path to your GOOGLE_APPLICATION_CREDENTIALS"
done < "$input"

#installing libraries
pip install --upgrade google-cloud-bigquery
pip install matplotlib

printf "\n\n----------------- Program ready to run -----------------\n\n"
python Query_Script.py
