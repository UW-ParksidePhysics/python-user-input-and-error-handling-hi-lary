# exercise 4.3
from f2c_qa import celsius
data_array = open('Temp_Data', 'r')
data_contents = data_array.readlines()
data_array.close()

f_value = float(data_contents[2].split()[2])

print(f'{celsius(f_value)}')
