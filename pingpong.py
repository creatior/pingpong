from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 390:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 390:
            self.rect.y += self.speed
        
window = display.set_mode((700,500))
window.fill((170, 170, 170))
display.set_caption('Ping-pong')

clock = time.Clock()

player_l = Player('left.png',20,220,60,100,5)
player_r = Player('right.png',620,220,60,100,5)
ball = GameSprite('ball.png',320,240,50,50,7)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((170, 170, 170))
    player_l.reset()
    player_l.update_l()
    player_r.reset()
    player_r.update_r()
    ball.reset()
    clock.tick(60)
    display.update()