def main():
    ratings = {
        "Inception": 9,
        "Interstellar": 8,
        "Matrix": 9,
        "Avatar": 7
    }

    print_movie_ratings(ratings)
    average_rating = average_ratings(ratings)
    print("Average rating:", average_rating)
    highest_movie, highest, lowest_movie, lowest = highest_lowest_rating(ratings)
    print(f"highest rating movie is {highest_movie} with rating of:", highest)
    print(f"lowest rating  movie is {lowest_movie} with rating of:", lowest)


def print_movie_ratings(ratings):
    for key in ratings:
        print(f"{key}: {ratings[key]}")

def average_ratings(ratings):
    total_key = len(ratings)
    total = 0
    for key in ratings:
        total += ratings[key]
    return total/total_key

def highest_lowest_rating(ratings):
    highest = float("-inf")
    highest_movie = ""

    lowest = float("inf")
    lowest_movie = ""

    for key in ratings:
        value = ratings[key]

        if value > highest:
            highest_movie = key
            highest = value
        
        if value < lowest:
            lowest_movie = key
            lowest = value
    return highest_movie, highest, lowest_movie, lowest

if __name__ == "__main__":
    main()