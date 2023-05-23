def add(n1, n2):
    return n1+n2
    
def sub(n1, n2):
    return n1-n2
    
def mult(n1, n2):
    return n1*n2
    
def div(n1, n2):
    return n1/n2
    
signs={"+":add,"-":sub,"*":mult,
"/":div}

num1=int(input('What is the first number?'))
num2=int(input('What is the second number?'))

for symbols in signs:
    print(symbols)

operation=input('Which operation do you like to use from above:')
calculation_function=signs[operation]
answer=calculation_function(num1, num2)

print(f"{num1}{operation}{num2}= {answer}")
