import random

cards = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
diler = ["Diler "]
player1 = ["Alex "]
player2 = ["Kairat "]

def start():
    for i in range(3):
        diler.append(random.choice(cards))
        player1.append(random.choice(cards))
        player2.append(random.choice(cards))

def winner():
    start()
    counter = 0
    max = 0
    max_name = []
    for i in diler, player1, player2:
        for card in i:
            if card.isdigit():
                counter += int(card)
            elif card in "JDK":
                counter += 10
            elif card == "A":
                counter += 11
        if counter > max:
            max = counter
            max_name = []
            max_name.append(i[0])
        elif counter == max:
            max_name.append(i[0])
        counter = 0
    return f"""
    -> {"-".join(diler)} -> {"-".join(player1)} -> {"-".join(player2)}
    Winners - {" ".join(max_name)} - ({max})"""



# if __name__ == "__main__":
#     print(winner())
