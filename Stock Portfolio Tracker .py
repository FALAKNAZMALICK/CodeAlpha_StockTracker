import os
print("Current working directory:", os.getcwd())

def stock_tracker():
    # 1. Hardcoded dictionary
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 150,
        "AMZN": 400,
        "META": 450
    }

    print("--- Portfolio Tracker ---")
    print("Prices today: AAPL:$180, TSLA:$250, GOOG:$150, AMZN:$400, META:$450")

    portfolio = {}

    while True:
          symbol = input("\nEnter Stock Name (or type 'done'): ").upper().strip()

          if symbol == 'DONE':
             break

          if symbol in stock_prices:
            try:
                qty = int(input(f"How many shares of {symbol} do you have? "))
                portfolio[symbol] = qty
            except ValueError:
                print(" Please enter a number for quantity.")
          else:
            print("That stock isn't in our system.")

    # 2. Calculating Total Investment
    total_value = 0
    report_lines = ["--- Portfolio Report ---\n"]

    for name, qty in portfolio.items():
        price = stock_prices[name]
        cost = qty * price
        total_value += cost
        line = f"{name}: {qty} shares @ ${price} = ${cost}"
        report_lines.append(line + "\n")
        print(f"{line}")

    final_summary = f"\n TOTAL PORTFOLIO VALUE: ${total_value}"
    report_lines.append(final_summary)
    print(final_summary)

    # 3. Save to .txt file
    save_choice = input("\nWould you like to save this report to a file? (yes/no): ").lower()
    if save_choice == 'yes':
        with open("portfolio_report.txt", "w") as f:
            f.writelines(report_lines)
        print(" Saved!")

if __name__ == "__main__":
    stock_tracker()