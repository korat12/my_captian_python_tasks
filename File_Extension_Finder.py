
filename = input("Input the Filename: ")

extension = filename.split(".")[-1]

if extension == "py":
    ext_name = "python"
else:
    ext_name = extension

print("The extension of the file is :", repr(ext_name))
