import requests

def convert_currency(base_currency, target_currency, amount):
    """
    Converts an amount from a base currency to a target currency 
    using live exchange rates.
    """
    # Using a free public API endpoint (no API key required for basic usage)
    url = f"https://open.er-api.com/v6/latest/{base_currency.upper()}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if the request was successful
        if data.get("result") == "success":
            rates = data.get("rates", {})
            target_currency = target_currency.upper()
            
            if target_currency in rates:
                rate = rates[target_currency]
                converted_amount = amount * rate
                return converted_amount, rate
            else:
                print(f"Error: Target currency '{target_currency}' not found.")
                return None, None
        else:
            print("Error: Failed to fetch exchange rates from the API.")
            return None, None
            
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None, None

def main():
    print("=== Simple Python Currency Converter ===")
    
    # Get user inputs
    base = input("Enter base currency (e.g., USD, EUR, GBP): ").strip()
    target = input("Enter target currency (e.g., UGX, JPY, CAD): ").strip()
    
    try:
        amount = float(input(f"Enter amount in {base.upper()}: "))
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return

    print("\nFetching live rates...")
    converted, rate = convert_currency(base, target, amount)
    
    if converted is not None:
        print("\n----------------------------------------")
        print(f"Exchange Rate: 1 {base.upper()} = {rate:.4f} {target.upper()}")
        print(f"Result: {amount:,.2f} {base.upper()} = **{converted:,.2f} {target.upper()}**")
        print("----------------------------------------")

if __name__ == "__main__":
    main()
