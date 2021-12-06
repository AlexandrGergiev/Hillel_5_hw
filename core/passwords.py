import hashlib
import base64
import random


def hash_password_raw(password: str) -> str:
    pepper = get_peppered()
    pepper_password = password + pepper
    hash_data = hashlib.sha256(pepper_password.encode("utf-8"))
    return base64.b64encode(hash_data.digest()).decode("utf-8")


def hash_password(password: str) -> str:
    salt = get_salt()
    return hash_password_raw(password + ":" + salt) + ":" + salt


def get_salt() -> str:
    salt_number = random.randint(0, 2 ** 256 - 1)
    return base64.b64encode(salt_number.to_bytes(32, "little")).decode("utf-8")


def get_peppered() -> str:
    pepper = "my_super_secret_pepper_228" + str(random.randint(0, 2 ** 32 - 1))
    return pepper


def passwords_equal(password: str, hash: str) -> bool:
    raw_hash, salt = hash.split(":", 2)
    return hash_password(password + get_peppered() + ":" + salt) == raw_hash
