import csv
import json

with open("resources/nozzle_config.json") as f:
# with open("nozzle_config.json") as f:
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
order = {}
with open(inputFile) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for i, line in enumerate(csvreader):
        cols = list(map(int, line))
        calc = True
        for j in range(len(cols)):
            if (cols[j] < 0 or cols[j] > 255):
                print(f"Invalid ink value on tile {i+1}.")
                cmyk = { "cyan": 0, "magenta": 0, "yellow": 0, "black": 0 }
                calc = False
        if calc:
            cmyk = rgb_to_cmyk(cols[0], cols[1], cols[2])
        temp = []
        for colour in nozzle_flows.keys():
            temp.append(cmyk[colour]*nozzle_flows[colour])
        order[i+1] = max(temp)

for key in dict(sorted(order.items(), key=lambda item: item[1])).keys():
    print(key)