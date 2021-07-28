# Arbitrage Calculator, Takes two decimal odds as input 
# and an optional argument for stake 
# and returns whether an arbitrage situation is present

def expected_value(odds_a, odds_b, stake=100):
    # To Convert Decimal odds to Implied Probability 
    implied_prob_a = (1/odds_a)
    implied_prob_b = (1/odds_b)

    #implied probability of event will exceed 1 in non-arbitrage situations
    implied_prob = implied_prob_a + implied_prob_b

    #when implied prob < 1 arbitrage situation is present
    #bookmaker_fee = implied_prob - 1.0
    expected_value = (stake / implied_prob) - stake

    return round(expected_value,2)

def find_margin(a, b):

    #calculates the bookmakers margin
    market_margin_percent = round((1/a + 1/b - 1)*100, 2)
    
    return market_margin_percent
    

def size_bets(a, b, total_stake=100):
    
    payout = total_stake + (expected_value(a,b,total_stake))
    
    #Calculate Size of Stake for Each Bet
    a_stake = round((payout / a ),2)
    b_stake = round((payout / b ),2)

    return a_stake, b_stake


def main():
    a_odds = float(input("Decimal Odds of Event A: "))
    b_odds = float(input ("Decimal Odds of Event B: "))
    stake = int(input("Stake: $"))

    print(f"\nBookMakers Margin: {find_margin(a_odds,b_odds)}%\n")
    print(f"Expected Value: ${expected_value(a_odds,b_odds, stake)} \n")
    print(f"Size Bets A, B: {size_bets(a_odds,b_odds,stake)} ")

if __name__ == '__main__':
    main()
