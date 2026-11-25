# Celsius to Fahrenheit

A small Python script for my UCS 745 Cloud and DevOps lab. It takes one Celsius value and prints the Fahrenheit result.

```text
$ python3 converter.py 37
98.60 °F
$ python3 converter.py -40
-40.00 °F
```

## Where Git got stuck

I made two branches from the same starting commit. On `feature/precision` I changed the return line to show two decimal places. On `feature/unit-label` I changed that same line to add `°F`.

I merged precision into `main` first. When I tried to merge the unit branch, Git stopped in `converter.py`. I checked both lines in `git diff` and combined them:

```python
return f"{fahrenheit:.2f} °F"
```

The resolution is in merge commit [`2906d8b`](https://github.com/ManasMehta12/ucs745-temperature-converter/commit/2906d8be9b35ebf2b904bee25c9e463706a56fe7).
