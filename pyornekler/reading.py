# try :
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı.")
#     file.close()

file = open("newfile.txt","r",encoding="utf-8")
# ***************for dögüsü
# for i in file :
#     print(i,end="")

# **************read() fonksiyonu
# content1 = file.read()
# print("içerik 1 ")
# print(content1)
#
# file = open("newfile.txt","r",encoding="utf-8")
#
# content2= file.read()
# print("içerik 2")
# print(content2)

# content=file.read(5)
# content=file.read(3)
#
# print(content)

#*************** readline() fonksiyonu

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())


liste = file.readlines()
print(liste[0],end="")
print(liste[2])



file.close()