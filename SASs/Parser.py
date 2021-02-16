import yaml

class parser:
    """A config parser class"""
    cfg = []
    def __init__(self):
       # stream = file('document.yaml', 'r')
        with open("config.yml", "r") as ymlfile:
            self.cfg = yaml.safe_load(ymlfile)
    
    def component_parse(self):
        return self.cfg["component"];  

    def parse(self):
        for section in self.cfg:
            print(section)
        print(self.cfg["other"])
        