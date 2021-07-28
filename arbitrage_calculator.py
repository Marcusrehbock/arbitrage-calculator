# Arbitrage Calculator, Takes two decimal odds as input 
# and an optional argument for stake 
# and returns whether an arbitrage situation is present

def arbitrage(odds_a, odds_b, stake=100):
    # To Convert Decimal odds to Implied Probability 
    implied_prob_a = (1/odds_a)
    implied_prob_b = (1/odds_b)

    #implied probability of event will exceed 1 in non-arbitrage situations
    implied_prob = implied_prob_a + implied_prob_b

    #when implied prob < 1 arbitrage situation is present
    #bookmaker_fee = implied_prob - 1.0

    return round(stake * (1 - implied_prob), 2)

def main():
    a = float(input("Decimal Odds of Event A: "))
    b = float(input ("Decimal Odds of Event B: "))
    print(f"Expected Value: ${arbitrage(a,b)} ")

if __name__ == '__main__':
    main()
