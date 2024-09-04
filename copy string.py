def copy_string(source):
    if source == "":
        return ""
    else:
        return source[0] + copy_string(source[1:])
original_string = "Hello, World!"
copied_string = copy_string(original_string)
print(copied_string)
