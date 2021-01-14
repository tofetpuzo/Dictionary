def mean(value):
    if isinstance(value, dict):
    # if type(value) == dict:
       the_mean = sum(value.values()) / len(value)

    else:
       the_mean = sum(value) / len(value)
    
    return the_mean


def foo(username):
    if len(username) > 8:
        return True
    else:
        return False

# print(foo("myname is good "))


def temp(value):
    if value > 25:
        return "Hot"
    elif value >= 15 or value <= 25:
        return "Warm"
    else:

        return "Cold"


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"} 
for value in phone_numbers.values():
    print(" %s" % (value).replace("+" , "00"))
()