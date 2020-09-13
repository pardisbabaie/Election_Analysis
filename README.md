# Election_Analysis
## Overview of Election Audit
Tom is a Colorado board of elections member that is doing an audit of the tabulated results for an election in Colorado. In this project, we are assisting Tom by conducting an analysis to report on the total number of votes, the number of votes for each candidate, the percentage of votes for each candidate, the winning candidate, the number of votes for each county, the percentage of votes in each county and the largest county turn out. 
## Election Results
The following is a breakdown of the results that were discovered in the analysis:
- The total number of votes captured in the election was 369,711. This is calculated using the total_votes counter.
- Through this analysis, I have captured the breakdown of the votes in each county and the percentage of the total votes captured in each county as per below:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- I used the following if decision statement to find out which county had the largest number of votes which is Denver
  ```
  if (votes > top_count):
            top_count = votes
            top_county = county_name
  ```
- Through this analysis, I also captured the breakdown of the votes and the percentage of the total votes captured for each candidate as per below:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- Finally, using another if decision statement, I discovered who the winning candidate is, what their total number of votes are and what percentage of the total votes they have:
   ```
   if (votes1 > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes1
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
   ```
   - Winner: Diana DeGette
   - Winning Vote Count: 272,892
   - Winning Percentage: 73.8%
## Election-Audit Summary
This script has determined who the winner is and the captured the number of votes for each candidate efficiently. This script will continue to work with more candidates and on a bigger scale which is much more reliable than completing the election count manually. There are also a few modifications and additions that can be made to the following script to be able to analyze voting habits and how to improve the voting process. An example of this would be to capture the 3 voting methods for each vote casted to determine what voting method has been used the most which can help us determine what method people find easiest to use. This can be done through creating a variable and dictionary of the voting methods and writing additional script to determine the number of times each method of voting was used and the percentage of that method overall to determine which method was used the most. Another example of improving the script would be to also capture the party the candidate belongs to so that we can use the same method as we used for determining the winning candidate to also determine the winning party in the election and the total # of percentage breakdown for the votes for each party.
