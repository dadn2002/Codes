
for i in range(255):
    with open("teste" + ".txt", "a", encoding='utf-8') as f1:
        f1.write(chr(i))
