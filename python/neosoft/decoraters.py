def div(a,b):
    print('......... :',  a/b)

def smart_div(func):
    def inner(a,b):
        if a < b :
            a,b = b,a
        return func(a,b)
    return inner
divv = smart_div(div)
divv(2,4)
# divv(4,2)