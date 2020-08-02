country = input ('請問你是哪國人: ')
age = input('你輸入年齡: ')
country = str(country)
age = float(age)
if country == '台灣':
	if age >= 18:
		print ('你可以考駕照')
	else: 
		print ('你還不能考駕照')
elif country == '美國':
	if age >= 16:
		print ('你在美國可以考駕照')
	else:
		print ('你在美國還不能考駕照')
else:
	print('你只能輸入台灣或美國')