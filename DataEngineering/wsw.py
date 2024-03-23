# def func(data):	
# 	if type(data) == dict:
# 		for val in data.values():
# 			if any(isinstance(i, list or dict) for i in val) == True:
# 				data[val] = func(val)
# 			else:
# 				data[val] = sum(val.values())
# 	else:
# 		for item in range(len(data)):
# 			if type(data[item]) != int:
# 				if any(isinstance(i, list or dict) for i in data[item]) == True:
# 					return func(data[item])
# 				else:
# 					data[item] = sum(data[item])
# 		return data

def conv(data):
	for val in data.values():			
		def func(inner):	
			for i in inner:
				if isinstance(i, list or dict) == True:
					return func(i)
				else:
					pass
				
	return func(val)


data_dict = {'a': [1, [2, [3, 2], 4], [5, 6, 7]], 'b': [{'c':8, 'd':9}, {'e':3, 'f':4}, 8]}
print(conv(data_dict))