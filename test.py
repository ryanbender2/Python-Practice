def calculator(num1, operator, num2):
    if operator == '+': 
        return num1 + num2
    if operator == '*': 
        return num1 * num2 
    if operator == '/': 
        if num2 == 0:
            return "Can't divide by 0!"
        return num1 / num2
    if operator == '-': 
        return num1 - num2
    return "Not a Vaild Operator"
        

# If the input tries to divide by 0, return: "Can't divide by 0!"
print(calculator(7, "/", 7))