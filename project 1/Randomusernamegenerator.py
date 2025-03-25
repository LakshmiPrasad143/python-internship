import random

# Lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Brave", "Silent", "Swift", "Funny", "Bright", "Wild"]
nouns = ["Tiger", "Dragon", "Wolf", "Eagle", "Fox", "Bear", "Hawk", "Panther"]

# Special characters and numbers for customization
special_chars = ["!", "@", "#", "$", "%"]
numbers = [str(i) for i in range(10)]  # ['0', '1', '2', ..., '9']

def generate_username(use_numbers=False, use_special=False):
    # Pick a random adjective and noun
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Base username
    username = adj + noun
    
    # Add numbers if requested
    if use_numbers:
        username += random.choice(numbers) + random.choice(numbers)  # Adds two random digits
    
    # Add special character if requested
    if use_special:
        username += random.choice(special_chars)
    
    return username

def save_to_file(username):
    with open("usernames.txt", "a") as file:  # 'a' mode appends to the file
        file.write(username + "\n")
    print(f"Saved '{username}' to usernames.txt")

def main():
    print("Welcome to the Random Username Generator!")
    
    while True:
        # Get user preferences
        print("\nOptions:")
        print("1. Generate a simple username (e.g., CoolTiger)")
        print("2. Add numbers (e.g., CoolTiger12)")
        print("3. Add special characters (e.g., CoolTiger!)")
        print("4. Add both numbers and special characters (e.g., CoolTiger12!)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        # Handle user input and generate username
        try:
            choice = int(choice)
            if choice == 5:
                print("Goodbye!")
                break
            elif choice in [1, 2, 3, 4]:
                use_numbers = choice in [2, 4]
                use_special = choice in [3, 4]
                username = generate_username(use_numbers, use_special)
                print(f"Generated Username: {username}")
                
                # Ask to save
                save_choice = input("Would you like to save this username? (y/n): ").lower()
                if save_choice == 'y':
                    save_to_file(username)
            else:
                print("Invalid choice! Please select between 1 and 5.")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
