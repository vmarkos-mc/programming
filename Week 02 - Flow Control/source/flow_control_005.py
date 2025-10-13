# source/flow_control_005.py
n = int(input("Please, enter an integer: "))
if n == 5:
    output = "Foo"
elif n <= 5:
    output = "Bar"
elif n > 7:
    output = "Foobar"
else:
    output = "Barfoo"
print(output)