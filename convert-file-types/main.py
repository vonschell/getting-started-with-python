import json

show_data = []

# Open the television_shows.txt file in read mode
with open("television_shows.txt", "r") as text_file:
    for line in text_file:
        show_data.append(line)

# Open a new file called best_shows.json in write mode
with open("best_shows.json", "w") as write_file:
    json.dump(show_data, write_file)
    