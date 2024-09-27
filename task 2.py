'''
def calc(a, b, operation):
     match operation:
          case "+":
               return a + b
          case "-":
               return a - b
          case "*":
               return a * b
          case "/":
               return a / b

map()
print(calc(a, b, '+'))  
'''
def calc(operation):
    numbers = list(filter(str.isdigit, operation))
    operators = list(filter(lambda x: not x.isdigit() and x.strip(), operation))
    
    if len(numbers) < 2 or len(operators) == 0:
        return "Ошибка: недостаточно данных для операции"
    
    a, b = map(int, numbers[:2])  # Пробуем привести только первые два найденных числа
    operation = operators[0]  # Берем первый найденный оператор
    
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "Ошибка: деление на ноль"
            else:
                return a / b
        case _:
            return "Ошибка: неизвестный оператор"

operat = input("Введите операцию: ")
result = calc(operat)
print(result)