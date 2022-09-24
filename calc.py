equation = input("Input your equation here no spaces, use + - * /): ")
if '+' in equation:
    plus = equation.find('+')+1
    length = len(equation)
    last_num = plus 
    first_num = plus - 1
    first_chars = equation[0:first_num]
    last_chars = equation[last_num:length]
    sum = float(first_chars) + float(last_chars)
    print("Sum")
    print(sum)
if '-' in equation:
    plus = equation.find('-')+1
    length = len(equation)
    last_num = plus 
    first_num = plus - 1
    first_chars = equation[0:first_num]
    last_chars = equation[last_num:length]
    sum = float(first_chars) - float(last_chars)
    print("Differnce")
    print(sum)
if '*' in equation:
    plus = equation.find('*')+1
    length = len(equation)
    last_num = plus 
    first_num = plus - 1
    first_chars = equation[0:first_num]
    last_chars = equation[last_num:length]
    sum = float(first_chars) * float(last_chars)
    print("Product")
    print(sum)
if '/' in equation:
    plus = equation.find('/')+1
    length = len(equation)
    last_num = plus 
    first_num = plus - 1
    first_chars = equation[0:first_num]
    last_chars = equation[last_num:length]
    sum = float(first_chars) / float(last_chars)
    print("Quotient")
    print(sum)
