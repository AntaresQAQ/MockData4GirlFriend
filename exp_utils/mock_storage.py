from os import path, makedirs

from .mock_data import mock_funcs

class ExpDataStorage:
    def __init__(self, name: str):
        self.storage = []
        self.name = name
        self.mock = mock_funcs.get(self.name)
        
    def add_point(self, x, y):
        if self.mock:
            y = self.mock(x, y)
        self.storage.append((x, y))
    
    def get_all_points(self):
        self.storage.sort(key=lambda x: x[0])
        return self.storage
    
    def save_to_file(self, output_dir = "output"):
        if not path.exists(output_dir):
            makedirs(output_dir, exist_ok = True)
        with open(path.join(output_dir, f"{self.name}.txt"), "w") as f:
            for x, y in self.get_all_points():
                f.write(f"{x}\t{y}\n")
                
    def print_all_points(self):
        for x, y in self.get_all_points():
            print(f"({x}, {y})")
