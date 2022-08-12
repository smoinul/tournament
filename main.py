import random

team = [
    ["Rajib", "Xpandan", "Robiul", "Ashiq Baten", "Mushfique", "Tahshin", "Moinul", "Naser"],
    ["Mostafa", "Tanvir", "Junayed", "Promit", "Rashed", "Rezaul", "Rafi", "Mosfik"],
    ["Sujel", "Farhan", "Rishov", "Asif", "Hafeez", "Sayem", "Sajal", "Rasi"]
]

for playerNumber in range(0,8):
    temp = ["1", "2", "3"]
    for teamNumber in range(0,3):
        temp [teamNumber]= team[teamNumber][playerNumber]
    random.shuffle(temp)
    for teamNumber in range(0, 3):
        team[teamNumber][playerNumber] = temp[teamNumber]

for teamNumber in range(0, 3):
    print (team[teamNumber])