'''Write a Python program that implements a menu-driven interface for managing a list of integers. The program should have the following menu options:

1. Add

2. Remove

3. Display

4. Quit



The program should repeatedly prompt the user to enter a choice from the menu. Depending on the choice selected, the program should perform the following actions:

Add: Prompts the user to enter an integer and add it to the integer list. If the input is not a valid integer, display "Invalid input".
Remove: Prompts the user to enter an integer to remove from the list. If the integer is found in the list, remove it; otherwise, display "Element not found". If the list is empty, display "List is empty".
Display: Displays the current list of integers. If the list is empty, display "List is empty".
Quit: Exits the program.
The program should handle invalid menu choices by displaying "Invalid choice".Ensure that the program continues to prompt the user until they choose to quit (option 4).
'''

number =[]
f = True
while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")

	n = int(input("Enter choice: "))
	if n==1:
		num = int(input("Integer: "))
		number.append(num)
		print("List after adding:",number)
	elif n==2:
		if len(number)==0:
			print("List is empty")
		else:
			x= int(input("Integer: "))
			if len(number)==0:
				print("List is empty")
			elif x in number:
				number.remove(x)
				print("List after removing:",number)
			else:
				print("Element not found")

	elif n==3:
		if len(number)==0:
			print("List is empty")
		else:
			print(number)
	elif n==4:
		f= False
		break
	else:
		print("Invalid choice")