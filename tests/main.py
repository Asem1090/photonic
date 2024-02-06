import src.photonic.crypto.hash as hsh


def main():
    path = (r"C:\Users\asems\OneDrive - Qatar University\University\2024 Spring\Special Topic In Digital "
            r"Forensics\Labs\lab 1\Lab 1\Lab 1\\")
    full_path = path + "dog.jpg"

    key = b"XYZAZYX"
    print(f"Integrate: {hsh.getHMAC(full_path, key) == 'e70e845d7253f3295e3b42f3a8548917'}")


if __name__ == "__main__":
    main()
