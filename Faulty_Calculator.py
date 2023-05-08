#!/usr/bin/env python
# coding: utf-8

# # Faulty Calculator

# In[1]:


# Designed a calculator which will correctly solve all the problems except the following ones:
# 45 * 3 = 555 , 56+9 = 77, 56/6 =4


# In[2]:


print("Enter first number")
num1 = int(input())
print("Choose your operator\n"
      "for Addition (+)\n"
      "for Subtraction (-)\n"   
      "for Multiplication (*)\n"
      "for Divison (/)")
operator = input()
print("Enter second number")
num2 = int(input())
if num1==45 and operator=="*" and num2==3:
    print("555")
elif num1==56 and operator=="+" and num2==9:
    print("77")
elif num1==56 and operator=="/" and num2==6:
    print("4")
elif  operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="/":
    print(num1/num2)
elif  operator=="*":
    print(num1*num2)

