import random
import string
def generate_password():
    try:
        length = int(input("Enter password length: "))
        if length < 4:
            print("Password length should be at least 4!")
            return
        # Character sets
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
        # Combine all characters
        all_chars = letters + digits + symbols
        # Ensure password has at least one of each type
        password = [
            random.choice(letters),
            random.choice(digits),
            random.choice(symbols)
        ]
        # Fill remaining length
        for _ in range(length - 3):
            password.append(random.choice(all_chars))
        # Shuffle password
        random.shuffle(password)
        # Convert list to string
        final_password = "".join(password)
        print("\nGenerated Password:", final_password)
    except ValueError:
        print("Please enter a valid number!")
# Run program
generate_password()