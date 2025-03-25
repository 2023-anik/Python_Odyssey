# import adder #1
# import adder as a #2
from adder import add, double #3
from datetime import datetime

# value = adder.add(2, 2) #1
# double_value = adder.double(value) #1

# value = a.add(2, 2) #2
# double_value = a.double(value) #2

value = add(2, 2) #3
double_value = double(value) #3

print(value)
print(double_value)
print(datetime.now())
print(datetime(2020, 2, 2))