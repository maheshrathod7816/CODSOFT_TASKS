import random
import string

print("===== PASSWORD GENERATOR =====")

# Step 1: Get password length
length = int(input("Enter the desired password length: "))

# Step 2: Choose complexity
print("\nChoose password complexity:")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = input("Enter your choice (1/2/3): ")

# Step 3: Create character set
if choice == "1":
    characters = string.ascii_letters

elif choice == "2":
    characters = string.ascii_letters + string.digits

elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation

else:
    print("Invalid choice!")
    exit()

# Step 4: Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Step 5: Display password
print("\nGenerated Password:", password)