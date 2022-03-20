import random
import matplotlib.pyplot as plt


class Bettor():
    def __init__(self, bankroll=1000):
        self.bankroll = bankroll
        self.bankrollHistory = [1000]
        self.iteration = []

    def coinToss(self, numberOfFlips, odds, amount):
        
        for iteration in range(numberOfFlips):
            self.iteration.append(iteration)
        
            bettorsPick = random.choice(["Heads", "Tails"])
            self.bankroll -= amount
            result = random.choice(["Heads", "Tails"])

            if (bettorsPick == result):
                self.bankroll += amount * odds
                
            self.bankrollHistory.append(self.bankroll)

            
                

def main():
    
    Aaron = Bettor(1000)
    Aaron.coinToss(100000, 2.1, 100)

    Bryan = Bettor(1000)
    Bryan.coinToss(100000, 2.0, 100)

    Charlie = Bettor(1000)
    Charlie.coinToss(100000, 1.9, 100)

    print(Charlie.bankrollHistory)

    plt.plot(Charlie.bankrollHistory)
    plt.plot(Aaron.bankrollHistory)
    plt.plot(Bryan.bankrollHistory)
    plt.ylabel("Cumulative Profit")
    plt.xlabel("Iteration")
    plt.title("Profit from coin Toss over Time")
    plt.show()
    
    
    
if __name__ == '__main__':
    main()
