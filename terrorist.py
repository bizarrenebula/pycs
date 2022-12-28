from bomb import Bomb

class Terrorist():
    
    def __init__(self, name, organization='self-employed'):
        self.name = name
        self.organization = organization
        self.bombs = {}
        
    def __str__(self):
        return f'{self.name} ({self.organization})'

    def create_bomb(self, bomb_type):
        try:
            if(bomb_type and bomb_type not in self.bombs):
                self.bombs[bomb_type] = Bomb(bomb_type)
                print(f'{bomb_type} bomb created!')
            elif(bomb_type and bomb_type in self.bombs):
                print(f'{bomb_type} already available!')
        except AssertionError as _e:
            print(_e)
    
    def check_bombs(self, all_bombs=True, bomb=None):
        if(len(self.bombs) > 0):
            if(all_bombs):
                print(f'Bombs available: {list(self.bombs)}')
            if(bomb):
                print(self.bombs[bomb])
            
    def plant_bomb(self, field, bomb, x, y):
        if field:
            if bomb in self.bombs:
                field.field[x][y] = [self.bombs[bomb].type]
                del self.bombs[bomb]
                print('Bomb has been planted!')
            else:
                print('Nothing to plant...create bomb first!')
        else:
            print('Where should I plant the bomb?')
        