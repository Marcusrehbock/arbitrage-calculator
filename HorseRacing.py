import random
import matplotlib.pyplot as plt
import math


#Want to graph what the profability of a BB is over time

class Bettor():
    def __init__(self, wealth = 4000, bonusBets=0):

        self.wealth = wealth
        self.bonusBets = bonusBets
        self.wealthHistory = []
        self.bonusBetHistory = []
        self.expectedValue = []

    def earnBonusBets(self, numberOfRaces, betSize=50,):
         for iteration in range(numberOfRaces):

            winner = random.randint(1, 100)

            if (winner > 50): #bonus bet 
                self.bonusBets += betSize
                self.bonusBetHistory.append(self.bonusBets)
                #self.wealth -= betSize 
                #self.wealthHistory.append(self.wealth)


            self.wealth -= betSize * 0.15
            self.wealthHistory.append(self.wealth)

    
    def convertBonusBet(self, bonusBetSize=50, odds=3):

        for iteration in range(round(self.bonusBets/bonusBetSize)):
            choises = []

            #odds to implied odds to number of possibilities
            impliedOdds = round((1/odds) * 100)
            
            winner = random.randint(1, 100)
                       
            if (winner > impliedOdds): #lost bonus bet 
                self.bonusBets -= bonusBetSize
                self.wealth -= 10
                self.wealthHistory.append(self.wealth)
                self.bonusBetHistory.append(self.bonusBets)

            else :
                self.bonusBets -= bonusBetSize
                self.bonusBetHistory.append(self.bonusBets)
                self.wealth += (odds * bonusBetSize) - bonusBetSize
                self.wealthHistory.append(self.wealth)
       

        #for odds in range(25):
#
 #           if odds != 0 :
#
 #
   #             valueReturned = (odds * bonusBet) - bonusBet
#
 #               expectedValue = valueReturned * impliedProbability
##               self.expectedValue.append(expectedValue)

        
    
def main():
    
    Aaron = Bettor(4000,0)
    Aaron.earnBonusBets(2000, 50)
    Aaron.convertBonusBet(50,14)

    plt.plot(Aaron.wealthHistory)
    #plt.plot(Aaron.bonusBetHistory)

    plt.ylabel("Welath/BonusBets")
    plt.xlabel("Number of Bets")
    plt.title("Profit from Bonus over Time")
    plt.show()
    
    
    
if __name__ == '__main__':
    main()
