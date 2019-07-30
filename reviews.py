import random
data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
r = random.randint(1, 1000000)
print(data[r])
sum = 0
for i in data:
    sum += len(i)
average = sum / count
print(average)
for i in data:
    if len(i) < 100:
        print(i)
        print("----------")