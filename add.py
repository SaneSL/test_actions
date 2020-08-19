from cryptography.fernet import Fernet

def test_crypt():
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"Test")
    k = f.decrypt(token)

def add(*args):
    total = sum(args)
    return total