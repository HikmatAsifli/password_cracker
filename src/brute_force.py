import hashlib
import bcrypt
import string
from itertools import product

# Hashing functions for each algorithm
def hash_password(password, algorithm):
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'bcrypt':
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def brute_force_crack(password_hash, algorithm):
    chars = string.ascii_lowercase + string.digits
    max_length = 10  # Start with shorter length for testing

    for length in range(1, max_length + 1):
        for guess in product(chars, repeat=length):
            guess = ''.join(guess)
            print(f"Trying: {guess}")  # Log each guess
            if algorithm == 'bcrypt':
                if bcrypt.checkpw(guess.encode(), password_hash.encode()):
                    print(f"Password found: {guess}")
                    return
            else:
                if hash_password(guess, algorithm) == password_hash:
                    print(f"Password found: {guess}")
                    return
    print("Password not found")


