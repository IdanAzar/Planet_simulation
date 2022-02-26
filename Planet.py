import pygame
import constants as c
import math


class Planet:

    def __init__(self, x, y, radius, planet_color, planet_mass, is_sun, vel_y, planet_name):
        # set cords on screen
        self.x = x
        self.y = y

        # set planet properties
        self.radius = radius
        self.planet_color = planet_color
        self.planet_mass = planet_mass
        self.planet_name = planet_name

        # set planet velocity on y dir and x dir
        self.vel_x = 0
        self.vel_y = vel_y

        # make sure if planet is the sun or not
        self.is_sun = is_sun
        self.distance_to_sun = 0

        # track planet points orbit to draw his circular orbit
        self.planet_orbit = []

    def draw_planet(self, window):
        # we want to draw the planet proportional to the scale of distance and the center of the screen
        new_screen_x = self.x * c.SCALE + c.SCREEN_SIZE[0] / 2
        new_screen_y = self.y * c.SCALE + c.SCREEN_SIZE[1] / 2

        # draw the orbit of the planet
        # we want to start drawing an orbit when it has at least 3 or more points in it
        if len(self.planet_orbit) > 2:
            points_update_by_scale = []
            for point in self.planet_orbit:
                new_x, new_y = point
                new_x = new_x * c.SCALE + c.SCREEN_SIZE[0] / 2
                new_y = new_y * c.SCALE + c.SCREEN_SIZE[1] / 2
                points_update_by_scale.append((new_x, new_y))

            # draw the orbit by drawing the list of the update points
            pygame.draw.lines(window, self.planet_color, False, points_update_by_scale, 2)

        # draw planet on screen
        pygame.draw.circle(window, self.planet_color, (new_screen_x, new_screen_y), self.radius)

    def attraction(self, planet):
        # calculating the distance between 2 planets
        distance_x = planet.x - self.x
        distance_y = planet.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        # let's check if the other planet is the sun, if it is we will update the out planet distance to the sun
        if planet.is_sun:
            self.distance_to_sun = distance

        # calculating the force of attraction
        force = c.G * self.planet_mass * planet.planet_mass / distance ** 2

        # calculating the angle of the force using the distance in x dir and y dir, and we will call it theta
        theta = math.atan2(distance_y, distance_x)

        # calculating the force components in x dir and y dir
        force_y = force * math.sin(theta)
        force_x = force * math.cos(theta)

        # function returns force components in x dir and y dir
        return force_x, force_y

    def update_position(self, planets):
        # we will sum all the forces in x dir and y dir,
        # in order update our planet velocity and his position because of that

        # init total sum of forces to 0
        sigma_fx = sigma_fy = 0

        # loop through all planets in the solar system in order to sum up all the forces in x dir and y dir
        for planet in planets:
            # if the planet we are checking is the same planet in the list we will continue the loop
            if self == planet:
                continue
            # calculating the forces in both directions
            fx, fy = self.attraction(planet)

            # sum the forces to each direction
            sigma_fx += fx
            sigma_fy += fy

        # calculating each velocity components in x dir and y dir using the second law of Newton
        self.vel_x += sigma_fx / self.planet_mass * c.TIME_STEP
        self.vel_y += sigma_fy / self.planet_mass * c.TIME_STEP

        # calculating the new position (x, y) of the planet because of the change in the velocity vector
        self.x += self.vel_x * c.TIME_STEP
        self.y += self.vel_y * c.TIME_STEP

        # append the new position to the orbit of the planet
        self.planet_orbit.append((self.x, self.y))
