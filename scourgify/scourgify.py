import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    first_file = sys.argv[1]
    second_file = sys.argv[2]

    try:
        with open(f"{first_file}") as file, open(f"{second_file}", "w", newline='') as towrite_file:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(towrite_file, fieldnames = ['first', 'last', 'house'])
            writer.writeheader()

            for row in reader:
                last, first = row.get("name").split(", ")
                house = row.get("house")
                writer.writerow(
                    {
                        'first': first,
                        'last': last,
                        'house': house
                    }
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {first_file}")


if __name__ == "__main__":
    main()
