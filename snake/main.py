import pygame, sys
from pygame.locals import *
from random import randrange

pygame.init()
pygame.display.set_caption("Snake")

windowWidth, windowHeight = 800, 800
cell_size = 20

screen = pygame.display.set_mode((windowWidth, windowHeight))
W = (255, 255, 255)
B = (0, 0, 0)
G = (30, 30, 30)
R = (154, 38, 23)

screen.fill(G)

def clear_console():
    print("\033[H\033[J")

def input(events):
    for event in events:
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type == KEYDOWN:
            if   event.key == pygame.K_w and App.direction != 2: App.direction = 0
            elif event.key == pygame.K_d and App.direction != 3: App.direction = 1
            elif event.key == pygame.K_s and App.direction != 0: App.direction = 2
            elif event.key == pygame.K_a and App.direction != 1: App.direction = 3
        else:
            clear_console()
            print(event)

class App:

    direction = 0
    segments = [[400, 400], [400, 420], [400, 440]]
    fruits = []

    def move():
        pygame.draw.rect(screen, G, (*App.segments[0],  cell_size, cell_size))
        pygame.draw.rect(screen, W, (*App.segments[0],  cell_size, cell_size), 1)
        pygame.draw.rect(screen, G, (*App.segments[-1], cell_size, cell_size), 1)

        for i in range(len(App.segments) - 1, 0, -1):
            App.segments[i] = App.segments[i-1].copy()

        if App.direction == 0:
            App.segments[0][1] =  (App.segments[0][1] - cell_size) % windowHeight
        elif App.direction == 1:
            App.segments[0][0] =  (App.segments[0][0] + cell_size) % windowWidth
        elif App.direction == 2:
            App.segments[0][1] =  (App.segments[0][1] + cell_size) % windowHeight
        elif App.direction == 3:
            App.segments[0][0] =  (App.segments[0][0] - cell_size) % windowWidth

        if App.segments[0] in App.segments[1:]:
            return True

        if App.segments[0] in App.fruits:
            if App.direction == 0:
                App.segments.append([App.segments[-1][0], (App.segments[-1][1] - cell_size) % windowHeight])
            elif App.direction == 1:
                App.segments.append([(App.segments[-1][0] - cell_size) % windowWidth, App.segments[-1][1]])
            elif App.direction == 2:
                App.segments.append([App.segments[-1][0], (App.segments[-1][1] + cell_size) % windowHeight])
            elif App.direction == 3:
                App.segments.append([(App.segments[-1][0] + cell_size) % windowWidth, App.segments[-1][1]])
            App.fruits.remove(App.segments[0])

            if len(App.fruits) == 0:
                App.new_fruit()

        pygame.draw.rect(screen, W, (*App.segments[0], cell_size, cell_size))


    def new_fruit():
        position = [randrange(0, windowWidth, cell_size), randrange(0, windowHeight, cell_size)]
        App.fruits.append(position)
        pygame.draw.rect(screen, R, (*position, cell_size, cell_size))

    def run():

        i = 0

        while True:
            input(pygame.event.get())
            if len(App.fruits) < 8:
                if i % 75 == 0:
                    App.new_fruit()
                    i = 0
                i += 1

            if App.move():
                break

            pygame.display.update()
            pygame.time.delay(100)



if __name__ == "__main__":
    App.run()


"""
owoce różnej wielkości 1-5 i różnych kolorów
przeszkody
wenżu nie je to go ubywa
różne kolory wenża np. po 10 segmentów
im dłuższy tym szybszy
"""
