class Calculator:
    def add(self, nmbr1, nmbr2):
        # result = nmbr1 + nmbr2
        result = f' i want to show the total of this number :{nmbr1 + nmbr2}'
        return result

    def dedcut(self, nmbr1, nmbr2):
        return  nmbr1 - nmbr2

    def multiplication(self, nmbr1, nmbr2):
        result = f'i want to show the result: {nmbr1 * nmbr2}'
        return result
    def division(self, nmbr1, nmbr2):
        return nmbr1 / nmbr2

my_calculator = Calculator()
result_add = my_calculator.add(10, 20)
result_deduct = my_calculator.dedcut(20, 40)
result_mul = my_calculator.multiplication(30, 40)
result_division = my_calculator.division(10, 5)
print(result_add)
print(result_deduct)
print(result_mul)
print(result_division)