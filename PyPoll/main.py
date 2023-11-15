# Import modules
import csv

# File Paths
election_csv = r"PyPoll/Resources/election_data.csv"
election_output_txt = r"PyPoll/analysis/election_output.txt"

# Declare Variables
line = '-------------------------'
total_votes = 0
unique_name = []
candidate_votes = []

# open and create reader
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    # skip the header
    csv_header = next(csv_reader)

    # loop thru each row
    for row in csv_reader:
        # add to total_vote count
        total_votes += 1
        # extract candidate name from the current row
        candidate_name = (row[2])
        # candidate already in unique_name? If so, just add to their vote count
        if candidate_name in unique_name:
            candidate_index = unique_name.index(candidate_name)
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        # If not, add to unique_name and add to their vote count
        else:
            unique_name.append(candidate_name)
            candidate_votes.append(1)

percentage = []
most_votes = candidate_votes[0]
candidate_most_votes = 0

# loop thru unique_name
for x in range(len(unique_name)):
    # calculate percentage - REMEMBER: 3 deci
    vote_percentage = round(candidate_votes[x]/total_votes*100, 3)
    percentage.append(vote_percentage)
    # check if current candidate has highest number of votes
    if candidate_votes[x] > most_votes:
        # if so, update number of most votes
        most_votes = candidate_votes[x]
        # and save index of the candidate with the most votes
        candidate_most_votes = x
# Save winner variable with name of candidate with the most votes
winner = unique_name[candidate_most_votes]

# Print to terminal
print('Election Results')
print(f'{line}')
print(f'Total Votes: {total_votes}')
print(f'{line}')
for x in range(len(unique_name)):
    print(f'{unique_name[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})')
print(f'{line}')
print(f'Winner: {winner}')
print(f'{line}')

with open(election_output_txt, "w") as output_txt_file:
    output_txt_file.write(f'Election Results\n')
    output_txt_file.write(f'{line}\n')
    output_txt_file.write(f'Total Votes: {total_votes}\n')
    output_txt_file.write(f'{line}\n')
    for x in range(len(unique_name)):
        output_txt_file.write(f'{unique_name[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})\n')
    output_txt_file.write(f'{line}\n')
    output_txt_file.write(f'Winner: {winner}\n')
    output_txt_file.write(f'{line}\n')