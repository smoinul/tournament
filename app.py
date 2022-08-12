from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    team = [
        ["Rajib", "Xpandan", "Robiul", "Ashiq Baten", "Mushfique", "Tahshin", "Moinul", "Naser"],
        ["Mostafa", "Tanvir", "Junayed", "Promit", "Rashed", "Rezaul", "Rafi", "Mosfik"],
        ["Sujel", "Farhan", "Rishov", "Asif", "Hafeez", "Sayem", "Sajal", "Rasi"]
    ]

    for playerNumber in range(0, 8):
        temp = ["1", "2", "3"]
        for teamNumber in range(0, 3):
            temp[teamNumber] = team[teamNumber][playerNumber]
        random.shuffle(temp)
        for teamNumber in range(0, 3):
            team[teamNumber][playerNumber] = temp[teamNumber]
    result = ""
    for teamNumber in range(0, 3):
        string = ','.join(str(x) for x in team[teamNumber])
        result = result + "\n" + string
    return result

if __name__ == "__main__":
    app.run()
