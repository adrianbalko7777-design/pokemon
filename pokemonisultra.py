import json
#budu dva typy jedno-typový a dvoj-typový


attackfield = {}
fr = open("effectiveness.json", "r")
data = json.load(fr)


helper = {"super effective": 2, "normal effective": 1, "not very effective": 0.5, "no effect": 0}

for strenght in data:
    for attacker in data[strenght]:
        if attacker not in attackfield.keys():
            attackfield[attacker] = {}
        for defender in data[strenght][attacker]:
            attackfield[attacker][defender] = helper[strenght]


def attack(P1: int, P2: int, army: str) -> str:
    temp = army.split(",")
    army1 = temp[:P1]
    army2 = temp[P1:]

    # print(attackfield) a
    # print(attackfield["Fire"]["Psychic"])

    #Výpočet útočnej sily prvého tímu na druhý tím
    power1 = 0.0
    for attacker_str in army1:
        attacker_types = attacker_str.split(" ")
        for defender_str in army2:
            defender_types = defender_str.split(" ")

            # Nájdeme najsilnejší útok útočníka (ak má 2 typy, vyberie ten výhodnejší)
            max_attacker_power = 0.0
            for a_type in attacker_types:
                current_power = 1.0
                for d_type in defender_types:
                    # Zistíme efektivitu z tabuľky attackfield, ak tam kombinácia nie je, je to 1.0
                    if a_type in attackfield and d_type in attackfield[a_type]:
                        effect = attackfield[a_type][d_type]
                    else:
                        effect = 1.0
                    current_power = current_power * effect

                if current_power > max_attacker_power:
                    max_attacker_power = current_power

            power1 = power1 + max_attacker_power

#Výpočet útočnej sily druhého tímu na prvý tím
    power2 = 0.0
    for attacker_str in army2:
        attacker_types = attacker_str.split(" ")
        for defender_str in army1:
            defender_types = defender_str.split(" ")

            max_attacker_power = 0.0
            for a_type in attacker_types:
                current_power = 1.0
                for d_type in defender_types:
                    if a_type in attackfield and d_type in attackfield[a_type]:
                        effect = attackfield[a_type][d_type]
                    else:
                        effect = 1.0
                    current_power = current_power * effect

                if current_power > max_attacker_power:
                    max_attacker_power = current_power

            power2 = power2 + max_attacker_power

    power1 = round(power1, 1)
    power2 = round(power2, 1)

    if power1 > power2:
        result_str = "ME"
    elif power2 > power1:
        result_str = "FOE"
    else:
        result_str = "EQUAL"

    return f"({power1},{power2},\"{result_str}\")"

print(attack(2, 6, "Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))