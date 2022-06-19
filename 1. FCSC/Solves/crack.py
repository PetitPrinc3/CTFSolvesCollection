from werkzeug.security import check_password_hash

with open ("/usr/share/wordlists/rockyou.txt", "r", encoding='latin-1') as file:
	for line in file.readlines():
		test = check_password_hash("sha256$FKM5MLhBFZ87pPgI$a51c4c0463d199fcf4a18bd8df2f40360c46e9caed05072618e8026f02dc83bf", line)

		if test :
			print(line)
			exit()

		else:
			print("nop")
