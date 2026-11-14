from getpass import getpass
import re
import shutil
import sys
import time


RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"

pin = ""


def center_text(text):
    terminal_width = shutil.get_terminal_size().columns
    visible_text = re.sub(r"\033\[[0-9;]*m", "", text)
    padding = max(0, (terminal_width - len(visible_text)) // 2)
    return f"{' ' * padding}{text}"


def search_pins_of_width(width, completed, total, started_at):
    for number in range(10**width):
        candidate = f"{number:0{width}d}"
        completed += 1

        if completed % max(1, total // 1000) == 0 or candidate == pin:
            progress = completed / total
            bar_width = 30
            filled = int(bar_width * progress)
            progress_text = (
                f"Progress: {'#' * filled}{'-' * (bar_width - filled)} "
                f"{progress:.1%}"
            )
            sys.stdout.write(
                f"\r{center_text(progress_text).replace(progress_text, '')}"
                f"{CYAN}Progress: {GREEN}{'#' * filled}"
                f"{'-' * (bar_width - filled)}{RESET} {progress:.1%}"
            )
            sys.stdout.flush()

        if candidate == pin:
            elapsed = time.perf_counter() - started_at
            print()
            print(center_text(f"{YELLOW}PIN found!{RESET}"))
            print(center_text(f"PIN: {pin}"))
            print(center_text(f"Attempts: {completed:,}"))
            print(center_text(f"Elapsed time: {elapsed:.2f} seconds"))
            raise SystemExit

    return completed


def main():
    global pin

    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    print(center_text(f"{CYAN}PIN CRACKER{RESET}"))
    print(center_text(f"{CYAN}================{RESET}"))
    print(center_text(f"{RED}For educational purposes only. Use only on PINs you own or are authorized to test.{RESET}"))
    print()
    print()
    print(center_text(f"{CYAN}Instructions{RESET}"))
    print(center_text(
        f"A {CYAN}6-digit{RESET} PIN has "
        f"{GREEN}1,000,000{RESET} possible combinations."
    ))
    print(center_text("Each digit has 10 choices (0-9), so calculate it as 10^6."))
    print(center_text("Searching PINs from 1 to 6 digits requires:"))
    print(center_text("10^1 + 10^2 + 10^3 + 10^4 + 10^5 + 10^6 = 1,111,110 combinations."))
    print()

    prompt_text = "PIN (1 to 6 digits (0-9)) > "
    prompt = f"{CYAN}{prompt_text}{RESET}"
    centered_prompt = center_text(prompt_text).replace(prompt_text, prompt)
    pin = getpass(centered_prompt)
    if not (1 <= len(pin) <= 6 and pin.isascii() and pin.isdigit()):
        message = "PIN must contain 1 to 6 digits (0-9)."
        print(center_text(f"{RED}{message}{RESET}"))
        return

    max_width = 6
    total = sum(10**width for width in range(1, max_width + 1))
    completed = 0
    started_at = time.perf_counter()

    for width in range(1, max_width + 1):
        completed = search_pins_of_width(width, completed, total, started_at)

    print()


if __name__ == "__main__":
    main()
