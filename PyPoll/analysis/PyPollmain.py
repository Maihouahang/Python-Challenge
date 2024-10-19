#You will be given a set of poll data called election_data.csv. 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
    #The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("..", "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
dictionary = {}  # This is the dictonary for candidate names and their vote counts

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # increase the total vote count by one to keep track of total_votes
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in dictionary:
            # Initializes their vote count to 0 in order to increment the vote counts
            dictionary[candidate_name] = 0  

        # Add a vote to the candidate's count
        dictionary[candidate_name] = dictionary[candidate_name] + 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the total vote count (to terminal)
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # Write the total vote count to the text file
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")

    # Before looping, initialize variables to track the winning candidate and winning count
        #Created an empty string to hold the name of the candidate who has the highest vote count
    winner = ""
        # Initialized to 0 to keep track of the highest number of votes
    highest_vote_count = 0

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in dictionary:

        # Get the vote count and calculate the percentage
        votes = dictionary[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > highest_vote_count:
            highest_vote_count = votes
            winner = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    # Generate and print the winning candidate summary
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Save the winning candidate summary to the text file
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")