def implied_probability(decimal_odds):
    # To Convert Decimal odds to Implied Probability 
    implied_probability = round((1/decimal_odds) * 100, 2)


    return implied_probability


def main():
    decimal = float(input("Decimal Odds: "))
    print(f"Implied Probability: {implied_probability(decimal)}%")

if __name__ == '__main__':
    main()

