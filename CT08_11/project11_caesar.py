# shift a single character

def shift_character(char, key, mode):
    if mode == "encryption":
        shift = (((ord(char) + key) - 32) % 95) + 32
    elif mode == "decryption":
        shift = (((ord(char) - key) - 32) % 95) + 32
    else:
        print("type something")
        shift = 32
    return chr(shift)

# char = input("input a character: ")
# key = int(input("what is the key: "))
# mode = input("what mode (encryption / decryption): ").lower()
# shift = shift_character(char, key, mode)
# print(shift)

# shift a sentence

def shift_sentence(sentence, key, mode):
    sentence1 = ""
    for letter in sentence:
        if mode == "encryption":
            shift = (((ord(letter) + key) - 32) % 95) + 32
            sentence1 += chr(shift)

        elif mode == "decryption":
            shift = (((ord(letter) - key) - 32) % 95) + 32
            sentence1 += chr(shift)
        else:
            print("type something")
            break
    return sentence1


# sentence = input("input a sentence: ")
# key = int(input("what is the key: "))
# mode = input("what mode (encryption / decryption): ").lower()
# shift = shift_sentence(sentence, key, mode)
# print(shift)

# shift a list of sentences

def shift_list(list, key, mode):
    sentence = ""
    list = []
    if not(mode == "encryption" or mode == "decryption"):
        print("type something")
        return sentence
    
    for item in list:
        print(item) 
        for letter in item:
            if mode == "encryption":
                shift = (((ord(letter) + key) - 32) % 95) + 32
                sentence += chr(shift)
            else:
                shift = (((ord(letter) - key) - 32) % 95) + 32
                sentence += chr(shift)
        list.append(sentence)
    return list

list = []
confirmation = ""
while confirmation != "end":
    confirmation = input("add a sentence to the list: ")
    if confirmation == "end":
        break
    else:
        list.append(confirmation)
key = input("key: ")
mode = input("mode: ").lower()
shift = shift_list(list, key, mode)
print(shift)