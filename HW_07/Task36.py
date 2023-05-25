#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
#которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
#Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
#Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).


def print_operation_table(operation, num_rows=6, num_columns=6):

	matrix = []
	for row in range (1,num_rows+1):
		a = []
		for column in range (1,num_columns+1):
			a.append(str(operation(row, column)))
		matrix.append(a)

	for row in range(num_rows):
		for column in range(num_columns):
			print(matrix[row][column], end=" ")
		print()


print_operation_table(lambda x, y: x + y)

