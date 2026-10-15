# in-class/flow_control_005a.py
n = int(input("Please, enter an integer: "))
if n < 6 and 4 < n: # The same as n == 5
    output = "Foo"
elif n < 5:         # "=" is not needed here
    output = "Bar"
elif 7 < n:         # x > y is the same as y < x
    output = "Foobar"
else:
    output = "Barfoo"
print(output)