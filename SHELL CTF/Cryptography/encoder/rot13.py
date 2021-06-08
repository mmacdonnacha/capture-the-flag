cipher = 'ZOLSS{W1G_D3HY_4_T45R}'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(alphabet)):
    plaintext = ''
    for x in cipher:
        if x.isalpha():
            index = alphabet.find(x)
            new_index = (index + i + 1) % 26
            plaintext = plaintext + alphabet[new_index]
        else:
            plaintext = plaintext + x
    
    if 'SHELL{' in plaintext:
        print(plaintext)