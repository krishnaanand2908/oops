import random
import string

def encode(word):
    # If the word has less than 3 characters, reverse it
    if len(word) < 3:
        return word[::-1]

    # Remove the first letter and append it at the end
    coded_word = word[1:] + word[0]
    # Append three random characters at the start and end
    coded_word = ''.join(random.choices(string.ascii_letters, k=3)) + coded_word + ''.join(random.choices(string.ascii_letters, k=3))
    return coded_word

def decode(word):
    # If the word has less than 3 characters, reverse it
    if len(word) < 3:
        return word[::-1]

    # Remove the three random characters from the start and end
    decoded_word = word[3:-3]
    # Remove the last letter and append it to the beginning
    decoded_word = decoded_word[-1] + decoded_word[:-1]
    return decoded_word

if __name__ == '__main__':
    while True:
        option = input('Enter 1 to decode or 2 to encode: ')
        if option == '1':
            word = input('Enter the secret code: ')
            if word:
                print(decode(word))
                break
        elif option == '2':
            word = input('Enter the message: ')
            if word:
                print(encode(word))
                break
        else:
            print('Invalid input!')
            continue
