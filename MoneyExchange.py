import requests

# Real-time currency converter using ExchangeRate-API
API_KEY = 'ebbe9b1e748f874c51f94302'  # Replace with your API key
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'


def get_supported_currencies():
    """Get a list of supported currencies from the API."""
    try:
        response = requests.get(BASE_URL + 'USD')  # Fetching rates based on USD
        if response.status_code == 200:
            data = response.json()
            return list(data['conversion_rates'].keys())  # Return list of supported currencies
        else:
            raise Exception("Error fetching supported currencies.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request error: {e}")


def get_exchange_rate(from_currency, to_currency):
    """Fetch real-time exchange rate between two currencies."""
    try:
        response = requests.get(BASE_URL + from_currency)
        if response.status_code == 200:
            data = response.json()
            rates = data['conversion_rates']
            return rates[to_currency]
        else:
            raise Exception(f"Error fetching exchange rate for {from_currency}.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request error: {e}")


def format_amount(amount):
    """Formats the number with commas and rounds to 2 decimal places."""
    return f"{amount:,.2f}"


def main():
    """Main function for real-time currency conversion."""
    while True:
        try:
            print("\nWelcome to the Real-Time Currency Converter!")

            # Get and display supported currencies
            supported_currencies = get_supported_currencies()
            print("\nSupported currencies:")
            for currency in supported_currencies:
                print(f" - {currency}")

            # Get user input
            amount = float(input("\nEnter the amount to convert: "))
            from_currency = input("Enter the source currency (e.g., USD, EUR, GBP): ").upper()
            to_currency = input("Enter the target currency (e.g., USD, EUR, GBP): ").upper()

            # Check if the currencies are supported
            if from_currency not in supported_currencies or to_currency not in supported_currencies:
                raise ValueError(f"Currency not supported: {from_currency} or {to_currency}")

            # Get the real-time exchange rate
            exchange_rate = get_exchange_rate(from_currency, to_currency)

            # Perform the conversion
            converted_amount = amount * exchange_rate
            print(
                f"\n{format_amount(amount)} {from_currency} is equal to {format_amount(converted_amount)} {to_currency}.")

            # Ask if the user wants to perform another conversion
            another_conversion = input("\nWould you like to perform another conversion? (yes/no): ").lower()
            if another_conversion != 'yes':
                print("Thank you for using the currency converter! Goodbye.")
                break

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


# Run the real-time currency converter
if __name__ == "__main__":
    main()