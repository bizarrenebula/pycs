import json

class Bomb():
    
    bomb_manual = {
        'C4':{'type':'C4', 'range':1, 'defuse':5},
        'TNT':{'type':'TNT', 'range':2, 'defuse':7}
    }
    
    def __init__(self, bomb_type):
        try:
            if bomb_type in self.bomb_manual:
                self.type = self.bomb_manual[bomb_type]['type']
                self.range = self.bomb_manual[bomb_type]['range']
                self.defuse = self.bomb_manual[bomb_type]['defuse']
        except AssertionError as _e:
            print(_e)
    
    def __str__(self):
        specs = {
            "type" : self.bomb_manual[self.type]['type'],
            "range": self.bomb_manual[self.type]['range'],
            "defuse": self.bomb_manual[self.type]['defuse']
        }
        return json.dumps(specs)
        