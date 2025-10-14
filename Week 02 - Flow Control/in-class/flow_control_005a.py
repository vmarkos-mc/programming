# in-class/flow_control_005a.py

n = int(input("Please, enter an integer: "))
if n < 6 and 4 < n: # not (n < 5 or 5 < n)
    output = "Foo"
elif n < 5:
    output = "Bar"
elif 7 < n:
    output = "Foobar"
else:
    output = "Barfoo"
print(output)