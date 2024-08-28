"""
ok wtf i can't just return the statement needed to fill in the sentence for the player_won_battle function?
intead i have to reformat it after returning the predefined vars which cannot be directly inserted?
that's just bad design smh
"""

import random
import json
from dataclasses import dataclass

ARM_WRESTLE = "arm wrestle"
DANCE_OFF = "dance off"
RACE = "race"

PLAYER_WON = "player won"
PLAYER_LOST = "player lost"
TIE = "tie"

def random_battle_type() -> str:
    return random.choice([ARM_WRESTLE, DANCE_OFF, RACE])

def select_monatures(monatures, party_size, random_select) -> list:
    selected_monatures = []
    if random_select:
        selected_monatures = random.sample(monatures, party_size)
    else:
        selected_monatures = monatures[0:party_size]

    for selected_monature in selected_monatures:
        monatures.remove(selected_monature)
  
    return selected_monatures

@dataclass
class Monature:
    name: str = ""
    strength: int = 0
    flair: int = 0
    speed: int = 0

def load_monatures() -> list:
    mons = []
    with open('resources/monatures.json') as jsonfile:
    # with open('monatures.json') as jsonfile:
        info = json.load(jsonfile)
        for item in info['monatures']:
            mons.append(Monature(**item))
    return mons
    
def player_won_battle(player_monature, enemy_monature, battle_type) -> str:
    options = {"arm wrestle":"strength", "race":"speed", "dance off":"flair"}
    pmon = {"strength":player_monature.strength, "speed":player_monature.speed, "flair":player_monature.flair}
    emon = {"strength":enemy_monature.strength, "speed":enemy_monature.speed, "flair":enemy_monature.flair}
    if pmon[options[battle_type]] > emon[options[battle_type]]: return "beat"
    elif pmon[options[battle_type]] < emon[options[battle_type]]: return "lost to"
    else: return "tied with"

def output_parties(player_monatures, enemy_monatures) -> str:
    playerList = '[%s]' % ', '.join(map(str, [playermon.name for playermon in player_monatures]))
    enemyList = '[%s]' % ', '.join(map(str, [enemymon.name for enemymon in enemy_monatures]))
    return f"{playerList} vs {enemyList}"

if __name__ == "__main__":
    random_select = input("Random monatures?: ")
    random_select = random_select == "y"

    monatures = load_monatures()
    player_monatures = select_monatures(monatures, 3, random_select)
    enemy_monatures = select_monatures(monatures, 3, random_select)
    
    round = 1
    while len(player_monatures) > 0 and len(enemy_monatures) > 0:
        print(f"""
Round {round}
{output_parties(player_monatures,enemy_monatures)}
=====""")

        battle = 1
        tied = True
        while tied:
            mode = random_battle_type()
            currentp, currente = player_monatures[0], enemy_monatures[0]
            result = player_won_battle(currentp, currente, mode)
            if result == "lost to":
                tied = False
                player_monatures.remove(currentp)
            elif result == "beat":
                tied = False
                enemy_monatures.remove(currente)
            print(f"""
Battle {battle}
-----
Your {currentp.name} {result} the enemy's {currente.name} in a {mode}.""")
            battle += 1
        round += 1

    if len(enemy_monatures) == 0: print("", "You won! :)", sep="\n")
    else: print("", "You lost! :(", sep="\n")
