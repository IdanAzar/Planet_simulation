import pygame
import constants as c
from Planet import Planet


def initialize_window():
    pygame.init()

    # creating screen
    window = pygame.display.set_mode(c.SCREEN_SIZE)

    # name the screen
    pygame.display.set_caption(' Planet Simulation - By Idan Azar')

    return window


def creating_planets():
    # init planets
    planets = []

    # create "planet" Sun
    sun = Planet(0, 0, 30, c.YELLOW, c.SUN_MASS, True, 0, "Sun")
    planets.append(sun)

    # create planet Earth
    earth = Planet(-1 * c.AU, 0, 16, c.BLUE, c.EARTH_MASS, False, 29.783 * 1000, "Earth")
    planets.append(earth)

    # create planet Mars
    mars = Planet(-1.524 * c.AU, 0, 12, c.RED, c.MARS_MASS, False, 24.077 * 1000, "Mars")
    planets.append(mars)

    # create planet Mercury
    mercury = Planet(0.387 * c.AU, 0, 8, c.DARK_GRAY, c.MERCURY_MASS, False, -47.4 * 1000, "Mercury")
    planets.append(mercury)

    # create planet Venus
    venus = Planet(0.723 * c.AU, 0, 14, c.WHITE, c.VENUS_MASS, False, -35.02 * 1000, "Venus")
    planets.append(venus)

    return planets


def simulation():
    # init window
    window = initialize_window()

    # creating clock for simulation
    clock = pygame.time.Clock()

    # set Simulation infinite loop
    run_simulation = True

    # creating planets for simulation
    sim_planets = creating_planets()

    while run_simulation:
        # clock ticks by max FPS
        clock.tick(c.FPS)

        # refresh screen by filling black color
        window.fill(c.BLACK)

        for event in pygame.event.get():
            # check for exit
            if event.type == pygame.QUIT:
                run_simulation = False

        # draw each planet on screen
        for planet in sim_planets:
            # move and update all planets position and velocity
            planet.update_position(sim_planets)

            # draw all planets on screen
            planet.draw_planet(window)

        # update window
        pygame.display.update()

    # end of simulation
    pygame.quit()


def main():
    simulation()


if __name__ == '__main__':
    main()
