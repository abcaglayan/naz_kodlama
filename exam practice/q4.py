def createAlphabet():
    alphabet = []
    index = 0
    while index < 26:
        char_to_be_added = chr(97 + index)
        alphabet.append(char_to_be_added)
        index += 1
    return alphabet

letter = input("Enter a lowercase letter: ")
a = createAlphabet()
if letter in a:
    print("The position of the letter is", a.index(letter) + 1)
else:
    print("This is not a lower case letter...")


def clean_tweet(tweet):
    return ' '.join(tweet.split())

def process_tweets(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    for line in lines:
        cleaned = clean_tweet(line)
        print(cleaned)

process_tweets("tweet.txt")




scores = {"A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2,
 		"H":4, "I":1, "J":8, "K":5, "L":1, "M":3, "N":1,
        "O":1, "Q": 10, "R":1, "S":1, "T":1, "U":1,
        "V":4, "W":4, "X":8, "Y":4, "Z":10}

def scrabble_score(word):
    total = 0
    for letter in word:
        total += scores[letter]
    print(total)
    return total

scrabble_score("DENEME")

def build_population_dict(filename):
    population_dict = {}
    file = open(filename, "r")
    for line in file:
        parts = line.strip().split()
        if len(parts) != 2:
            continue  # skip malformed lines
        _, city = parts
        if city in population_dict:
            population_dict[city] += 1
        else:
            population_dict[city] = 1
    file.close()
    return population_dict

population_data = build_population_dict("population.txt")

city_name = input("Enter a city name: ")

if city_name in population_data:
    print(f"Population of {city_name}: {population_data[city_name]}")
else:
    print("City not found in the database.")