# attributes -> variable
# behaviour -> methods(fun)

class computer:
    def config(self):
        print("i4, 4gb, 50mp")

comp1 = computer()
comp2 = computer()
# print(type(comp1))
computer.config(comp2)
comp1.config()