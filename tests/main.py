import src.photonic.crypto.hash as hsh


def main():
    path = (r"C:\Users\asems\OneDrive - Qatar University\University\2024 Spring\Special Topic In Digital "
            r"Forensics\Labs\lab 1\Lab 1\Lab 1\\")
    full_path = path + "Cat.jpg"

    print("MD5: " + hsh.getMD5(full_path))
    print("SHA1: " + hsh.getSHA1(full_path))
    print("SHA512: " + hsh.getSHA512(full_path))


if __name__ == "__main__":
    main()
