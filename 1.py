s = 0
for i in range(0,1000,3):
    s += i # add multiples of 3
for i in range(0,1000,5):
    s += i #add multiples of 5
for i in range(0,1000,15):
    s -= i #remove double counting

print(s)
