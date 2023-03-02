# exercise 4.3
from f2c_qa import celsius
data_array = open('Temp_Data', 'r')     # opens Temp_Data, 'r' reads the file
data_contents = data_array.readlines()  # specifies to read each line in the file
data_array.close()  # close it so we don't accidentally change anything in Temp_Data

f_value = float(data_contents[2].split()[2]) # grabs the float from the third line and third space

print(f'{celsius(f_value)}')  # calls the celsius function from f2c_qa and prints the value corresponding to f_value
