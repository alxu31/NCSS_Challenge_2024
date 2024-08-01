'''
For some reason grok hates my code just because I did it differently
e.g. I took 2 params but it didnt allow that so i put them in a tuple as one param, but they want a single int. (smh)
=> then it doesnt like the fact I'm using a global variable in the function which means 
I have to hardcode the number of runs (1-100)...
meaning I can't change the runs easily through one var
'''
def linear_search(info) -> int:
    num, ran = info
    for tries in range(1, ran + 1):
        if tries == num: return tries

def binary_search(info) -> int:
    num, ran = info
    left = 1
    right = ran

    for tries in range(1, ran//2):
        mid = (left + right)//2

        if num > mid: left = mid + 1
        elif num < mid: right = mid - 1
        else: return tries

def calculate_winner(ran) -> tuple:
    equals = 0
    linWins = 0
    binWins = 0
    for i in range(1, ran + 1):
        linTries = linear_search((i, ran))
        binTries = binary_search((i, ran))

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
    