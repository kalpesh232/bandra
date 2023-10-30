f = open('MyData1.txt','r')
# print('1 : ', f)
# print('2 : ',f.read())
# print('3 : ',f.readline(1))
# print('4 : ',f.readline(2))
# print('5 : ',f.readlines(3))
# f.close()

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.readline(),end="")
# print(f.readline(),end="")

# print(f.readlines())

ls = ['python', 'linux', 'javascript' ]

f1 = open('myData1.txt','w')
f1.write(ls)
print('file created')
# f1.close()

f1 = open('myData.txt','w')
f1.writelines(ls)
print('file created')
f1.close()

# f1 = open('MyData1.txt','a')
# f1.write('hello'+'\n')

# for data in f:
#     f1.write(data)

# f3 = open('file.jpeg','rb')
# print(f3.read())

# f4 = open('file1.jpeg','wb')
# for i in f3:
#     f4.write(i)

#  write read writelines readlines append
