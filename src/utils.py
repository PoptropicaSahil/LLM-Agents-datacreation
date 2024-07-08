import csv


class UTILS:
    def __init__(self):
        pass

    # function to read csv by user
    @staticmethod
    def read_csv(file_path):
        """
        Reads a CSV file and returns its contents as a list of rows.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            list: A list of rows from the CSV file, where each row is a list of values.
        """
        data = []
        with open(file_path, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

    @staticmethod
    def save_to_csv(data, file_path, headers=None):
        """
        Writes data to a CSV file.

        Args:
            data: The data to be written to the CSV file.
            file_path: The path to the CSV file.
            headers: Optional. The headers to be written to the CSV file.

        Returns:
            None
        """
        mode = "w" if headers else "a"
        with open(file_path, mode, newline="") as file:
            writer = csv.writer(file)
            if headers:
                writer.writerow(headers)  # write headers of csv file
            for row in csv.reader(data.splitlines()):
                writer.writerow(row)
