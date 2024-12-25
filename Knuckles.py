print("Please enter the IQ of the people who tried to kill sonic the hedgehog to get the percentage of how smart they are altogether: ")
s = int(input("Sage: "))
c = int(input("Chaos: "))
d = int(input("Dr.Robotnik/Eggman: "))
k = int(input("Knuckles: "))
sh = int(input("Shadow: "))
sum = s+c+d+k+sh
print(sum)
p = (sum/400)*100
print(p)