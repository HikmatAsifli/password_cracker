
# Password Cracker

A lightweight, modular password cracking tool written in Python. Designed for educational purposes and authorized penetration testing only.
## Features

- Supports multiple attack modes:
    - Dictionary/wordlist attack
    - Brute-force (customizable character sets & lengths)
    - Rule-based mutations (planned)
- Hash support:
    - MD5, SHA1, SHA256, NTLM, and more (via hashlib and passlib)
- Multi-threaded for improved performance
- Clean CLI interface with progress tracking
- Easily extensible architecture
## Installation

```bash
git clone https://github.com/HikmatAsifli/password_cracker.git
cd password_cracker
pip install -r requirements.txt
```
## Usage

- **Dictionary Attack**
```bash
python src/cracker.py -m dictionary -p "<your_bcrypt_hash>" -a bcrypt -d wordlists/common_passwords.txt
```
- **Brute-force Attack**
```bash
python src/cracker.py -m brute -p "<your_bcrypt_hash>" -a "<your_algorithm>
```
- **Help**
```bash
python src/cracker.py -h
```
## Requirements

- Python 3.8+
- `hashlib`, `argparse`, `concurrent.futures` (standard library)
- Optional: `passlib` (for NTLM, etc.)

See `requirements.txt` for details.


## Disclaimer
This tool is intended only for security testing on systems you own or have explicit permission to test. Unauthorized use is illegal and unethical.
## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
