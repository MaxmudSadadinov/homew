with open('data_x.txt', 'r', encoding='utf-8') as d: 
    sata = input('11111')
    lst = []
    data = d.readlines()
    data_strip = [line.strip() for line in data]
    for i in range(len(data)):
        if data[i] == '\n':
            plus = data[i-1] + data[i]
            if sata  not in plus:
                lst.append(plus)
    print(lst)
            