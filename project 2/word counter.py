def count_words(text):
    """Function to count the number of words in the given text."""
    words = text.split()
    return len(words)

def main():
    """Main function to handle user input and display word count."""
    while True:
        user_input = input("Enter a sentence or paragraph (or type 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        if not user_input:
            print("Error: Input cannot be empty. Please enter some text.")
            continue
        
        word_count = count_words(user_input)
        print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
