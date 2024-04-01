with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(11)
    print(content)
    file.seek(0)
    print(file.tell())
    content2 = file.read(11)
    print(content2)
