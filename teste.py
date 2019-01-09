#!/usr/bin/python
import sys

def fReturnExpression(vOne, vTwo, vExpression):
    
    vExpression = vExpression.replace('\r','')

    if vExpression == "sum":
        vReturn = vOne + vTwo
    elif vExpression == "diff":
        vReturn = vOne - vTwo
    else:
        print("Expression ", vExpression, "doesn't exist!")
        vReturn=None
    return vReturn


print("Choice your command (sum/diff):")

if sys.hexversion >= 0x3000000:
    vCommand = input()
else:
    vCommand = raw_input()

print("First number: ")
vFirstNumber = int(input())
print("Second number: ")
vSecondNumber = int(input())

print(vFirstNumber, " ", vCommand, " ", vSecondNumber, " equal ", fReturnExpression(vFirstNumber, vSecondNumber, vCommand))
