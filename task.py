import csv

with open('moma.csv', newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row['DisplayName'], row['Gender'],row['ArtistBio'], sep=';')

