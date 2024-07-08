import csv

class UTILS:

    def __init__(self):
        pass
    
    # function to read csv by user
    @staticmethod
    def read_csv(file_path):
        data = []
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

    @staticmethod
    def save_to_csv(data, file_path, headers=None):
        mode = "w" if headers else "a"
        with open(file_path, mode, newline="") as file:
            writer = csv.writer(file)
            if headers:
                writer.writerow(headers) # write headers of csv file
            for row in csv.reader(data.splitlines()):
                writer.writerow(row)
