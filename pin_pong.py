from pygame import *
from random import choice, randint
back = (200, 255, 255)
win_widht = 700
win_height = 600
init()

font.init()
score_font = font.SysFont('Arial', 36)
clock = time.Clock()
FPS = 60
speed = 4
score1 = 0
score2 = 0
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

        if keys_passed[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_passed = key.get_pressed()

        if keys_passed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed

        if keys_passed[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed






window = display.set_mode((win_widht, win_height))
window.fill(back)
display.set_caption('pin-pong game')
hero1 = Player1(5,"image_processing20200914-32184-htqdir.png", 10, 250, 70, 85)
hero2 = Player2(5,"image_processing20200914-32184-htqdir.png", 620, 250, 70, 85)
ball = Player1(5,"—Pngtree—tennis ball clipart png_4354778.png", 350, 250, 50, 50)
speed_x = 3
speed_y = 3


def reset_ball():
    ball.rect.x = win_widht // 2 - 25
    ball.rect.y = win_height // 2 - 25
    speed_x = choice([-speed, speed])
    speed_y = choice([-randint(1,3), randint(1,3)])

    return speed_x, speed_y
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height -50 or ball.rect.y < 0:
            speed_y *= -1

        if (sprite.collide_rect(hero1, ball) and speed_x < 0) or (sprite.collide_rect(hero2, ball)and speed_x > 0):
            speed_x *= -1.1
            speed_y *= 1
        if ball.rect.x < 0:
            score2 += 1
            speed_x, speed_y = reset_ball()
        if ball.rect.x > win_height:
            score1 += 1
            speed_x, speed_y = reset_ball()


        score_text =score_font.render(f'{score1} : {score2}', True, (0, 0, 0))
        window.blit(score_text, (win_height // 2 - 40, 20))
    

    hero1.update()
    hero1.reset()
    ball.reset()
    hero2.update()
    hero2.reset()

    display.update()
    clock.tick(FPS)
quit()
       



