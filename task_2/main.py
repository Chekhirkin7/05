import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float]:
	pattern = r'\s(\d+.\d+)\s' #Патерн для пошуку чисел в рядку типу "число.число" + ігнорування на спеціальні символи
	for match in re.findall(pattern, text): #Перебираємо по одному значенню за раз, щоб програма працювала швидше
		yield float(match) #Повернення одного значення з циклу та збереження його, оскільки це генератор

def sum_profit(text: str, func: Callable[[str], Generator[float]]) -> float: # type: ignore #Приймаємо рядок і функцію для подальшого обчислення
	return sum(func(text)) #Повернення суми

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")