size = int(input("Enter the size of the list :"))
lst = []
for i in range(size):
    lst.append(int(input("Enter the number :")))
print(lst)
res = map(lambda number:number * number,lst)
print(list(res))