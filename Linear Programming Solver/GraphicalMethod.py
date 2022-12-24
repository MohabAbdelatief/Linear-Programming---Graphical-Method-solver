
import matplotlib.pyplot as plt
import numpy as np
# BEGINNING OF CLASSES


class ObjectiveFunction:
    value1 = 0
    value2 = 0

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def display(self):
        print("Z = " + str(self.value1) + "x1 + " + str(self.value2) + "x2")


class Constraint:
    value1 = 0
    value2 = 0
    sign = ''
    value3 = 0
    # FOR PLOTTING AND FEASIBLE REGION
  

    def __init__(self, value1, value2, value3, sign):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.sign = sign

    def display(self):
        print(str(self.value1) + "x1 + " + str(self.value2) +
              "x2 " + self.sign + " " + str(self.value3))

    def Solve(self):
    # 2x + 1y = 100
    # SOLVE FOR Y
        x = int(self.value3)
        y = int(self.value2)
        z = int(self.value1)
        # FIRST POINT
        tempX = z * 0
        tempY = x / y

        point1 = [] 

        point1.append(tempX)
        point1.append(tempY)
        # SOLVE FOR X
        # SECOND POINT
        tempY = y * 0
        tempX = x / z

        point2 = []

        point2.append(tempX)
        point2.append(tempY)

        print("POINTS")
        print("------")
        print("(" + str(point1[0]) + " , " + str(point1[1]) + ")")
        print("(" + str(point2[0]) + " , " + str(point2[1]) + ")")

        x = [point1[0], point2[0]]
        y = [point1[1], point2[1]]
  

        plt.plot(x, y)
      
# DISPLAY
def DisplayNonNegativeConstraints():
    print("------------------------")
    print("Non-Negative Constraints")
    print("------------------------")
    print("x1 >= 0")
    print("x2 >= 0")

def DisplayAll():
    print("")

    # PRINT OBJECTIVE
    print("OBJECTIVE FUNCTION")
    print("------------------")
    Objective_Function.display()

    print("")

    print("CONSTRAINTS: ")
    print("------------------")
    # PRINT CONSTRAINTS
    for obj in Constraints:
        print(" ")
        obj.display()
        print(" ")
    DisplayNonNegativeConstraints()

def DrawFeasibleReigon():
    if constraint.sign == "<=":
        # Shade under the line
        x = [0, 0, 20, 50]
        y = [0, 80, 60, 0] 
    plt.fill(x, y, 'lightgrey')
# END OF CLASSES
# ---------------------------------------

# MAIN

# ---------------------------------------
# Enter your objective function
value1 = input("Enter Value 1 for objective function: ")
value2 = input("Enter Value 2 for objective function: ")
Objective_Function = ObjectiveFunction(value1, value2)
# Enter Your constraints
# NUMBER OF DESIERD CONSTRAINTS
numberOfConstraints = input("Enter number of constraints: ")
X = int(numberOfConstraints)
index = 0  # ITERATOR
Constraints = []  # ARRAY OF CONSTRAINTS
# INPUT LOOP
while (index < X):
    valueX = input("Enter value of X1: ")  # valueX X1 +
    valueY = input("Enter value of X2: ")  # + valueY X2
    Sign = input("Enter your compare sign: ")  # sign
    ValueZ = input("Enter value after the compare signs: ")  # sign ValueZ
    constraint = Constraint(valueX, valueY, ValueZ, Sign)
    Constraints.append(constraint)
    index = index + 1  # INDEX INCREASES BY 1
# END OF INPUT LOOP

# -------------------------------------

DisplayAll()
for obj in Constraints:
    obj.Solve()

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# HARD CODED
# FEASIBLE REIGON
drawIT = input("Do you want to draw feasible region? [Y/N]")
if drawIT == 'Y' or drawIT == 'y':
    DrawFeasibleReigon()
else:
    print("Drawing without feasible region shading")
    
# END OF HARD CODED
plt.show()