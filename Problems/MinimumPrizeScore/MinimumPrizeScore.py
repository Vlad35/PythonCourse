# Read input from file
with open("data/participants.txt", "r") as f_in:
    lines = f_in.readlines()

# Process the data
scores = []
for line in lines:
    name, score = line.rsplit(' ', 1)
    score = int(score)
    scores.append((name, score))

# Sort the scores in decreasing order
scores.sort(key=lambda x: x[1], reverse=True)

# Find the index of the last participant in the top 45%
num_participants = len(scores)
num_winners = int(num_participants * 0.45)
if num_winners == num_participants:
    num_winners -= 1
last_top_45_score = scores[num_winners - 1][1]
while num_winners < num_participants and scores[num_winners][1] == last_top_45_score:
    num_winners += 1

# Find the maximum possible score and half of it
max_score = scores[0][1]
half_max_score = max_score // 2

# Find the minimum score of the prize-winners
min_winner_score = max_score
for i in range(num_winners):
    name, score = scores[i]
    if score > half_max_score:
        min_winner_score = min(min_winner_score, score)
    else:
        break

# Write output to file
with open('data/result.txt', "w") as f_out:
    f_out.write(str(min_winner_score))
