

movies = ["Movie A", "Movie B", "Movie C"]
ratings = [4.2, 4.8, 4.5]

print("Movie\t\tRating")

for i in range(len(movies)):
    print(movies[i], "\t", ratings[i])

best = max(ratings)
index = ratings.index(best)

print("\nRecommended Movie :", movies[index])
print("Rating :", ratings[index])