#!/bin/bash

input="Pathtojson.txt"
while IFS= read -r line
do
  export GOOGLE_APPLICATION_CREDENTIALS="$line"
  echo "$line was added as the path to your GOOGLE_APPLICATION_CREDENTIALS"
done < "$input"

python Query_Script.py 
