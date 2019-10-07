ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LEN_ALPHA = len(ALPHABET)

def crypt(shift, msg):
  """
  Takes two arguments, an integer, the shift you want to be used to encrypt, and a string, the message to encrypt.
  Return a string which contains the encrypted message.
  """
  shift = shift % LEN_ALPHA
  msg_encrypt = [letter.upper() for letter in msg]
  for i in range(0, len(msg_encrypt)):
    index = ALPHABET.find(msg_encrypt[i])
    if index != -1: # if the character of index i was find in ALPHABET (it means, if the character is a letter)
      msg_encrypt[i] = ALPHABET[(index+shift)%LEN_ALPHA]
  msg_encrypt=[msg_encrypt[i].lower() if msg[i] == msg[i].lower() else msg_encrypt[i] for i in range(0, len(msg))] # each time a letter was lowercase in the original message, put it lowercase in the encrypted message too.
  return ''.join(msg_encrypt)

def decrypt(shift,msg_encrypt):
  """
  Takes two arguments, an integer, the shift which was used to encrypt, and a string, the message to decrypt.
  Return a string which contains the decrypted message.
  """
  shift = shift % LEN_ALPHA
  msg = [letter.upper() for letter in msg_encrypt]
  for i in range(0, len(msg)):
    index = ALPHABET.find(msg[i])
    if index != -1: # if the character of index i was find in ALPHABET (it means, if the character is a letter)
      msg[i] = ALPHABET[(index-shift)%LEN_ALPHA]
  msg = [msg[i].lower() if msg_encrypt[i] == msg_encrypt[i].lower() else msg[i] for i in range(0, len(msg_encrypt))] # each time a letter was lowercase in the original message, put it lowercase in the decrypted message too.
  return ''.join(msg)

def main():
  shift = int(input("Choisissez le decalage : "))
  if int(input("Chiffrer (0) ou dechiffrer (1) ? ")) == 0:
    msg = input("Entrez la phrase a chiffrer : \n==> ")
    msg = crypt(shift,msg)
  else:
    msg = input("Entrez la phrase a dechiffrer : \n==> ")
    msg = decrypt(shift,msg)
  print(msg)

if __name__=="__main__":
  main()
