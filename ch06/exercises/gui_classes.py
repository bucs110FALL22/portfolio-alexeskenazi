
class Character:
    def __init__(self):
        self.player_num = 1
        self.lives = 3  # players always start with 3 lives
        self.is_large = False  # player always starts small
    
    def make_small(self):
        self.is_large = False

    def make_large(self):
        self.is_large = True

    def is_dead():
        return self.lives == 0

class Prize:
    def __init__(self):
        self.position = (20, 30)
        self.value = 100  # Prize in coins
        self.active = True  # prize not claimed

        
class Goomba:
    def __init__(self):
        self.id = 1
        self.position = (20, 10)
        self.speed = 30  # Movement speed
        self.active = True
        self.is_large = False
        self.color = 'red'