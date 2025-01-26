import re
from collections import Counter

def count_word_occurrences_stream(file_path, top_n=2):
    """
    Counts word occurrences in a text file without loading the entire file into memory
    and returns the most frequently occurring words.

    Args:
        file_path (str): Path to the text file.
        top_n (int): Number of most frequently occurring words to display.

    Returns:
        list[tuple]: A list of tuples containing words and their occurrence counts.
    """
    word_counts = Counter()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Convert to lowercase and clean the line
                line = line.lower()
                line = re.sub(r"[0-9]", " ", line)
                line = re.sub(r"[^\w\s]", " ", line)
                
                # Split the line into words and update counts
                words = re.split(r"\s+", line)
                word_counts.update(word for word in words if word)  # Skip empty strings
        
        # Get the most common words
        most_common_words = word_counts.most_common(top_n)
        return most_common_words

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    file_name = "potop.txt"
    top_words = count_word_occurrences_stream(file_name, top_n=5)
    
    if top_words:
        for word, count in top_words:
            print(f'The word "{word}" occurred {count} times.')
