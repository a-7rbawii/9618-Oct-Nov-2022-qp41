class Card:
    def __init__(self, num, clr):
        self.__Number = num
        self.__Colour = clr
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

class Hand:
    def __init__(self, c1, c2, c3, c4, c5):
        self.__Cards = []
        self.__Cards.append(c1)
        self.__Cards.append(c2)
        self.__Cards.append(c3)
        self.__Cards.append(c4)
        self.__Cards.append(c5)
        self.__FirstCard = 0
        self.__NumberCards = 5

    def GetCard(self, choice):
        return self.__Cards[choice]

def CalculateValue(player):
    score = 0
    for i in range(4):
        cardGot = player.GetCard(i)
        score = score + cardGot.GetNumber()
        Colour = cardGot.GetColour()
        if Colour == "red":
            score = score + 5
        elif Colour == "blue":
            score = score + 10
        else:
            score = score + 15
    return score

OneR = Card(1,"red")
TwoR = Card(2,"red")
ThreeR = Card(3,"red")
FourR = Card(4,"red")
FiveR = Card(5,"red")

OneB = Card(1,"blue")
TwoB = Card(2,"blue")
ThreeB = Card(3,"blue")
FourB = Card(4,"blue")
FiveB = Card(5,"blue")

OneY = Card(1,"yellow")
TwoY = Card(2,"yellow")
ThreeY = Card(3,"yellow")
FourY = Card(4,"yellow")
FiveY = Card(5,"yellow")

player1 = Hand(OneR, TwoR, ThreeR, FourR, OneY)
player2 = Hand(TwoY, ThreeY, FourY, FiveY, OneB)

score1 = CalculateValue(player1)
score2 = CalculateValue(player2)

print("Player 1 score: {}".format(score1))
print("Player 2 score: {}".format(score2))

if score1 > score2:
    print("PLAYER 1 IS THE WINNER")
elif score2 > score1:
    print("PLAYER 2 IS THE WINNER")
else:
    print("MATCH IS A DRAW")