#Zadacha №1

array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(2,100):
    for j in range(2,10):
        if (i % j == 0):
            array[j] += 1
print(array[2:10])
