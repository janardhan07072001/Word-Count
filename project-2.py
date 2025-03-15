def count_words(text):
    """
    Function to count the number of words in a given text.
    """
    # Split the text into words based on spaces and return the count
    words = text.split()
    return len(words)

def main():
    """
    Main function to handle user input and display the word count.
    """
    print("Welcome to the Word Counter Program!")
    
    # Prompt the user for input
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: You must enter some text to count words.")
        return
    
    # Call the function and display the result
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")

# Run the program
if __name__ == "__main__":
    main()
