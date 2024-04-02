from src.photonic.crypto.stegno import lsb_hide, lsb_reveal
from src.photonic.utils.time_utils import print_run_time


PATH = r"C:\Users\asems\OneDrive - Qatar University\Desktop\test.txt"

def main():
    lsb_hide(PATH, "This is a secret")
    print(lsb_reveal(PATH))


if __name__ == "__main__":
    main()
