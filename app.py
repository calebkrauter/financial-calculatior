import json

value = input('Enter a new account Name: \n')
print(f'you entered {value}')

key_value = input('Enter the ammount of money in ' + value + ': $')
info = 'stored-input.txt'

# with open(info) as json_file:
# 	info = json.load(json_file)
# 	print(info)
# 	print('Data type ', type(info))

# list_dicts = []
# list_dicts.append()
# print('list ')
# print(list_dicts)

d = dict()
d['account'] = value
d['amount'] = key_value

with open(info, 'w') as file:
	file.write(json.dumps(d))


print('$' + key_value + ' is in account: ' + value)

file_read = open(info, 'r')
file_contents = file_read.read()
print(file_contents)

