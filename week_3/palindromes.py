def is_palindrome(word) -> bool:
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        return True
    return False

if __name__ == '__main__':
    check_word = input("Enter the word(s) to check: ")
    if is_palindrome(check_word):
        print("The input is a palindrome.")
    else:
        print("The input is not a palindrome.")
