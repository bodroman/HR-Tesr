def convert_camel_to_snake(name: str):
    res = ""
    for char in name:
        if char.isupper():
            res += "_" + char.lower()
        else:
            res += char

s = "userInBlocked"

snaked_s = convert_camel_to_snake(s)
print(snaked_s)

