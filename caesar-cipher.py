def caesar(text, shift, direction):
    result = ""

    # Normalize shift
    shift = shift % 26
    if direction == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Shift character using ASCII
            base = ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Keep spaces, numbers, symbols
            result += char

    return result


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ["encode", "decode"]:
        print("Invalid input. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    output = caesar(text, shift, direction)
    print(f"The {direction}d text is: {output}")

    restart = input("Type 'yes' to try again, or 'no' to exit:\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")