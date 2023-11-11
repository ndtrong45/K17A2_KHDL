import math
a=float(input("Nhập vào a: "))
b=float(input("Nhập vào b: "))
c=float(input("Nhập vào c: "))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích của tam giác =",s)