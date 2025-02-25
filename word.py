import re

def count_words(text):
    """Counts words in the given text."""
    words = re.findall(r'\b\w+\b', text)  # Using regex to capture words properly
    return len(words)

def count_characters(text):
    """Counts characters excluding spaces."""
    return len(text.replace(" ", ""))

def count_sentences(text):
    """Counts sentences by splitting at '.', '!', or '?'."""
    sentences = re.split(r'[.!?]', text)
    return len([s for s in sentences if s.strip()])  # Removing empty parts

def count_paragraphs(text):
    """Counts paragraphs based on double line breaks."""
    paragraphs = text.strip().split("\n\n")  # Splitting by double newlines
    return len([p for p in paragraphs if p.strip()])  # Removing empty paragraphs

def display_statistics(text):
    """Displays text analysis summary."""
    print("\n--- Text Analysis Summary ---")
    print(f"Total Words: {count_words(text)}")
    print(f"Total Characters (excluding spaces): {count_characters(text)}")
    print(f"Total Sentences: {count_sentences(text)}")
    print(f"Total Paragraphs: {count_paragraphs(text)}")
    print("-----------------------------")

def main():
    """Main function to handle user input and display output."""
    print("🔹 Welcome to the Advanced Word Counter 🔹")

    # Taking multi-line user input
    print("\nEnter your text (Press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines).strip()  # Joining input lines into a single string

    # Error handling for empty input
    if not text:
        print("\n❌ Error: No text entered. Please enter valid text.")
        return

    # Displaying text analysis results
    display_statistics(text)

if __name__ == "__main__":
    main()
