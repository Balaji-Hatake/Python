def file_ops():

    file_path = input("Please enter the path of the file : ")
    key = input("Please enter the key to be modified : ")
    value = input("Please enter the value to be modified : ")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(f"{key} = {value}\n")
            else:
                file.write(line)


file_ops()
