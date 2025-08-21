#task1
Reqem = int(input("Eded daxil edin: "))
i = 0
while i < Reqem:
    print("*", end="")
    i = i + 1

#task2
eded = int(input("Eded daxil et: "))
faktorial = 1
i = 1
while i <= eded:
    faktorial = faktorial * i
    i = i + 1
print(faktorial)
#task3
eded1 = int(input("Esas eded: "))
eded2 = int(input("Ust: "))
i = 1
cavab = 1
while i <= eded2:
    cavab = cavab * eded1
    i = i + 1
print(cavab)
#task4-

#task5
eded = int(input("Eded daxil et: "))
i = 1
while i <= eded:
    if eded % i == 0:
        print(i)
    i = i + 1


