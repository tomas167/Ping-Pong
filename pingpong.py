import pygame

pygame.init()

# Veľkosť okna
SIRKA = 800
VYSKA = 600
okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Ping-Pong")

# Farba pozadia (svetlomodrá)
POZADIE = (170, 230, 230)

# Hlavná slučka hry
bezi = True
while bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False

    okno.fill(POZADIE)
    pygame.display.flip()

pygame.quit()