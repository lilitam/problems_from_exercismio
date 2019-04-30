def slices(series, length):
    if length <= 0 or len(series) == 0 or len(series) < length:
        raise ValueError("Invalid input!")
    list = []
    for i in range(len(series)-length+1):
        list.append(series[i: i+length])
    return list

