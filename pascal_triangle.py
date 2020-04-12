pasc = []
coco = []
power =int(input("enter number: "))
for x in range(0, power + 1, 1):
    pasc.append(x)
    coco.append(x)
    pasc[x] = 1
    coco[x] = 1
    p=len(pasc)
    if p >= 2:
        for y in range (1,p-1,1):
            coco[y] = pasc[y]
            if y==1:
                pasc[y] = pasc [y] + pasc [y-1]
            else:
                pasc[y] = coco[y] + coco[y-1]
    print(pasc)
