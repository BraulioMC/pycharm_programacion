count = 0
for i in range(1, 100):
    if count == 8:
        print("")
        count = 0
    else:
        print("{:04d}{}".format(i**2, "\t"), end="")
        count += 1
