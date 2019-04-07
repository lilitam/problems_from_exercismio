def raindrops(number):
    factor_dict = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    result = []
    for i in factor_dict.keys():
        if number % i == 0 and i in factor_dict:
            result.append(factor_dict[i])
    if result:
        return "".join(result)
    else:
        return str(number)
