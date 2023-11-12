from json_reader import json_reader

class data_reader:
    def __init__(self, parameter = "ex", id = -1, data = None):
        if data is None:
            raise Exception("Invalid data provided")
        self.data = data
        if parameter not in self.data['result'][0].keys():
            raise Exception("Invalid parameter called")
        if parameter == "coordinates":
            self.get_coords(parameter)
        self.index = self.search(id)
        if self.index == -1:
            raise Exception("Invalid ID Called")
        
    def search(self, id):
        for i in range(0, len(self.data['result'])):
            if self.data['result'][i]['id'] == id:
                return i
        return -1
    def get_values(self, id):
        return self.index['result'][self.index]

def main():
    read_json = json_reader()
    data = read_json.get_data()
    parameter = "id"
    id = -1
    data_reader(parameter, id, data)

if __name__ == "__main__":
    main()