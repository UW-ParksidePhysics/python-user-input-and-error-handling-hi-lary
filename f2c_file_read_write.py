# exercise 4.4
from f2c_qa import celsius
data_array = open('Temp_Data', 'r')     # opens Temp_Data, 'r' reads the file
data_contents = data_array.readlines()  # specifies to read each line in the file
data_array.close()  # close it so we don't accidentally change anything in Temp_Data
array = range(2, 8)  # so we can go through the desired lines from Data_Temp in the for loop below
f_temp = []  # empty list to put f temperatures in
c_temp = []  # empty list to put c temperatures in

for i in array:
    f_value = float(data_contents[i].split()[2])  # grabs the float from the i-th row and third space
    f_temp.append(f_value)  # not necessary but now I have a list with  f temperatures
    c_value = celsius(f_value)  # calls the celsius function from f2c_qa and prints the value corresponding to f_value
    c_temp.append(c_value)  # not necessary but now I have a list with c temperatures
    print(f'{f_value}, {c_value}')  # prints the f_value and c_value for every float in Temp_Data
