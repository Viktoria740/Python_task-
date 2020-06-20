sent = list(input("введите ").split(" "))
for ind, el in enumerate(sent, 1):
    print(ind, el[:10])