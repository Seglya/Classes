# Day1 homework
import time
from datetime import datetime
x=365*24
print ("1 year has %s hours" %x)


x=365*24*10*60
print ("decade has %s minutes" % x)
print("now ", datetime.now())
today=datetime.now()
x=(today-datetime(1987,1,24,16,15)).total_seconds()
print ("I am %s seconds old" % x )
delta=(datetime.now()-datetime(1970,1,1)).total_seconds()-x+300*60 #From my time zone UTC -5
print("My Birthday: ",datetime.fromtimestamp(delta))

#Andreea Birthday
x=48618000*24
delta=(datetime(2018,7,16,8,23 )-datetime(1970,1,1)).total_seconds()-x+300*60 # From my time zone UTC -5
print("Andreea Birthday: ",datetime.fromtimestamp(delta))
print("Andreea is %s years old" % (x/60/60/24/365))

#32bit (64bit) system timeout
system=[32,64]
for i in range(0,2):
	maxInt=pow(2,system[i])
	print("%s bit system timeout is %s days" %(system[i],maxInt/1000/60/60/24))


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
	for x in text:
		if x.lower().startswith("chapter"):
			print(x.ljust(50), end='')
		else :
			print(x)
	return

def main():
 	get_name()
 	favorite_number()
 	angry_boss()
 	table_of_contents()
 	return

main()
####################
#     Week1 Day 4  #
####################
import random

#99 Bottles of beer on the wall function
def _99_bottles_of_beer():
	x=99
	while x>1:
		y=x-1
		print("{0} bottles of beer on the wall, {0} bottles of beer.\nTake one down and pass it around, {1} bottles of beer on the wall.\n".format(x,y) )
		x-=1
	if x==1:
		print ("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n")
		x-=1
	if x==0:
		print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
	return

#Deaf grandma function
def grandma():
	
	start_year=int(input("Input start year: "))
	finish_year=int(input("Input finish year: "))
	print("Say something to your grandma...")
	flag=0
	while True:
		text=input("You: ")
		if text.isupper()!=True:
			flag=0
			print("Grandma: HUH?! SPEAK UP, GIRL!")
		else:
			if text=="BYE":
				flag+=1
				if flag==3:
					print("Grandma: BYE")
					break
			else:
				flag=0
				while True:
					year=random.randint(start_year,(finish_year+1))
					if (year%4)==0:
						if (year%100)==0:
							if(year%400)==0:
								print("Grandma: NO, NOT SINCE %s!" %year)
								break
						print("Grandma: NO, NOT SINCE %s!" %year)
						break
			
	return
#Building and Sorting an array
def sorting_array():
	print("Please input words:")
	words=[]
	while True:
		new_word=input()
		if len(new_word)==0:
			break
		words.append(new_word)
	for x in sorted(words):
		print (x)
	return
# Moo function
def moo():
	n=int(input("Plese input the number: "))
	while n>0:
		print("moo")
		n-=1
	return
# Roman numbers
def old_roman_numbers():
	try:
		number=int(input("Please input the number 1...3000: "))
	except ValueError:
		print("No valid number! Please try again...")
	roman_number=""
	m=number//1000
	d=(number-m*1000)//500
	c=(number-m*1000-d*500)//100
	l=(number-m*1000-d*500-c*100)//50
	x=(number-m*1000-d*500-c*100-l*50)//10
	v=(number-m*1000-d*500-c*100-l*50-x*10)//5
	i=(number-m*1000-d*500-c*100-l*50-x*10-v*5)
	roman_number='M'*m+'D'*d+'C'*c+'L'*l+'X'*x+'V'*v+'I'*i
	print(roman_number)
	return
def new_roman_numbers():
	try:
		number=int(input("Please input the number 1...3000: "))
	except ValueError:
		print("No valid number! Please try again...")
	roman_number=""
	m=number//1000
	d=(number-m*1000)//500
	c=(number-m*1000-d*500)//100
	l=(number-m*1000-d*500-c*100)//50
	x=(number-m*1000-d*500-c*100-l*50)//10
	v=(number-m*1000-d*500-c*100-l*50-x*10)//5
	i=(number-m*1000-d*500-c*100-l*50-x*10-v*5)
	tous=""
	hundr=""
	ten=""
	if c==4:
		if(d==0):
			tous='C'+'D'
		else:
			tous='C'+'M'
		roman_number='M'*m+tous
	else:
		roman_number='M'*m+'D'*d+'C'*c
	if x==4:
		if(l==0):
			hundr='X'+'L'
		else:
			hundr='X'+'C'
		roman_number+=hundr
	else:
		roman_number+='L'*l+'X'*x
	if i==4:
		if(v==0):
			ten='I'+'V'
		else:
			ten='I'+'X'
		roman_number+=ten
	else:
		roman_number+='V'*v+'I'*i
	
	print(roman_number)
	return
def main():
	_99_bottles_of_beer()
	grandma()
	sorting_array()
	a=moo()
	print(a)
	old_roman_numbers()
	new_roman_numbers()
	return
main()