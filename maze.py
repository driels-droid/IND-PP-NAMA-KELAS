from pygame import*
window = display.set_mode((700, 500))

display.set_caption("Maze")

bg = transform.scale(image.load("background.jpg"), (700, 500))

mixer.init()
mixer.music.load('RUINS.mp3')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.arah = 'right'
    def update(self):
        if self.arah == ' right':
            self.rect.x += self.speed
        if self.arah == 'left':
            self.rect.x -= self.speed

        if self.rect.x < 470:
            self.arah = 'right'
        if self.rect.x > 615:
            self.arah = 'left'

class WALL(sprite.Sprite):
    def __init__(self, color_1, color_2 , color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

w1 = WALL(154, 205, 50, 100, 20, 450, 10)
w2 = WALL(154, 205, 50, 100, 480, 350, 10)
w3 = WALL(154, 205, 50, 100, 20, 10, 380)
w4 = WALL(154, 205, 50, 200, 130, 10, 350)
w5 = WALL(154, 205, 50, 450, 130, 10,360)
w6 = WALL(154, 205, 50, 300, 20, 10, 350)
w7 = WALL(154, 205, 50, 390, 120, 130, 10)

packman = Player('frisk.png', 5, 420, 4)
monster = Enemy('undyne.png', 620, 280, 2)
final = GameSprite('souls.png', 580, 420, 0)

clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (235, 5, 28))

finish = False

# Loop Game
run = True
while run:
    clock.tick(FPS)
    # Mendeteksi Event
    for e in event.get():
        if e.type == QUIT:
            run = False
    # Meletakkan Aset dan Objek

    if finish == False:
        window.blit(bg, (0,0))
        packman.reset()
        monster.reset()
        final.reset()
        packman.update()
        monster.update()

    if sprite.collide_rect(packman, w1):
        finish = True
        window.blit(lose, (50, 50))

    if sprite.collide_rect(packman, final):
        finish = True
        window.blit(lose, (50, 50))
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    w7.draw_wall()

    display.update()
