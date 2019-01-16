#import pdb
import re

regex = r".*\(\d\):.*name.*"
py_code='''
--- modulename: functrack, funcname: <module>
functrack.py(2): def return_name(name):
functrack.py(8): name=input("Enter your nam:")
Enter your nam:mohit
functrack.py(9): print("Hello",return_name(name))
 --- modulename: functrack, funcname: return_name
functrack.py(3):     name="changed"
functrack.py(4):     print (dir())
['name']
functrack.py(5):     return name
Hello changed
 --- modulename: trace, funcname: _unsettrace
'''
matches = re.finditer(regex, py_code, re.MULTILINE)


for matchNum, match in enumerate(matches, start=1):
    
    print ( match.group())




#def return_name(name):
#    name="changed"
#    print (dir())
#    return name

#pdb.set_trace()
#name=input("Enter your nam:")
#print("Hello",return_name(name))




