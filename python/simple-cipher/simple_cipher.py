class Cipher(object):
    def __init__(self, key):
        if key:
            self.key=key
            print("key's here")
        else:
            self.key='aaaaaaaaaaaaaaaa'
            print("No key, setting to 'aaaaaaaaaaaaaaaa'")
        self.alphabet="abcdefghijklmnopqrstuvwxyz"
        self.enc_key=[self.alphabet.index(key[n]) for n in range(len(key))]
        self.encoded=[]
        self.decoded=[]
    def encode(self, text):
        i=0
        indexed_txt=[self.alphabet.index(text[n]) for n in range(len(text))]
        print("Text indices: " + str(indexed_txt))
        print("Key indices: " + str(self.enc_key))
        for n in range(len(text)):
           if indexed_txt[n]+self.enc_key[i] < 26:
               self.encoded.append(self.alphabet[indexed_txt[n]+self.enc_key[i]])
           else:
               self.encoded.append(self.alphabet[(indexed_txt[n]+self.enc_key[i])-26])
           i=i+1
           if i > (len(self.enc_key)-1):
               i=0
        return ''.join(self.encoded)

    def decode(self, text):
        i=0
        indexed_txt=[self.alphabet.index(text[n]) for n in range(len(text))]
        print("Encoded text indices: " + str(indexed_txt))
        for n in range(len(text)):
           if indexed_txt[n]-self.enc_key[i] >= 0:
               self.decoded.append(self.alphabet[indexed_txt[n]-self.enc_key[i]])
           else:
               self.decoded.append(self.alphabet[(indexed_txt[n]-self.enc_key[i])+26])
           i=i+1
           if i > (len(self.enc_key)-1):
               i=0
        return ''.join(self.decoded)

cipher=Cipher("fakjsdfkj")
encoded=cipher.encode("chickcorea")
decoded=cipher.decode(''.join(encoded))
print(encoded)
print(decoded)

