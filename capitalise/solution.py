

def capitalise(word):
    if len(word) == 0:
        return word
    return word[0].upper() + word[1:]

# I recommend you start by calling capitalise with the string "hello"

# Advanced hint: When you've called the function with a string, you can also run this file with a runtime called bun (just run bun <path-to-file>)
# bun runs JS files like node but with a few differences - can you spot any differences?

print(capitalise('ian'))