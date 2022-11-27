class Phone:

    def __init__(self, a, b, c, d):
        self.name = a
        self.manufacturer = b
        self.memory = str(c)
        self.price = str(d)


box = list()

box.append(Phone("Apple Iphone 7", "China", 64, 799))
box.append(Phone("Huawey 3G Pro", "Taiwan", 128, 249))
box.append(Phone("Xiaomi Pro Max Plus Energy", "China", 256, 325))
box.append(Phone("Apple Iphone X", "USA", 128, 1299))
box.append(Phone("Apple Iphone 13 Pro", "USA", 256, 1599))
box.append(Phone("Sony Ericson", "China", 128, 799))
f = open('123.txt', 'w')
box.sort(key=lambda x: x.name, reverse=False)

for i in box:
    print(i.name, i.manufacturer, i.memory, i.price, sep=' ')
    f.write(i.name)
    f.write(' ')
    f.write(i.manufacturer)
    f.write(' ')
    f.write(i.memory)
    f.write(' ')
    f.write(i.price)
    f.write('\n')
f.close()

