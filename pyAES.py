from Cryptodome.Cipher import AES
#from Cryptodome.Random import get_random_bytes

nachricht = "Hallo ITO"

key = b'09865rfqghlafgtz78nafg3q'

print("Type of key: ", type(key))

#cipher ist das Verschlüsselungsverfahren
#MODE_EAX ist das Kryptographieverfahren, das AES hier verwendet.
#Es beinhaltet die Verschlüsselung (Vertraulichkeit) und einen Hashwert (Authentizität)
cipher = AES.new(key, AES.MODE_EAX)

#Der String wird in Byte codiert. Bei einer eingelesenen Datei ist das nicht notwendig.
data = str.encode(nachricht)
print("type of data", type(data))

#chiperText beinhaltet den verschlüsselten Text (Bytes)
#messageDigest beinhaltet den Hash, des unverschlüsseltet Textes. Den können wir später für die Integrität verwenden.
ciphertext, messageDigest = cipher.encrypt_and_digest(data)

print("Verschlüsselte Daten: ", ciphertext, type(ciphertext), len(ciphertext))
print("Hashwert: ", messageDigest, type(messageDigest), len(messageDigest))

#Decrypt
nonce = cipher.nonce
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

print(plaintext)
