# def username(phrase):
#     interrogatives = ("how", "what", "why")
#     capitalized = phrase.capitalize()
#     if phrase.startswith((interrogatives)):
#         return "{}?".format(capitalized)
#     else:
#         return "{}.".format(capitalized)

# results = []
# while True:
#     user_input = input("say something: ")
#     if user_input == "\end":
#         break
#     else:
#         results.append(username(user_input))
    

# print(" ".join(results))
    # mean 
def the_mean(*args):
    the_average = sum(args) / len(args)
    return the_average

print(the_mean(10,20,30,40))


def foo(*args):
    args = [i.upper() for i in args]
    return sorted (args)


