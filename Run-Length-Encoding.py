fin = open("RLE-Input.txt")
text = fin.read()
fin.close()
print("Input Message is: " + text)

enc = ""
count = 1
for i in range(len(text)-2):
    if(text[i]==text[i+1]):
        count = count + 1
    else:
        enc = enc + str(count) + text[i]
        count = 1

print("Encrypted Message is: " + enc)
fout = open("RLE-Encrypted.txt", "w")
fout.write(enc)
fout.close()

dec = ""
digits = ""
for i in range(len(enc)):
    if(enc[i].isdigit()):
        digits = digits + enc[i]
    else:
        for j in range(int(digits)):
            dec = dec + enc[i]
        digits = ""

print("Decrypted Message is: " + dec)
fout = open("RLE-Decrypted.txt", "w")
fout.write(dec)
fout.close()
