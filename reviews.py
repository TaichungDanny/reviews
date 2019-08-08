#import random
data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))

wc = {}
for d in data:
    words = d.strip().split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 1000:
        print(word, wc[word])
while True:
    c = input('請輸入關鍵字:')
    if c not in wc:
        print('未找到關鍵字')
    else c == 'q':
        print('感謝使用')
        break
    print(c, '出現的次數', wc[c])


#r = random.randint(1, 1000000)
#print(data[r])
#sum = 0
#for i in data:
    #sum += len(i)
#average = sum / count
#print(average)
#for i in data:
    #if len(i) < 100:
        #print(i)
        #print("----------")