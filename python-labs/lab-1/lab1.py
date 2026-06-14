#full_Name = input("Enter your full name: ")
#first_name=full_Name.split()[0]
#last_name=full_Name.split()[1]
#print(last_name + " " + first_name)


#n = input("Enter a value: ")
#res =int(n)+int(n)**2+int(n)**3
#print(res)


"""
print(\
"Sample string :","a string that you \"don't\" have to escape \
This \
is a ....... multi-line \
heredoc string --------> example")
"""
#r=6
#from math import pi
#volume_of_a_sphere = 4/3 * pi * r**3
#print("Volume of a sphere with radius", r, "is", volume_of_a_sphere)

#base = input("Enter the base of triangle ")
#hieght = input("Enter the h of triangle ")
#area= 0.5*int(base)*int(hieght)
#print("Area of triangle is", area)


#for i in range(1, 6):
#    for j in range(i):
#        print("*       |      *", end=" ")
#    print()
#for i in range(4, 0, -1):
#    for j in range(i):
#        print("*       |      *", end=" ")
#    print()


#s=input("Enter a string: ")
#result = ""
#for i in range(len(s)-1,-1,-1):
#    result+=s[i]
#print(result)



#n1=0
#n2=1
#for i in range(1, 50):
#    print(n2, end=" ")
#    n1, n2 = n2, n1+n2

#def fib(n):
#    if n <= 1:
#        return n
#    return fib(n - 1) + fib(n - 2)
#print(fib(6))
number_of_digits=0
number_of_letters=0
s=input("Enter a string: ")
for i in range(len(s)):
  if(s[i].isdigit()):
    number_of_digits+=1
  else:
    number_of_letters+=1
print("Number of digits:", number_of_digits)
print("Number of letters:", number_of_letters)