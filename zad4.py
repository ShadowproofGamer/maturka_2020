plik = open("pary.txt")
dane = plik.read().split()
slowa = []
cyfry = []
for i in dane[1::2]:
    slowa.append(i)
for i in dane[0::2]:
    cyfry.append(int(i))
liczby_pierwsze = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print("4.1:")
for i in cyfry:
    goldman = []
    temp=i
    if i%2==0:
        for j in liczby_pierwsze[-1:0:-1]:
            if j<=temp and j!=(temp-1):
               temp-=j
               goldman.append(j)
            if j<=temp and j!=(temp-1):
               temp-=j
               goldman.append(j)
    goldman.sort()
    if len(goldman)>0:
        print(i, goldman[0], goldman[1])

print("4.2:")
for i in slowa:
    temp = i[0]
    temp_ilosc=1
    max = i[0]
    max_ilosc = 1
    for j in i[1::]:
        if j==temp:
            temp_ilosc+=1
        else:
            if temp_ilosc>max_ilosc:
                max_ilosc=temp_ilosc
                max = temp
            temp = j
            temp_ilosc = 1
    print(max*max_ilosc, max_ilosc)

print("4.3:")
para_temp = [cyfry[0], slowa[0]]
for i in range(1,99):
    if cyfry[i] < para_temp[0]:
        para_temp = [cyfry[i], slowa[i]]
    elif cyfry[i]==para_temp[0] and slowa[i]<para_temp[1]:
        para_temp = [cyfry[i], slowa[i]]
print(para_temp)