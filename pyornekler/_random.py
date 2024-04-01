import random

# result = dir(random)
# result = help(random)

result = random.random() * 100 #0 ile 100 arasında rasgele sayı motdu
result = int(random.uniform(10, 100)) #tam rasgele sayı metodu
result = random.randint(1, 100) #tam rasgele sayı metodu


#liste ve stringlerede random
greeting = 'hello there'
names = ['ali', 'yağmur', 'deniz', 'cenk', 'ahmet', 'efe']
# result = names[random.randint(0, len(names) - 1)]
result = random.choices(names)
result = random.choices(greeting)

liste = list(range(10))
random.shuffle(liste) #listeyi karıştırma
result = liste

liste = range(100)
result = random.sample(liste,3) #0 ile 100 arasında 3 adet rastgele sayı
result = random.sample(names,2)
print(result)
