
def return_name(name):
    name="changed"
    print (dir())
    return name

#pdb.set_trace()
name=input("Enter your nam:")
print("Hello",return_name(name))