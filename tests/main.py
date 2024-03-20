from src.photonic.crypto.stegno import lsb_hide, lsb_reveal
from src.photonic.utils.time_utils import print_run_time

@print_run_time
def test1():
    y = 5
    for i in range(100_000_000):
        x = f"{y}\n{'5'}"


@print_run_time
def test2():
    y = 5
    for i in range(100_000_000):
        x = str(y) + "\n" + '5'


def main():
    test1()
    test2()
    try:
        ...
    except OSError:
        ...
    except FileNotFoundError:
        ...


if __name__ == "__main__":
    main()
