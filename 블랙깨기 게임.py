import pygame
import sys
import random

# 게임 초기화
pygame.init()

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 화면 크기
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록 깨기 게임")

# 공 설정
ball_width = 20
ball_height = 20
ball = pygame.Rect(screen_width // 2 - ball_width // 2, screen_height // 2 - ball_height // 2, ball_width, ball_height)
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

# 패들 설정
paddle_width = 400
paddle_height = 20
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 10, paddle_width, paddle_height)
paddle_speed = 10

# 블록 설정
block_width = 60
block_height = 20
blocks = [pygame.Rect(i * (block_width + 10) + 35, j * (block_height + 10) + 35, block_width, block_height) for i in range(10) for j in range(5)]

# 폰트 설정
font = pygame.font.Font(None, 74)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed

    ball.left += ball_speed_x
    ball.top += ball_speed_y

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    for block in blocks[:]:
        if ball.colliderect(block):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)
            break

    if ball.top >= screen_height:
        text = font.render("게임 오버", True, RED)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
