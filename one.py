
#  in = "userInBlocked"
#  out = "user_in_blocked"

def return_pascal_in_snake(name: str):
    res = ""
    for char in name:
        if char.isupper():
            res += "_" + char.lower()
        else:
            res += char

s = "userInBlocked"

snaked_s = return_pascal_in_snake(s)
print(snaked_s)