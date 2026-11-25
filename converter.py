"""Convert Celsius to Fahrenheit from the command line."""

import argparse


def format_fahrenheit(celsius: float) -> str:
    fahrenheit = celsius * 9 / 5 + 32
    return f"{fahrenheit:.2f}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("celsius", type=float, help="temperature in Celsius")
    args = parser.parse_args()
    print(format_fahrenheit(args.celsius))


if __name__ == "__main__":
    main()
