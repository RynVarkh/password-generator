'''
    Ask the user for the app name.
    Ask the user for the desired password length.
    Generate a random password of that length.
    Save the app name and generated password in secrets.json.
'''
import json, os, random, string

FILE = "/home/valrik/.secrets.json"

def load_passwd():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_passwd(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_passwd(length):
    safe_punctuation = "!#%()*+,-.:;=?@[]^_{}~/"
    char = string.ascii_letters + string.digits + safe_punctuation
    return "".join(random.choice(char) for _ in range(length))

def main():
    passwords = load_passwd()

    appName = input("App: ")
    length = int(input("Desired password Length: "))

    password = generate_passwd(length)
    print(f"Generated Password for {appName} : {password}")

    passwords.append({"app":appName, "password":password})
    save_passwd(passwords)
    print(f"Saved password to {FILE}")

if __name__ == "__main__":
    main()