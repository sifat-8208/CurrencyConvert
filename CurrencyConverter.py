from forex_python.converter import CurrencyRates, RatesNotAvailableError
import requests

class CurrencyConverter:
    def __init__(self):
        self.cr = CurrencyRates()

    def get_conversion_rate(self, from_currency, to_currency):
        try:
            rate = self.cr.get_rate(from_currency, to_currency)
            return rate
        except RatesNotAvailableError:
            print(f"Error: Conversion rate between {from_currency} and {to_currency} is not available.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
        except Exception as e:
            print(f"Error fetching the conversion rate: {e}")
            return None

    def convert(self, amount, from_currency, to_currency):
        rate = self.get_conversion_rate(from_currency, to_currency)
        if rate:
            converted_amount = amount * rate
            return converted_amount
        return None

    def display_menu(self):
        print("Welcome to the Currency Converter!")
        print("Available currencies: USD, EUR, GBP, INR, JPY, AUD, CAD, and many more.")
        print("Type 'q' to quit.")
        
    def user_input(self):
        while True:
            from_currency = input("Enter the currency you want to convert from (e.g., USD, EUR): ").upper()
            if from_currency == 'Q':
                print("Goodbye!")
                break
            if not from_currency.isalpha() or len(from_currency) != 3:
                print("Invalid currency code. Please enter a valid 3-letter currency code (e.g., USD, EUR).")
                continue

            to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR): ").upper()
            if to_currency == 'Q':
                print("Goodbye!")
                break
            if not to_currency.isalpha() or len(to_currency) != 3:
                print("Invalid currency code. Please enter a valid 3-letter currency code (e.g., USD, EUR).")
                continue

            try:
                amount = float(input("Enter the amount to convert: "))
                if amount <= 0:
                    print("Please enter a valid positive amount.")
                    continue
            except ValueError:
                print("Invalid amount entered. Please enter a numeric value.")
                continue

            result = self.convert(amount, from_currency, to_currency)
            if result:
                print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
            else:
                print("Conversion failed. Please try again.")
            
            cont = input("Do you want to make another conversion? (y/n): ").lower()
            if cont != 'y':
                print("Goodbye!")
                break

if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.display_menu()
    converter.user_input()
