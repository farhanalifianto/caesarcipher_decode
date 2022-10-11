alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(plt,sr):
  cytext = ""
  for letter in plt:
    pos = alphabet.index(letter)
    newpos = pos + sr
    newl = alphabet[newpos]
    cytext += newl
  print(cytext)

def decrypt(plt,sr):
  cytext = ""
  for letter in plt:
    pos = alphabet.index(letter)
    newpos = pos - sr
    newl = alphabet[newpos]
    cytext += newl
  print(cytext)


if direction == "encode":
  encrypt(plt=text,sr=shift)
elif direction == "decode":
  decrypt(plt=text,sr=shift)

    
