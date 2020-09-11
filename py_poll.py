import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total vote counter
total_votes = 0

# candidate options
candidate_options = []
# declare a candidate votes dictionary
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the file here
    file_reader = csv.reader(election_data)
    # read the header row
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1 
        #print the candidate names from each row
        candidate_name = row[2]
        #if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add to the candidate name to list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidates count
        candidate_votes[candidate_name] +=1

# determine the percentage of votes for each candidate by looping through
#iterate through the candidate list
for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    vote_percentage = votes / total_votes *100
    
    #determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage): 
            # if true then set winning_coun = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    # print out the winning candidate, vote count and percentage to terminal

    #print the candidate name and the percentage of the vote
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")

print(winning_candidate_summary)   
   














