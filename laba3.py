a=list(map(int,input('Введите массив:').split()))
min = float('inf')
for i in range (len(a)):
   if a[i]>0 and a[i]<min:
       min=a[i]
       n=i
if min==float('inf'):
    print("В списке нет положительных чисел")
else:
    print("Минимальный положительный элемент списка:", min)
