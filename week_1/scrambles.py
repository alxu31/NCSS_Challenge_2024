import random
random.seed(1)

print("Game of Scrambles!")
print("------------------")
print()

word_list = ['python', 'dinosaur', 'jumble', 'kangaroo', 'pumpkin'] 

score = 0
for i, item in enumerate(word_list, start=1):
    shuffled = list(item)
    random.shuffle(shuffled)
    shuffled = "".join(shuffled)
    print(f"Scrambled word {i}: {shuffled}")
    guess = input("Your guess: ")
    if guess == item:
        score += 1

print()
print(f"Your final score is: {score} out of {len(word_list)}!")