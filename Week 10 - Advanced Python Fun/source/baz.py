# source/baz.py

def baz(num, **kwargs):
    name = "John Doe"
    msg = "My Number is: "
    if "name" in kwargs:
        name = kwargs["name"]
    if "msg" in kwargs:
        msg = kwargs["msg"]
    known_kwargs = {"name", "msg"}
    for kwarg in set(kwargs).difference(known_kwargs):
        print(f"Unknown argument: {kwarg}.")
    print(f"{name} says: '{msg} {num}'.")