#!/bin/bash

echo "----------------- Setting up environment -----------------"

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

echo "----------------- Program ready to run -----------------"
python Query_Script.py
