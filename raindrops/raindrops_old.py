import math


def raindrops(number):
    factor_dict = {3:'Pling', 5:'Plang', 7:'Plong'}
    result = []
    # square_root = math.sqrt(number)
    #for i in range(2, int(square_root)+1):
    for i in [3, 5, 7]:
        if number % i == 0 and i in factor_dict:
            #factors.append(number/i)
            result.append(factor_dict[i])
    if result:
        return "".join(result)
    else:
        return str(number)
    
    # if 3 in factors:
    #     result.append('Pling')
    # if 5 in factors:
    #     result.append('Plang')
    # if 7 in factors:
    #     result.append('Plong')
    # if result:
    #     return "".join(result)
    # else:
    #     return str(number)
