import re

def word_filter_counter(text, filter_words):
    # Convert the filter words to lowercase for case-insensitive comparison
    filter_words_lower = [word.lower() for word in filter_words]

    # Remove punctuation and split the text into words
    words = re.findall(r'\b\w+\b', text)

    # Initialize a dictionary to store word counts
    word_counts = {}

    # Count occurrences of filtered words
    for word in words:
        word_lower = word.lower()
        if word_lower in filter_words_lower:
            # Increment the count for the filtered word
            word_counts[word_lower] = word_counts.get(word_lower, 0) + 1

    return word_counts

# Test cases
print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  # Expected output: {'hello': 2}
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}
