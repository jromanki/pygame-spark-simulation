'''--- Spark-like particle grnerator/simulation made in Pygame by jromanki --- https://github.com/jromanki ---'''

import pygame, sys, random

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pySnake")

BLACK = (0, 0, 0)

FPS = 60
MAX_STRENGTH = 30
MAX_SPEED = 6
RADIOUS = 4                 # Radious of a particle
PARTICLE_MULTIPLIER = 20    # Multiplies the number of generated particles (takes only full numbers greater than 0)


'''This function sets/randomizes the initial state of a particle. The data is stored in returned 'particles' list like:
[strength(randomized), x.speed(positive or negative, randomized), y.speed(positive or negative, randomized), [x.mouse, y.mouse]]'''
def setParticles(particles):
    for i, position in enumerate(particles):
        if position.__class__==tuple:
            particles[i] = [random.randrange(MAX_STRENGTH), random.randrange(-MAX_SPEED, MAX_SPEED), 
            random.randrange(-MAX_SPEED, MAX_SPEED), list(position)]
    return particles


def dimParticle(strength):
    dimness = strength/MAX_STRENGTH
    color = int(dimness*255)
    return color


def drawParticles(particles):
    for i, position in enumerate(particles):
        position[0] -= 1
        if position[0] >= 0:
            position[3][0] += position[1]
            position[3][1] += position[2]
            pygame.draw.circle(WIN, (dimParticle(position[0]), dimParticle(position[0])*random.random(), 0),
                tuple(position[3]), RADIOUS)
        else:
            del particles[i]


def drawWindow(left, particles):
    WIN.fill(BLACK)

    if left:
        pos = pygame.mouse.get_pos()
        for i in range(PARTICLE_MULTIPLIER):
            particles.append(pos)               #If you want to place particles somewhere else, append some other 'pos' as a touple - (x, y)

    particles = setParticles(particles)    
    drawParticles(particles)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    particles = []

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        left, middle, right = pygame.mouse.get_pressed()

        drawWindow(left, particles)

main()