import queue

def open_file(filename):
    with open(filename, "r", encoding = "UTF-8") as file:
        return file.read().splitlines()
    
def write_file(filename, content):
    with open(filename, "a+", encoding = "UTF-8") as file:
        file.write(content + "\n")