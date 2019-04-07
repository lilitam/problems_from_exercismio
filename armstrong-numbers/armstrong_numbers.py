def is_armstrong(number):
    number_len = len(str(number))
    power_result = 0
    for i in str(number):
        power_result += int(i)**number_len

    if power_result == number:
        return True
    else:
        return False

