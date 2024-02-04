from hashlib import md5, sha1, sha512


def getMD5(file_path):
    with open(file_path, "rb") as file:
        return md5(file.read()).hexdigest()


def getSHA1(file_path):
    with open(file_path, "rb") as file:
        return sha1(file.read()).hexdigest()


def getSHA512(file_path):
    with open(file_path, "rb") as file:
        return sha512(file.read()).hexdigest()