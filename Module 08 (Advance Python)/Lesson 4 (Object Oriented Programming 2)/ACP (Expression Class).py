class Addition:
    def __init__(self,x,y,z):
        self.num1=x
        self.num2=y
        self.num3=z

    def result(self):
        self.num=self.num1+self.num2+self.num3
        print('Output:',self.num)

x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))
z = int(input("Enter 3rd Number: "))
Sum = Addition(x,y,z)

Sum.result()