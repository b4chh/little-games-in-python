import pygame
from game import Game
pygame.init()

pygame.display.set_caption("Test")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

game = Game()

running = True

while running:

    screen.blit(background, (0, -200))

    screen.blit(game.player.image, game.player.rect)

    for projectil in game.player.all_projectiles:
        projectil.move()

    for monster in game.all_monsters:
        monster.forward()

    game.all_monsters.draw(screen)

    game.player.all_projectiles.draw(screen)

    # vérifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # mettre à jour la fenetre
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('left')
                if event.key == pygame.K_RIGHT:
                    print('right')
                if event.key == pygame.K_UP:
                    print('jump')
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    print('left stop')
                if event.key == pygame.K_RIGHT:
                    print('right stop')