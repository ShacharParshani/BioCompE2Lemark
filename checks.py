import random
remain_letters = [chr(i) for i in range(97, 123)]  # set of remained letters
used_letters = {chr(i): [] for i in range(97, 123)}  # dictionary of number of instance for every letter
print(remain_letters)
print(used_letters)
for letter in used_letters:
    print("latter", letter)
    print(used_letters[letter])
    print(len(used_letters[letter]))
    if len(used_letters[letter]) > 1:
        rand_loc = random.choice(used_letters[letter])
        random_l = random.choice(remain_letters)
        remain_letters.remove(random_l)
