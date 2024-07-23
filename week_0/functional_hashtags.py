
def hashtag(words) -> str:
    new = ["#"]
    words = words.split()
    for word in words:
        word = list(word)
        word[0] = word[0].upper()
        for i in range(1, len(word)):
            word[i] = word[i].lower()
        new.append("".join(word))
    return "".join(new)

# msg = hashtag('Putting the FUN in FUNCTIONS')
# print(msg)