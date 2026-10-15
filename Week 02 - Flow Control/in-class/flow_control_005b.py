# in-class/flow_control_005a.py
n = int(input("Please, enter an integer: "))
if n < 5:
    output = "Bar"
elif n < 6:
    output = "Foo"
elif 7 < n:
    output = "Foobar"
else:
    output = "Barfoo"
print(output)