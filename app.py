from field import Field
from terrorist import Terrorist

# Initiate a field
field = Field(5,5)

# Initiate a terrorist
t1 = Terrorist('Jack','Reapers')



if __name__ == "__main__":
    # Display the field
    field.show()

    # Check t1 info
    print(t1)

    # Create 2 bombs
    t1.create_bomb('C4')
    t1.create_bomb('TNT')

    # Check list of available bombs
    t1.check_bombs(True)

    # Check specific bomb's specs
    t1.check_bombs(False, 'C4')
    t1.check_bombs(False, 'TNT')

    # Plant a bomb
    t1.plant_bomb(field, 'C4', 2, 3)

    # See the field with the bomb
    field.show()
