# 10.12 Project: Currency Converter
# This is the main script and will import exchange_rates.py to access the exchange rates
import exchange_rates

# Functions for conversion calculations
def convert_usd_to_eur(usd):
    eur = usd * exchange_rates.USD_TO_EUR
    return eur

def convert_usd_to_gbp(usd):
    gbp = usd * exchange_rates.USD_TO_GBP
    return gbp

def convert_usd_to_jpy(usd):
    jpy = usd * exchange_rates.USD_TO_JPY
    return jpy

# Function where all the main code is
def main():
    usd = 17.00

    eur = convert_usd_to_eur(usd)
    gbp = convert_usd_to_gbp(usd)
    jpy = convert_usd_to_jpy(usd)

    print(f"${usd} is \u20AC{eur}")
    print(f"${usd} is £{gbp}")
    print(f"${usd} is \u00A5{jpy}")

if __name__ == "__main__":
    main()