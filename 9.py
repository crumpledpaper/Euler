for a in range(1,1000):
    for b in range(a,1000-a):
        c = (a**2 + b**2) ** 0.5
        if c % 1 == 0:
            if a + b + c == 1000:
                print(a*b*c)
