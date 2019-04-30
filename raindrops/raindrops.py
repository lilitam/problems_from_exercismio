def raindrops(number):
    list_numbers=[3,5,7]
    list_str=['Pling', 'Plang', 'Plong']
    result = [j for i, j in zip(list_numbers, list_str) if number % i == 0]
    if result:
        return "".join(result)
    else:
        return str(number)


