# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# ****************Sayfa sonunda güncelleme*******************
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nEmel Turan")

# ****************Sayfa başında güncelleme*******************
# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "efe turan\n" + content
#     file.seek(0)
#     print(content)


# ****************Sayfa ortasında güncelleme*******************

with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Yılmaz Aygün\n")
    file.seek(0)
    file.writelines(list)
with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())



