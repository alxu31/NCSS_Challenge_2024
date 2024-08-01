
def linear_search(num) -> int:
    for tries in range(1, 101):
        if tries == num: return tries

def binary_search(num) -> int:
    left = 1
    right = 100

    for tries in range(1, 50):
        mid = (left + right)//2

        if num > mid: left = mid + 1
        elif num < mid: right = mid - 1
        else: return tries

def calculate_winner(ran) -> tuple:
    equals = 0
    linWins = 0
    binWins = 0
    for i in range(1, ran + 1):
        linTries = linear_search(i)
        binTries = binary_search(i)

        if binTries < linTries: binWins += 1
        elif binTries > linTries: linWins += 1
        else: equals += 1

    return binWins, linWins, equals


if __name__ == '__main__':
    ran = 100
    print("Search showdown")
    print("---------------")
    print()

    binary_result, linear_result, equal = calculate_winner(ran)

    print(f"Binary search was quickest {binary_result}% of the time.")
    print(f"Linear search was quickest {linear_result}% of the time.")
    print(f"Both searches took the same number of guesses {equal}% of the time.")
    print()

    if binary_result == linear_result: print("It's a tie!!!!")
    else:
        if binary_result > linear_result: winner = "Binary"
        elif binary_result < linear_result: winner = "Linear"
        print(f"{winner} search wins!!!!")
    