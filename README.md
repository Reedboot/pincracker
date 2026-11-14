# PIN Cracker

An educational command-line demonstration of exhaustive search against a
user-entered PIN. It illustrates how the number of possible combinations grows
with PIN length and how a program can test candidates one at a time.

## What it does

The program asks you to enter a PIN locally, then searches candidate numeric
strings from one digit up to six digits until it finds that value. It reports
the number of attempts and elapsed time. The PIN is read without echoing it to
the terminal.

This is a self-contained demonstration: it does not connect to a device,
account, network service, or PIN-protected system, and it cannot test a PIN
against any such target. Do not adapt brute-force techniques to access systems
without authorization.

## Requirements

- Python 3
- A terminal

## Run

From the project directory:

```sh
python3 pin_cracker.py
```

Or, if the shell script is executable:

```sh
./run.sh
```

Enter a PIN containing one to six ASCII digits when prompted. Leading zeroes
are supported. The search space for all PIN lengths from one through six is
`10 + 100 + 1,000 + 10,000 + 100,000 + 1,000,000` candidates.

## Educational notes

For a fixed length of `n` digits, there are `10^n` possible PINs. Exhaustive
search therefore scales exponentially with the number of digits. Real systems
should not rely on PIN length alone: rate limits, lockouts, and secure
credential handling help prevent repeated guesses.

## License

No license has been specified for this project.
