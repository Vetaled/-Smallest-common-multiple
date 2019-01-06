a,b = map(int,input().split())
d = 2
list_a = []
list_b = []
nok = []
NOK = 1
while a > 1:
    
    if a % d == 0:
        list_a.append(d)
        a = a / d
        
    else:
        d += 1;

d = 2

while b > 1:
    
    if b % d == 0:
        list_b.append(d)
        b = b / d

    else:
        d += 1

for i in range(len(list_a)):

    for j in range(len(list_b)):

        if list_a[i] == list_b[j]:
            nok.append(list_a[i])
            list_b[j] = 1
            list_a[i] = 1

for i in range(len(list_a)):

    if list_a[i] != 1:
        nok.append(list_a[i])

for j in range(len(list_b)):

    if list_b[j] != 1:
        nok.append(list_b[j])

for k in range(len(nok)):
    NOK *= nok[k]
    
print(NOK)

            
