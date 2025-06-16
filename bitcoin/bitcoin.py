import requests
import sys


def main():
    if len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
    try:
        amount_btc = float(sys.argv[1])
        try:
            response = requests.get(
                "https://rest.coincap.io/v3/assets/bitcoin?apiKey=b07bc9535003c51d183138cae52ad825cfd67894b46f385461f0a06255062c49"
            )
            content = response.json()

            price_usd_for_btc = float(content["data"]["priceUsd"])

            amount = amount_btc * price_usd_for_btc
            print(f"${amount:,.4f}")

        except requests.RequestException:
            ...
    except:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()
