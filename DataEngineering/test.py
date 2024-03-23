import numpy as np

def func(data):
    if type(data) == dict:
        for key in data.keys():
            if any(isinstance(i, dict) for i in data[key]) == True:
                return func(data[key])
    else:
        for item in range(len(data)):
            if type(data[item]) == dict:
                data[item] = sum(data[item].values())
            elif type(data[item]) != int:
                data[item] = sum(data[item])


data_dict = {'a': [1, [2, 3, 4], [5, 6, 7]], 'b': [{'c':8, 'd':9}, {'e':3, 'f':4}, 8]}