import os


def read_file(folder_name, file_name):
    cwd = os.getcwd()
    source = os.path.join(cwd, folder_name, file_name)
    with open(source) as f:
        data = [line.strip() for line in f.readlines()]
        
    return data

print(os.getcwd())
print(os.path.dirname(os.getcwd()))

