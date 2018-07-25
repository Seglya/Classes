#Week 2 Day 1 Homework
import string
#Alice_in_wonderland
def read_from_file(file_name):
	text=[]
	with open(file_name, encoding='utf-8') as f:#open and reading from file
		text=f.read()
	return text
def count_letters(text):
	letters_list=string.ascii_uppercase
	counted_letters=[]
	for letter in letters_list: # For each letter in the alphabet counting appearence in the text
		num=text.count(letter)
		counted=[letter,num]
		counted_letters.append(counted)
	return counted_letters
#Unittesting:
# functions
def secret_formula(started):
	jelly_beans=started*500
	jars=jelly_beans/1000
	crates=jars/100
	return jelly_beans, jars, crates
def break_words(stuff):
	words=stuff.split(' ')
	return words
def sort_words(words):
	return sorted(words)
def full_name(first_name, second_name):
	full_name=first_name+" "+second_name
	return full_name
def calculator(number1,number2, sign):
	if sign=='+':
		result=number1+number2
	elif sign=='-':
		result=number1-number2
	elif sign=='*':
		result=number1*number2
	elif sign=='/':
		result=number1/number2
	else:
		print("Wrong input!!!")
	return result
def main():
	file_name="alice_in_wonderland.txt"
	text=read_from_file(file_name).upper()
	table=count_letters(text)
	print(table)
	return
#main()