# This code uses the re module to extract words from each sentence 

import re

# calculate_profanity function to count the number of racial slurs in each sentence

def calculate_profanity(sentence, profanity_list):
    profanity_count = 0
    words = re.findall(r'\w+', sentence)
    for word in words:
        if word.lower() in profanity_list:
            profanity_count += 1
    return profanity_count

# get_profanity_score function opens the given file and calculates the profanity score for each sentence.

def get_profanity_score(file_name, profanity_list):
    scores = []
    with open(file_name, 'r') as file:
        for line in file:
            score = calculate_profanity(line, profanity_list)
            scores.append((line, score))
    return scores
  
#   get_profanity_score function to get the scores for each sentence. The scores are then printed to the console.

def main():
    profanity_list = ["racial", "slur", "hate", "bigotry"]
    file_name = "tweets.txt"
    scores = get_profanity_score(file_name, profanity_list)
    for tweet, score in scores:
        print(f"Tweet: {tweet}")
        print(f"Profanity Score: {score}\n")

if __name__ == "__main__":
    main()
