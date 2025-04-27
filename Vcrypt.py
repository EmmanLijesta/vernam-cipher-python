"""
Vernam Cipyher implementation in Python by Engr. Emman Lijesta
Intentionally used class, inheritance and basic code for readbility and
organization. For better security, use at least 64-char hex key.
Vernam Cipher is an unbrekable encryption lest the key is discovered.
"""

# Use ^ or XOR to encrypt in Vernam
class Vernam:
    def __init__(self, key, text):
        self.key = key
        self.text = text

    def convert(self):
        result = []
        count = 0
        length = len(self.key)

        for x in self.text:
            result.append(ord(x) ^ ord(self.key[count % length]))
            count += 1

        return result

# Encode or decode and return as string
class Cipher(Vernam):
    def __init__(self, key, text):
        super().__init__(key, text)

    def encode(self):
        mbyte = self.convert()
        result = ""

        for x in mbyte:
            result += chr(x)

        return result

# Sample key and text
key = "6b8a52cd5a2d8ab3fd6a3b4ad57060136aa49dccd61398ea81a9cbfabde60048"
text = "The quick brown fox jumps over the lazy dog."

# Encoding the text
encoded = Cipher(key, text).encode()
print(encoded)

# Decoding the text
decoded = Cipher(key, encoded).encode()
print(decoded)

"""
Encoded:
b]ADG^APW    NAYYXFSBG^AXX␦CYV
Decoded:
The quick brown fox jumps over the lazy dog.
"""
