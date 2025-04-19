from pygame import *
back = (200, 255, 255)
win_widht = 700
win_height = 500



clock = time.Clock()
FPS = 60
speed = 5
game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, plaer_speed, plaer_image, plaer_x, plaer_y, wigth, height):
        super().__init__()
        self.image = transform.scale(image.load(plaer_image), (wigth, height))
        self.speed = plaer_speed
        self.rect = self.image.get_rect()
        self.rect.x = plaer_x
        self.rect.y = plaer_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys_passed = key.get_pressed()

        if keys_passed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed

        if keys_passed[K_s] and self.rect.y < 490:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_passed = key.get_pressed()

        if keys_passed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed

        if keys_passed[K_DOWN] and self.rect.y < 490:
            self.rect.y += self.speed






window = display.set_mode((win_widht, win_height))
window.fill(back)
display.set_caption('pin-pong game')
hero1 = Player1(5,"tennis-racket.png", 10, 250, 50, 65)
hero2 = Player2(5,"tennis-racket.png", 650, 250, 50, 65)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    hero1.update()
    hero1.reset()
    hero2.update()
    hero2.reset()
    display.update()
    clock.tick(FPS)

       




