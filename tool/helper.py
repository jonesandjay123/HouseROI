class Helper:
    @staticmethod
    def read_access_token(file_name):
        with open(file_name, 'r') as file:
            return file.read().strip()