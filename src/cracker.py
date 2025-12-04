import argparse
from brute_force import brute_force_crack
from dictionary_attack import dictionary_attack_crack

def main():
    parser = argparse.ArgumentParser(description="Password Cracker using brute-force or dictionary attack")
    parser.add_argument('-m', '--method', choices=['brute', 'dictionary'], required=True, help="Method to use: brute-force or dictionary")
    parser.add_argument('-p', '--password_hash', required=True, help="The hashed password to crack")
    parser.add_argument('-a', '--algorithm', choices=['md5', 'sha1', 'bcrypt'], required=True, help="Hash algorithm used")
    parser.add_argument('-d', '--dictionary', help="Path to the dictionary file for dictionary attack")

    args = parser.parse_args()

    # Check that the bcrypt hash is valid (starts with $2)
    if args.algorithm == 'bcrypt' and not args.password_hash.startswith("$2"):
        print("Invalid bcrypt hash format. Make sure it starts with $2.")
        return

    if args.method == 'brute':
        brute_force_crack(args.password_hash, args.algorithm)
    elif args.method == 'dictionary':
        if args.dictionary is None:
            print("Please provide a dictionary file for dictionary attack")
        else:
            dictionary_attack_crack(args.password_hash, args.algorithm, args.dictionary)

if __name__ == "__main__":
    main()


