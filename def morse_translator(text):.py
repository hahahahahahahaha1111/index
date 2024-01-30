def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Convert the text to uppercase for case-insensitivity
    text = text.upper()

    # List to store translated Morse code for each character
    morse_code_list = []

    for char in text:
        if char.isalpha():
            # Add the Morse code for alphabetic characters
            morse_code_list.append(morse_code_dict[char])
        elif char == " ":
            # Add a forward slash for space between words
            morse_code_list.append("/")
    
    # Join the Morse code list into a single string
    morse_code_str = " ".join(morse_code_list)

    return morse_code_str

# Test cases
print(
    morse_translator("HELLO WORLD")
)  
print(morse_translator("Python"))  
print(
    morse_translator("Morse Code")
)  
