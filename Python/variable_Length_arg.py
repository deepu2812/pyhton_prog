def person(name, **data):
    print(name)
    # print(data)

    for i, j in data.items():
        print(i,j)

person('Dipak',age=22,city="rajkot",mob=987654321)