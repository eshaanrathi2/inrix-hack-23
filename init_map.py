from json_reader import json_reader

class map_init:
    def __init__(self):
        read_json = json_reader()
        self.data = read_json.get_data()
        self.info = []
        for i in range(0, len(self.data['result'])):
            self.info.append({"coords":self.data['result'][i]['geometry']['coordinates'], "id": self.data['result'][i]['id']})
        
    def get_info(self):
        return self.info

def main():
    map_init()

if __name__ == "__main__":
    main()