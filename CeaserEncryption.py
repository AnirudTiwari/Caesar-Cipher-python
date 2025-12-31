def key_enter():
    while True:
        try:
            key = int(input("Enter key (Intiger only) : "))
            break
        except:
            print("Not an Intiger")
    return key

def choice():
    running = True
    msg = enorde = ""
    key = 0
    while True:
        enorde = input("Do you want to Encrypt(e) or Decrypt(d) the message (q to quit) ? : ")
        if enorde.lower() == "e":
            msg = input("Message to be Encrypted: ")
            key = key_enter()
            break
        elif enorde.lower() == "d":
            msg = input("Message to be Dencrypted: ")
            key = -key_enter()
            break
        elif enorde.lower() == "q":
            running = False
            break
        else:
            print("Enter a valid choice")
    return key, running, msg, enorde

while True:
    key, running, msg, enorde = choice()
    if not running:
        print("Bye!")
        break
    else:
        oasciis = [ord(char) for char in msg]
        nasciis = [((oascii-32+key)%95)+32 for oascii in oasciis]
        encrypted =  ''.join(chr(nascii) for nascii in nasciis)

        print(f"Encrypted message: ***{encrypted}***") if enorde.lower() == "e" else print(f"Decrypted message: ***{encrypted}***")