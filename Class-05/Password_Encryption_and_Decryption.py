def encrypt(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

# shift=-3
def decrypt(text,shift):

  return encrypt(text,shift)


message = input("Enter message: ")
shift = 3

encrypted = encrypt(message,shift)
print("Encrypted Text:", encrypted)

decrypted = decrypt(encrypted,shift)
print("Decrypted Text:", decrypted)
