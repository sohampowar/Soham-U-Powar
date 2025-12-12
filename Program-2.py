a = int(input("Enter a: "))

series = []
num = 1

for _ in range(a):
    series.append(num)
    num += 2

print(series)
