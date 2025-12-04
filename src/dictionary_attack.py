import hashlib
import bcrypt

def hash_password(password, algorithm):
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'bcrypt':
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def dictionary_attack_crack(password_hash, algorithm, dictionary_path):
    with open(dictionary_path, 'r') as file:
        for line in file:
            password = line.strip()
            if algorithm == 'bcrypt':
                # Check if the provided hash is bcrypt format
                if bcrypt.checkpw(password.encode(), password_hash.encode()):
                    print(f"Password found: {password}")
                    return
            else:
                if hash_password(password, algorithm) == password_hash:
                    print(f"Password found: {password}")
                    return
    print("Password not found")


