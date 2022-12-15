try:
    src = input("Enter name of source file : ")
    dest = input("Enter name of destination file : ")
    with open(src, "r") as f1:
        with open(dest, "w") as f2:
            lines = f1.readlines()
            alternate_lines = lines[::2]
            f2.writelines(alternate_lines)

except IOError:
    print("Error opening your files")
