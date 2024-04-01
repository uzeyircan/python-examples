import os
import datetime

result=os.name
# dizin değiştirme
# os.chdir('C:\\') dizini değiştirir
# os.chdir('../..')

# klasör oluşturma
# os.mkdir("newdirectory") klasör oluşturur (aynı dizin içinden)
# os.makedirs("newdirectort/yeniklasör")

# listeleme
# result= os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


# etkin dizin öğrenme
# result = os.getcwd()

result = os.stat("_date.py")
result = result.st_size/1024

print(result)