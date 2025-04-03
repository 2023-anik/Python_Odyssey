# # main.py

# # import mypackage.module1 #1
# # import mypackage.module2 #1
# # from mypackage import module1 as m1, module2 as m2 #2
# from mypackage.module1 import greet as g #3
# from mypackage.module2 import depart as d #3

# # mypackage.module1.greet("Pythonista") #1
# # mypackage.module2.depart("Pythonista") #1

# # m1.greet("Pythonista") #2
# # m2.depart("Pythonista") #2

# g("Pythonista") #3
# d("Pythonista") #3


from mypackage.module1 import greet
from mypackage.mysubpackage.module3 import people

for person in people:
    greet(person)