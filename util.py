import queue

def open_file(filename):
    with open(filename, "r", encoding = "UTF-8") as file:
        return file.read().splitlines()
    
def write_file(filename, content):
    with open(filename, "a+", encoding = "UTF-8") as file:
        file.write(content + "\n")

def create_queue(data: dict):
    data_queue = queue.Queue()
    for key in data.keys():
        data_queue.put([key, data[key]])
    return data_queue

