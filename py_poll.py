import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the file here
    file_reader = csv.reader(election_data)
    # print the header row in the CSV file
    headers = next(file_reader)
    print(headers)
       








