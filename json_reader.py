import json

class json_reader:
    def __init__(self):
        f = open('/Users/jameshunter/Downloads/response.json')

        self.data = json.load(f)

    def get_data(self):
        return self.data
