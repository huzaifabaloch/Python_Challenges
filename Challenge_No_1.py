"""
	Write a program or function that takes a list of integers and sort
	the same list in descending order.. for e.g
	a = [80,100,4,75,63,21,5]
	After running the function(a)
	a = [100,80,75,63,21,5,4]
"""

def swap_numbers(num1, num2):
	"""Swap two numbers."""
	
	num1, num2 = num2, num1
	return num1,  num2
	
a = [80,100,4,75,63,21,5]

def numbers_in_descending_order(list_of_numbers):
	"""Returns a list of numbers in descending order."""
	
	for i in range(len(list_of_numbers) - 1):
		
		for j in range(i, len(list_of_numbers) - 1):
			
			if list_of_numbers[i] < list_of_numbers[j+1]:
				
				list_of_numbers[i], list_of_numbers[j+1] = \
				swap_numbers(list_of_numbers[i], list_of_numbers[j+1])

	return list_of_numbers
	
print(numbers_in_descending_order(a))
	
	
