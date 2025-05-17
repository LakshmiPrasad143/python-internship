import random
import tkinter as tk
from PIL import Image, ImageTk
import os

# Function to simulate a single coin toss
def coin_toss():
    return random.choice(["Heads", "Tails"])

# Function to simulate multiple tosses
def simulate_tosses(num_tosses):
    heads_count = 0
    tails_count = 0
    results = []

    for _ in range(num_tosses):
        result = coin_toss()
        results.append(result)
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count, results

# Function to display results
def display_results(heads, tails, total):
    print(f"\nResults of {total} coin tosses:")
    print(f"Heads: {heads} ({(heads / total) * 100:.2f}%)")
    print(f"Tails: {tails} ({(tails / total) * 100:.2f}%)")

# Bonus: Show image of the final coin toss result
def show_coin_image(result):
    window = tk.Tk()
    window.title("Final Coin Toss Result")

    # Image files required: heads.png and tails.png in the same folder
    image_file = "heads.png" if result == "Heads" else "tails.png"

    if not os.path.exists(image_file):
        print(f"Image file '{image_file}' not found. Skipping graphical display.")
        return

    img = Image.open(image_file)
    img = img.resize((200, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(window, image=photo)
    label.pack()

    tk.Label(window, text=f"The final toss was: {result}", font=("Arial", 14)).pack()

    window.mainloop()

# Main function
def main():
    print("🎲 Welcome to the Virtual Coin Toss Simulator! 🎲\n")
    
    while True:
        try:
            num = int(input("Enter the number of coin tosses: "))
            if num <= 0:
                print("Please enter a positive number.")
                continue

            heads, tails, all_results = simulate_tosses(num)
            display_results(heads, tails, num)

            # Bonus: Show the image of the final result
            show_graphic = input("Do you want to see the last coin toss result as an image? (y/n): ").strip().lower()
            if show_graphic == 'y':
                show_coin_image(all_results[-1])

            again = input("\nDo you want to toss again? (y/n): ").strip().lower()
            if again != 'y':
                print("Thank you for using the Virtual Coin Toss Simulator. Goodbye!")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

# Entry point
if __name__ == "__main__":
    main()
