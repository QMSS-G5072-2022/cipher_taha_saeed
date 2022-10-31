def cipher(text, shift, encrypt=True):
    
""" 
-describe the function - the funtion encrypts text
-explain its inputs and its output and - the inputs are the text to be encrypted, the number of shifts the funtion should undergo in the alphabet
-provide a short use case example of encrypting and decrypting. - the funtion can be used to hide passwords.

"""


    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
