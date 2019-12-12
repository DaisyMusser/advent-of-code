# day 12: tracking the moons
import math

def file_to_string(file_name):
    locations = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:         # a little bit of error catching
                break
            locations.append(line)
    return locations


def int_maker(list_of_strings):
    x = ''
    for string in list_of_strings:
        x += string
    return int(x)


def formatter(locations):
    formatted_loc = []
    for i in range(4):
        x_start = (locations[i].index('x')) + 2
        dummy = []
        for ii in range(10):
            x = locations[i][x_start + ii]
            if x == ',':
                break
            dummy.append(x)
        x_value = int_maker(dummy)

        y_start = (locations[i].index('y')) + 2
        dummy = []
        for ii in range(100):
            x = locations[i][y_start + ii]
            if x == ',':
                break
            dummy.append(x)
        y_value = int_maker(dummy)

        z_start = (locations[i].index('z')) + 2
        dummy = []
        for ii in range(100):
            x = locations[i][z_start + ii]
            if x == '>':
                break
            dummy.append(x)
        z_value = int_maker(dummy)

        formatted_loc.append([x_value, y_value, z_value])
    return formatted_loc


class JupMoon(object):
    def __init__(self, loc):
        self.loc = loc
        self.x = loc[0]
        self.y = loc[1]
        self.z = loc[2]
        self.velocity = [0, 0, 0]  # does velocity need to be reset every time step? edit: no
        return

    def apply_gravity(self, moon_one, moon_two, moon_three):   # pass in loc of other three moons
        for i in range(3):
            if self.loc[i] > moon_one[i]:       # rel one
                self.velocity[i] -= 1
            elif self.loc[i] < moon_one[i]:
                self.velocity[i] += 1

            if self.loc[i] > moon_two[i]:       # rel two
                self.velocity[i] -= 1
            elif self.loc[i] < moon_two[i]:
                self.velocity[i] += 1

            if self.loc[i] > moon_three[i]:     # rel three
                self.velocity[i] -= 1
            elif self.loc[i] < moon_three[i]:
                self.velocity[i] += 1
        return

    def apply_velocity(self):
        for i in range(3):
            self.loc[i] += self.velocity[i]
        # self.velocity = [0, 0, 0]      # resets velocity for next gav calc
        return

    def calc_total_energy(self):
        kinetic = abs(self.loc[0]) + abs(self.loc[1]) + abs(self.loc[2])
        potential = abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])
        return kinetic + potential


# answers part one
def run_one(time_steps, locations):
    io = JupMoon(locations[0])
    europa = JupMoon(locations[1])
    ganymede = JupMoon(locations[2])
    callisto = JupMoon(locations[3])
    # print('After 0 steps:\npos=<', io.x, ', ', io.y, ', ', io.z, '>, ', 'vel=<', io.velocity[0], end='')
    # print(', ', io.velocity[1], ', ', io.velocity[2], '>')
    # print('pos = < ', europa.x, ', ', europa.y, ', ', europa.z, ' >, ', 'vel = < ', europa.velocity[0], end='')
    # print(', ', europa.velocity[1], ', ', europa.velocity[2], '>')
    # print('pos = < ', ganymede.x, ', ', ganymede.y, ', ', ganymede.z, ' >, ', 'vel = < ', ganymede.velocity[0], end='')
    # print(', ', ganymede.velocity[1], ', ', ganymede.velocity[2], '>')
    # print('pos = < ', callisto.x, ', ', callisto.y, ', ', callisto.z, ' >, ', 'vel = < ', callisto.velocity[0], end='')
    # print(', ', callisto.velocity[1], ', ', callisto.velocity[2], '>')
    for step in range(time_steps):
        print('step: ', step)
        print('  io velocity: ', io.velocity)
        io.apply_gravity(europa.loc, ganymede.loc, callisto.loc)
        europa.apply_gravity(io.loc, ganymede.loc, callisto.loc)
        ganymede.apply_gravity(io.loc, europa.loc, callisto.loc)
        callisto.apply_gravity(io.loc, europa.loc, ganymede.loc)
        print('    new io velocity: ', io.velocity)

        print('      io loc: ', io.loc)
        io.apply_velocity()
        europa.apply_velocity()
        ganymede.apply_velocity()
        callisto.apply_velocity()
        print('        new io loc: ', io.loc)

        # print('After ', step, ' steps:\npos=<', io.x, ', ', io.y, ', ', io.z, '>, ', 'vel=<', io.velocity[0], end='')
        # print(', ', io.velocity[1], ', ', io.velocity[2], '>')
        # print('pos=<', europa.x, ', ', europa.y, ', ', europa.z, '>, ', 'vel=<', europa.velocity[0], end='')
        # print(', ', europa.velocity[1], ', ', europa.velocity[2], '>')
        # print('pos=<', ganymede.x, ', ', ganymede.y, ', ', ganymede.z, '>, ', 'vel=<', ganymede.velocity[0],
        #      end='')
        # print(', ', ganymede.velocity[1], ', ', ganymede.velocity[2], '>')
        # print('pos=<', callisto.x, ', ', callisto.y, ', ', callisto.z, '>, ', 'vel=<', callisto.velocity[0],
        #       end='')
        # print(', ', callisto.velocity[1], ', ', callisto.velocity[2], '>')
    total_total_energy = io.calc_total_energy() + europa.calc_total_energy() + ganymede.calc_total_energy() + callisto.calc_total_energy()
    return total_total_energy


# main program
locations = file_to_string('ten_steps.txt')    # change file name here
locations = formatter(locations)

answer = run_one(10, locations)                # change steps here
print(answer)


