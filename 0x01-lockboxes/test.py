num = int(input("Enter how many numbers to average: "))
print((sum(float(input("Enter a number: ")) for _ in range(num))) / num)
