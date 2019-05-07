import os, sys

print ("\033[1;32mlogin dulu ya om")

username = 'bojes'      

password = 'bocahjenius'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32m    mantap om", 

			sys.exit()



		else:

			print "\033[1;32msalah terus dech\033[00m"

			print "\033[1;32myang bener dong coy\033[00m"

			restart()



	else:

		print "\033[1;32mSalah\033[00m"

		print "\033[1;32mbaca doa kalau gak bisa >:(\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
