from hmac import new
from hashlib import md5, sha1, sha512


def getMD5(binary_data):
    return md5(binary_data).hexdigest()


def getSHA1(binary_data):
    return sha1(binary_data).hexdigest()


def getSHA512(binary_data):
    return sha512(binary_data).hexdigest()


def getHMAC(binary_data, key):
    return new(key, binary_data, md5).hexdigest()