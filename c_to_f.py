age = input('請輸入年齡:')
age = int(age)
if age >= 20:
	print('你可以投票')
if age < 20:
	print('你不能投票ㄎㄎ')


c = input('請輸入攝氏溫度:')
c = float(c)
f = c * 9 / 5 + 32
print('華氏溫度為：', f)
