def get_score(competitors):
    return competitors[1]
competitors = [("Alice", 85), ("Bob", 99), ("Charlie", 82), ("David", 67), ("Alice", 15), ("Bob", 31), ("Charlie", 99), ("David", 19), ("Alice", 34), ("Bob", 25), ("Charlie", 90), ("David", 90)]
competitors.sort(key=get_score, reverse = True)
highest_score = competitors[0][1]
top_pi = [competitor[0] for competitor in competitors if competitor[1] == highest_score]
print(f'Highest scorers: ' + ", ".join(top_pi))
print(f'Highest score: ' + str(highest_score))