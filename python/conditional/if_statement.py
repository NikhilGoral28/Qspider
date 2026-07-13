# q1 - WAP to check greatest amoung two numbers

a = 20
b = 10

if a>b:
    print(f'a:{a} is greater than b:{b}')  # a:20 is greater than b:10

#-----------------------------------------------------
# q2 - Wap to check the given number is positive

num = 34

if num > 0:
    print(f'{num} is positive')  # 34 is positive

#------------------------------------------------------

#q3 - WAP to check the given number is even

num = 56

if num % 2 == 0:
    print(f'{num} is even number')  # 56 is even number

#--------------------------------------------------------------------

#q4 - WAP To check the given number is odd

num = 77

if num % 2 != 0:
    print(f"{num} is odd number")  # 77 is odd number

#-----------------------------------------------------------------------

#q5- WAP to check given number is divisible by 3

num = 15

if num % 3 == 0:
    print(f"{num} is divisible by 3")  # 15 is divisible by 3

#---------------------------------------------------------------------------
 
#q6- WAP to check given number is divisible by 5

num = 25

if num % 5 == 0:
    print(f"{num} is divisible by 5")  # 25 is divisible by 5


#---------------------------------------------------------------------------

#q7 - WAP to check the give number is divisible by 3 and 5

num = 15

if num % 3 == 0 and num % 5 == 0:
    print(f'{num} is divisible by 3 and 5')   # 15 is divisible by 3 and 5



#---------------------------------------------------------------------------

#q8 - WAP to check the given string starts with the ovels

s = 'apple'

if s[0] in 'aeiouAEIOU':
    print(f'{s} is starts with the ovels')  # apple is starts with the vovels


#---------------------------------------------------------------------------

#q9 - WAP to check the given string starts with the consonents

s = 'microsoft'

if s[0] not in 'aeiouAEIOU':
    print(f'{s} is starts with the consonents')  # apple is starts with the  consonents


#---------------------------------------------------------------------------

#q10 - WAP to check the given string ends with the ovels

s = 'apple'

if s[-1] in 'aeiouAEIOU':
    print(f'{s} is ends with the ovels')  # apple is ends with the vovels


#---------------------------------------------------------------------------

#q11 - WAP to check the given string ends with the consonents

s = 'apple'

if s[-1] not in 'aeiouAEIOU':
    print(f'{s} is ends with the consontes')  # apple is ends with the consonents


#----------------------------------------------------------------------------------

#q12 - WAP to check given string starts with the upper case

s = 'Apple'

if s[0] <= 'A' and s[0] <= 'Z':
    print(f'{s} starts with the upper case')  # Apple starts with the upper case


#-------------------------------------------------------------------------------

#q13 - WAP to check given char is in lower case

ch = 'a'

if 'a'<=ch<='z':
    print(f'{ch} is lower case') # a is lower case


#-----------------------------------------------------------------------

#q13 - WAP to check given char is  digit

ch = '9'

if '0'<=ch<='9':
    print(f'{ch} is digit') # 9 is digit


#-------------------------------------------------------------------------------

#q13 - WAP to check given char is special symbol

ch = '$'

if not ('A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9'):
    print(f'{ch} is special symbol') # $ is special symbol

