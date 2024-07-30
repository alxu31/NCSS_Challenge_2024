
def classification(l, w) -> str:
    if l < 2.5: return "Setosa"
    else:
        if w < 1.9: return "Versicolor"
        return "Virginica"

print("Iris flower classifier")
print("----------------------")
print()
run = True

while run:
    try:
        petalLength = float(input("Enter petal length: "))
        petalWidth = float(input("Enter petal width: "))
    except(TypeError):
        print("Petal width and length must be numbers.")
    print(f"Iris classification is {classification(petalLength, petalWidth)}")
    
    while True:
        print()
        keepClassifying = input("Classify another? (y)es or (n)o: ")
        if keepClassifying == "n":
            run = False
            break
        elif keepClassifying == "y": break
        else: print("Please respond with either (y)es or (n)o.")