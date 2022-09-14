def test(a):
    a[0] += 2
    print(a)

b = [5]
print(b)
test(b)
print(b)