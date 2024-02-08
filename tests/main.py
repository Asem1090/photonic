import src.photonic.crypto.hash as hsh


def main():
    path = (r"C:\Users\asems\OneDrive - Qatar University\University\2024 Spring\Special Topic In Digital "
            r"Forensics\Labs\lab 1\Lab 1\Lab 1\\")
    # secret_message = "Assalam Alikum"
    # byte_message = "".join(format(ord(c), "08b") for c in secret_message)
    # hsh.getHMAC(byte_message, )
    file_name = "Hashes.txt"
    with open(path + file_name, "r") as file:
        hashes = dict(line.split(" : ") for line in file.read().splitlines())

    print(f"{'File Name':<20}{'Integrate':<20}")
    for file_name, _hash in hashes.items():
        with open(path + file_name, "rb") as file:
            print(f"{file_name:<20}{_hash.lower() == hsh.getMD5(file.read())}")


if __name__ == "__main__":
    main()
