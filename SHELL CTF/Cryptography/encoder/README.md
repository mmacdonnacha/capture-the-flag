# encoder

## Description

50 Points

Can you decrypt this text : "ZOLSS{W1G\_D3HY\_4\_T45R}"

NOTE: do not shift the numbers and the special charecters( '{' , '}' , '\_' ).

---

## Solution

The clue for this challenge is the `shift` word. Shifting characters by a specific amount is a [rotation cipher](https://en.wikipedia.org/wiki/ROT13).

In a rotation or ROT cipher every letter in the cipher text is moved forward by a defined amount.  
ROT13 means `a` moves forward 13 places and becomes `n`.  
ROT8 means `a` moves forward 8 places and becomes `i`.


I wrote a script in python to generate all possible plaintexts for the given cipher text. 

```python
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
```

After generating all possible plaintexts (26 letters in alphabet so 26 plaintexts) I check if any contain the string `SHELL{`.  

All flags for the ctf start with `SHELL{` so this helps narrow down the possible plaintexts to one.


Flag: `SHELL{P1Z_W3AR_4_M45K}`