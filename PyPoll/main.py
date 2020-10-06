# ## PyPoll

import os
import csv

polling_csv = os.path.join("Resources", "election_data.csv")

votes = []
candidates = []
percentage_won = 0
candidate_votes = 0
winner = ""

# Open and read csv
with open(polling_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    header = next(csv_reader)
    
    for row in csv_reader:
        votes.append(row[0])
        candidates.append(row[2])
    total_votes = len(votes)
    
    candidates_list = candidates
    unique_candidates = set(candidates)
    #print(unique_candidates)

    OTooley = candidates_list.count("O'Tooley")
    Khan = candidates_list.count("Khan")
    Li = candidates_list.count("Li")
    Correy = candidates_list.count("Correy")

    OTooley_percentage = round(OTooley/total_votes*100, 2)
    Khan_percentage = round(Khan/total_votes*100, 2)
    Li_percentage = round(Li/total_votes*100, 2)
    Correy_percentage = round(Correy/total_votes*100, 2)

if Khan > Correy > Li > OTooley:
    Winner = "Khan"
elif Correy > Khan > Li > OTooley:
    Winner = "Correy"
elif Li > Khan > Correy > OTooley:
    Winner = "Li"
elif OTooley > Khan > Correy > Li:
    Winner = "O'Tooley"
    

print("""

Election Results
-------------------------
""")
print(f'Total number of votes were: {total_votes}')
print("""
-------------------------
""")
print(f'Khan: {Khan_percentage:.3f}% ({Khan})')
print(f'Correy: {Correy_percentage:.3f}% ({Correy})')
print(f'Li: {Li_percentage:.3f}% ({Li})')
print(f"O'Tooley: {OTooley_percentage:.3f}% ({OTooley})")
print(f"""
-------------------------

Winner: {Winner}
""")

output_file = os.path.join("analysis","results.txt")

with open(output_file,"w") as f:
    print("""

Election Results
-------------------------
""",file=f)
    print(f'Total number of votes were: {total_votes}',file=f)
    print("""
-------------------------
""",file=f)
    print(f'Khan: {Khan_percentage:.3f}%, ({Khan})',file=f)
    print(f'Correy: {Correy_percentage:.3f}%, ({Correy})',file=f)
    print(f'Li: {Li_percentage:.3f}%, ({Li})', file=f)
    print(f"O'Tooley: {OTooley_percentage:.3f}%, ({OTooley})",file=f)
    print(f"""
-------------------------
Winner: {Winner}
-------------------------
""",file=f)
