# data = [{'a': [1, [2, 3, 4], [5, 6, 7]], 'b': [{'c':8, 'd':9}, {'e':3, 'f':4}, 8]}]
# s = {'c':8, 'd':9}
# # if isinstance(data['b'], dict) == True:
# # 	print(2)
# b = [{'c':8, 'd':9}, {'e':3, 'f':4}, 8]

# # contains_dict = any(isinstance(item, dict) for item in data['b'])

# print(sum(s.values()))

# def func(data):
# 	for key, value in data.items():
# 		if any(isinstance(i, dict) for i in data.values()) == True:
# 			for item in range(len(value)):
# 				if type(value[item]) == dict:
# 						value[item] = sum(value[item].values())
# 				elif type(value[item]) != int:
# 						value[item] = sum(value[item])
# 			return data
# 		else:
# 		  for key, value in data.items():
# 			  value = sum(data[key])

# data_dict = {'a': [1, [2, 3, 4], [5, 6, 7]], 'b': [{'c':8, 'd':9}, {'e':3, 'f':4}, 8]}

# print(func(func(data_dict)))

def func(data):
	for value in data.values():
		for item in range(len(value)):
			if type(value[item]) == dict:
					value[item] = sum(value[item].values())
			elif type(value[item]) != int:
					value[item] = sum(value[item])
	return data

data_dict = {'a': [1, [2, 3, 4], [5, 6, 7]], 'b': [{'c':8, 'd':9}, {'e':3, 'f':4}, 8]}

print(func(data_dict))

# for i in data_dict.values():
# 	for j in range(len(i)):
# 		if type(i[j]) == list:
# 			i[j] = sum(i[j])

# print(data_dict)