# Algoric-Shift

## Description

50 points

Ciphered text : HESL{LRAT5PN51010T\_CNPH1R}3

Try decrypting: [script.py](script.py)

---

## Solution

The challenge provides the source code for the encryption program.  
Reading [script.py](script.py) we can see what is happening.

```python
text = 'flag{...}'

key = [3,1,2]

li0 = []
li1 = []
li2 = []
for i in range(0,len(text)):
    if i % 3 == 0:
        li0.append(text[i])
    elif (i - 1) % 3 == 0:
        li1.append(text[i])
    elif (i - 2) % 3 == 0:
        li2.append(text[i])
li = []
for i in range(len(li1)): 
    li.append(li1[i]) 
    li.append(li2[i])
    li.append(li0[i])

# print(li)
print("The ciphered text is :")
ciphered_txt = (''.join(li))
print(ciphered_txt)

```

From reading the source code we can see that it iterates over each character in the flag and splits the characters into 3 different lists.

It them loops over the lists and reassemble the flag in order of list 3, list 2, list 1.

So a flag of `THE` would be encrypted as `HET`
A flag of `ANSWER` would be encrypted as `NSAERW`.

To decrypt the flag we first break it into groups of 3.

`HES L{L RAT 5PN 510 10T _CN PH1 R}3`

The 3rd letter in each grouping needs to be moved to the front of that group  
`HES -> SHE`  
`L{L -> LL{`  

Doing this for each grouping will get us  
`SHE LL{ TRA N5P 051 T10 N_C 1PH 3R}`  

Combining them back together will give the flag.  
Flag: `SHELL{TRAN5P051T10N_C1PH3R}`