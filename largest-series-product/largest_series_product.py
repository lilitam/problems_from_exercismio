def largest_product(series, size):
    if size < 0 or len(series) < size:
        raise ValueError("Invalid input!")
    if size == 0:
        return 1
    list=[]
    max = 0
    for i in range(len(series) - size + 1):
        list.append(series[i:i+size])
        product = 1
        for i in series[i:i+size]:
            product = product * int(i)
        if product > max:
            max = product
    return max