# exercise 4.19

# F to C
def calc_celsiusf(fahrenheit):
    c_from_f = (fahrenheit - 32) * 5/9
    return c_from_f


# K to C
def calc_celsiusk(kelvin):
    c_from_k = kelvin -273
    return c_from_k


# C to F
def calc_fahrenheitc(celsius):
    f_from_c = (9/5 * celsius) + 32
    return f_from_c


# K to F
def calc_fahrenheitk(kelvin):
    f_from_k = ((kelvin - 273)* 9/5) + 32
    return f_from_k


# C to K
def calc_kelvinc(celsius):
    k_from_c = celsius + 273
    return k_from_c


# F to K
def calc_kelvinf(fahrenheit):
    k_from_f = ((fahrenheit - 32) * 5/9) + 273
    return k_from_f


def calc_temperatures(temp_unit, given_temp):
    if temp_unit == 'kelvin':
        temp_for_k_to_c = calc_celsiusk(given_temp)
        temp_for_k_to_f = calc_fahrenheitk(given_temp)
        return temp_for_k_to_f, temp_for_k_to_c

    elif temp_unit == 'celsius':
        temp_for_c_to_f = calc_fahrenheitc(given_temp)
        temp_for_c_to_k = calc_kelvinc(given_temp)
        return temp_for_c_to_f, temp_for_c_to_k

    elif temp_unit == 'fahrenheit':
        temp_for_f_to_c = calc_celsiusf(given_temp)
        temp_for_f_to_k = calc_kelvinf(given_temp)
        return temp_for_f_to_k, temp_for_f_to_c

    return calc_temperatures


# e
def test_conversion():
    f = 32
    c = 0

    f_test = calc_fahrenheitc(calc_celsiusf(f))
    c_test = calc_celsiusf(calc_fahrenheitc(c))

    assert ((f_test == f) and (c_test == c))


if __name__ == '__main__':
    print(calc_temperatures('kelvin', 273))  # output 0 and 32
    print(calc_temperatures('celsius', 0))  # output 273 and 32
    print(calc_temperatures('fahrenheit', 32))  # output 273 and 0

