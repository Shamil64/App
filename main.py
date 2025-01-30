import pygame
import pygame_widgets
from pygame_widgets.button import Button

pygame.init()
win = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Моё приложение")
pygame.display.set_icon(pygame.image.load("icon.png"))
win.fill((255, 255, 255))
button = Button(
    # Mandatory Parameters
    win,75,  75, 150,  150,

    text='Тест',
    fontSize=20,
    margin=10,
    inactiveColour=(200, 50, 0),
    hoverColour=(150, 0, 0),
    pressedColour=(0, 200, 20),
    onClick=lambda: win.fill((0, 150, 0))
)

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()



    pygame_widgets.update(events)
    pygame.display.update()