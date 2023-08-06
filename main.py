morse_codes = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": " ",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "/": "-..-.",
    "@": "....-.",
    "sos": "....---...",
}
user_input = input('What sentence, word or letter do you want to change to morse code?\n').lower()

codes = []
answer = ""
for letter in user_input:
    if letter in morse_codes:
        new = morse_codes[letter]
        answer = answer + new
        codes.append(new)
    else:
        answer = answer + " "
        codes.append(' ')

print(answer)
reverse = input('Do you want to change it back to words? Y or N? ').upper()

changed = ''
if reverse == 'Y':
    for code in codes:
        if code == ' ':
            changed = changed + ' '
        else:
            items = morse_codes.items()
            for key, value in items:
                if code == value:
                    new = key
                    changed = changed + new

    print(changed.capitalize())

else:
    print('Have a good day!')
