import os
import csv

election_path = os.path.join('PyPoll','Resources','election_data.csv')

# Initialize variables to store the total votes and votes for each candidate
total_votes = 0
candidate_votes = {}

# Open the CSV file containing election data
with open(election_path) as csvfile:
    # Create a CSV reader object
    election_data = csv.reader(csvfile, delimiter=",")
    # Read and skip the header row
    header = next(election_data)

    # Loop through each row of the CSV file
    for row in election_data:
        # Increment the total vote count for each row
        total_votes += 1
        # Extract the candidate name from the row
        candidate_name = row[2]
        
        # If the candidate is already in the dictionary, increment their vote count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        # If the candidate is not in the dictionary, add them with an initial vote count of 1
        else:
            candidate_votes[candidate_name] = 1

# Print the total number of votes cast
print("---------------------------------------------------------")
print("Election Results")
print("---------------------------------------------------------")

print("Total Votes:", total_votes) #prints total vote count
print("---------------------------------------------------------")

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100 #calculates percentage of votes won by each candidate
    print(f"{candidate}: {percentage:.3f}% ({votes} votes)") #prints candidate name, percent of votes won, and number of votes won
print("---------------------------------------------------------")
# Find the winner of the election based on the popular vote
winner = max(candidate_votes, key=candidate_votes.get) #finds out the winner using the max number of votes
print("Winner:", winner)
print("---------------------------------------------------------")

# Write results to a text file
output_file = os.path.join('PyPoll','analysis','election_restuls.txt')
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("----------------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes} votes)\n")
    file.write("----------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------------------\n")
