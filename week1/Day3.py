# Week1 Day 3
#Full name greeting

def get_name():
	first_name=input("What is your first name?\n")
	middle_name=input("What is your middle name?\n")
	last_name=input("What is your last name?\n")
	print ("\nHello %s!!! Nice to see you!!!" %(first_name+' '+middle_name+' '+last_name))
	return 
#Favorite number
def favorite_number():
	fav_number=int(input("What is your favorite number?\n"))
	print("Don't you think the bigger favorite number is better!?\nI think YES, so your bigger and better favorite number is %s!!!" %(fav_number+1))
	return
#Task angry boss
def angry_boss():
	answer=input("WHAT DO YOU WANT?")
	print("WHAAAT DO YOU MEAN \"%s\"???? YOU'RE FIRED!!!" %answer.upper())
	return
# Task Table of contents
def table_of_contents():
	text=["Chapter 1: Getting Started", "page 1", "Chapter 2: Numbers", "page 9", "Chapter 3: Letters", "page 13"]
	for x in range(len(text)):
		if text[x].lower().startswith("chapter"):
			print(text[x].ljust(50), end='')
		else :
			print(text[x])
	return

def main():
 	get_name()
 	favorite_number()
 	angry_boss()
 	table_of_contents()
 	return

main()

