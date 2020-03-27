import os
import random
from datetime import datetime

number = '0123456789'
symbol = '@!#$%&*(){}[]<>;.,|+-/"'
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def file_name():

	get_name = ''

	for char in range(16):

		get_name += random.choice(lower + upper + number)

	return get_name


def str2bool(v): return str(v).lower() in ("Yes", "True", "yes", "true", "y", "t", "Y", 'T')


def generate():

	char = ''
	
	count = 0
	folder = 'exports/'

	print(f'-' * 75)
	print('Small Password Generator'.center(75))
	print('>> By: thesilvacesar <<'.center(75))
	print(f'-' * 75 + "\n")

	size = input('[+] => Password size: ')
	total = input('[+] => Total of password [min. 1] [max. 1,500,000]: ')
	legend = input("[+] => Show legend ? [Def.: 'n'] [y/n]: ")
	export = input("[+] => Export passwords ? [Def.: 'n'] [y/n]: ")
	print("\r")

	total = int(total)
	legend = str2bool(legend)

	get_password = ''

	print(f'-' * 75)
	print('Passwords'.center(75))
	print(f'-' * 75 + "\n")

	if str2bool(export):
		
		if not os.path.exists(folder): os.mkdir(folder)
		f = open(folder + file_name() + ".txt", "w")

		f.write(f'-' * 75 + "\n")
		f.write('Passwords'.center(75) + "\n")
		f.write(f'-' * 75 + "\n\n")

	if total > 1 < 1500000:

		while count < total:

			get_password = ''

			for char in range(int(size)):

				get_password += random.choice(lower + upper + number + symbol)

			count += 1

			if str2bool(legend):

				print(f'Password {count}: ' + get_password)
				if str2bool(export): f.write(f"Password {count}: " + get_password + "\n")

			else:

				print(get_password)
				if str2bool(export): f.write(get_password + "\n")

	elif total == 1:

		for char in range(int(size)):
			get_password += random.choice(lower + upper + number + symbol)

		count = 1

		if legend:

			print(f'Password: ' + get_password)
			if str2bool(export): f.write(get_password + "\n")

		else:

			print(get_password)
			if str2bool(export): f.write(get_password + "\n")

	print("\r")
	print(f'-' * 75)
	print('More info'.center(75))
	print(f'-' * 75)

	now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
	print(f"\n[+] => Passwords generated in: " + now)

	if str2bool(export): 
		f.write("\n")
		f.write(f'-' * 75 + "\n")
		f.write('More info'.center(75) + "\n")
		f.write(f'-' * 75 + "\n")

		f.write(f"\n[+] => Passwords generated in: " + now + "\n")
		f.close()
