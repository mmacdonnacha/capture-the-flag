# Subsi

## Description

50 points

cipher : HITSS{5X65Z1ZXZ10F\_E1LI3J}

Downloadable file : [script.py](script.py)

---

The challenge provides the source code for the encryption program.  
Reading [script.py](script.py) we can see what is happening.

```python
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_1234567890'
key   = 'QWERTPOIUYASDFGLKJHZXCVMNB{}_1234567890'

text = <flag>

def encrypter(text,key):
    encrypted_msg = ''
    for i in text:
        index = alpha.index(i)
        encrypted_msg += key[index]
    # print(encrypted_msg)
    return encrypted_msg
```

From reading the source code we can see that each character in the plaintext is replaced with a character in the key that is at the same index.

`A` has an index of `1` in the alpha and is mapped to the character `Q` which has an index of `1` in the key.  
`M` has an index of `13` in the alpha and is mapped to the character `D` which has an index of `13` in the key.  


Using the linux command `tr` we can decrypt the flag

```
~$ echo <encrypted_flag> | tr <key> <alpha>

~$ echo HITSS{5X65Z1ZXZ10F_E1LI3J} | tr QWERTPOIUYASDFGLKJHZXCVMNB{}_1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_1234567890
```

Flag: `SHELL{5U65T1TUT10N_C1PH3R}`