import yaml

test_list = {
    '1':['1','2','3'],
    '2': 2,
    '3': {'a':'2€','b':'4€'}
}

with open('test.yaml','w') as f:
    yaml.dump(test_list,f,allow_unicode = True)
