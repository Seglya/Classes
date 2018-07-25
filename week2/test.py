import unittest
from week2_day1 import calculator
from week2_day1 import full_name
from week2_day1 import secret_formula
from week2_day1 import break_words
from week2_day1 import sort_words

class test_calc(unittest.TestCase):
	"""docstring for test_calc"""
	def test0(self):
		self.assertEqual(calculator(2,5,'*'), 10)
	def test1(self):
		self.assertEqual(calculator(5,3,'-'),2)
class test_full_name(unittest.TestCase):	
	"""docstring for test_full_name"selff """
	def test0(self):
		self.assertEqual(full_name("Tatsiana", "Odebunmi"),"Tatsiana Odebunmi")
class test_secret_formula(unittest.TestCase):

	"""docstring for test_secret_formula"unittest.TestCasef """
	def test0(self):
		self.assertEqual(secret_formula(1000), (500000, 500, 5))
		
class test_break_words(unittest.TestCase):
	"""docstring for test_break_words"""
	def test0(self):
		self.assertEqual(break_words("1 million women to tech"),
			(["1","million","women", "to", "tech"]))
class test_sort_words(unittest.TestCase):
	"""docstring for test_sort_words"""
	def test0(self):
		self.assertEqual(sort_words(["1", "million", "women", "to", "tech"]),
			(["1", "million","tech", "to", "women"]))
						
		
unittest.main()
		