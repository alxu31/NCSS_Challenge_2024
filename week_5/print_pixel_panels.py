import csv
import json

with open("nozzle_config.json") as f:
    nozzle_flows = json.load(f)

def rgb_to_cmyk(red, green, blue) -> dict:
    red, green, blue = map(lambda x: x / 255, (red, green, blue))
    black = 1 - max(red, green, blue)
    cyan = ((1 - red - black) / (1 - black)) if black != 1 else 0
    magenta = ((1 - green - black) / (1 - black)) if black != 1 else 0
    yellow = ((1 - blue - black) / (1 - black)) if black != 1 else 0
    cyan, magenta, yellow, black = map(lambda x: int(x * 100), (cyan, magenta, yellow, black))
    return { "cyan": cyan, "magenta": magenta, "yellow": yellow, "black": black }

#! resources/->rgberr.csv,rgbw.csv,rick.csv
inputFile = input("Input file: ")
cmyks = []
order = {}
with open(inputFile) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for i, line in enumerate(csvreader):
        print(line)
        for item in line:
            if (int(item) < 0 or int(item) > 255):
                print(f"Invalid ink value on tile {i+1}.") 
        cmyk = rgb_to_cmyk(int(line[0]), int(line[1]), int(line[2]))
        cmyks.append(cmyk)
    print(cmyks)

for j in range(len(cmyks)):
    temp = []
    for colour in nozzle_flows.keys():
        temp.append(cmyks[j][colour]*nozzle_flows[colour])
    print(max(temp))
    order[j+1] = max(temp)

for key in dict(sorted(order.items(), key=lambda item: item[1])).keys():
    print(key)