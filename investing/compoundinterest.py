import locale


def main():
	locale.setlocale(locale.LC_ALL, 'en_US')
	total = 0
	print("deposit amount per year:")
	deposit = int(input())
	print("age")
	age = int(input())
	for x in range(age, 100):
		total += deposit
		total += total * .07
		formatted_total = format_money(total)
		print("When you are " + str(x) + " Your worth will be $" + str(formatted_total),)
		pause = input()


def format_money(money):
	formatted_money = float(("%.2f" % round(money, 2)))
	formatted_money = "{:,}".format(formatted_money)
	return formatted_money


if __name__ == "__main__":
	main()
