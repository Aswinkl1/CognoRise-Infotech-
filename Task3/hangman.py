import hangmanart
import hangmanword
import random


words = hangmanword.word_list
stages = hangmanart.stages
answer = []
random_word = random.choice(words)
# print(random_word)
for i in range(0, len(random_word)):
    answer.append("_")
index = 0
print(answer.count("-"))
number_of_life = 7

print(hangmanart.logo)
while True:
    user_input = input("Guess a letter: ").lower()
    # Clearing the Screen

    if answer.count(user_input) != 0:
        print(f"you have already guessed {user_input}")
    wrong_letter = True
    for position in range(len(random_word)):
        if user_input == random_word[position]:
            answer[position] = user_input
            wrong_letter = False
    print(f'{" ".join(answer)}')
    if wrong_letter:
        print(f"you guessed {user_input}, that's not in the word . you loose a life")
        print(stages[number_of_life - 1])
        number_of_life -= 1

    if answer.count("_") == 0:
        print("You Win")
        break
    elif number_of_life == 0:
        print("You loose")
        break

print(f"The answer is {random_word}")