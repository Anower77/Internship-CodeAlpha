def fibo():
    a=0
    b=1
    while True:
        yield a
        a,b = b, a+b

for f in fibo():
    if f>100:
        break
    print(f, end=' ')