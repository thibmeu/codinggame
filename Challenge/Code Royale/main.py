import sys
import math
from enum import Enum

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class Position:
    MIN_X = 0
    MIN_Y = 0
    MAX_X = 1920
    MAX_Y = 1000

    def __init__(self, _x, _y):
        self._x = _x
        self._y = _y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def _sanitize(self):
        self.x = min(max(self.x, MIN_X), MAX_X)
        self.y = min(max(self.y, MIN_Y), MAX_Y)

    def move(_direction, _range = 1):
        if _direction in Direction:
            self.__addition(_direction, _range)

    def distance(self, _position):
        return math.sqrt((self._x - _position.x)**2 + (self._y - _position.y)**2)


class OwnerType(Enum):
    NONE = -1
    ALLY = 0
    ENEMY = 1


class UnitType(Enum):
    QUEEN = -1
    KNIGHT = 0
    ARCHER = 1


class Unit:
    def __init__(self, *kwargs):
        self.position = Position(kwargs[0], kwargs[1])
        self.owner = OwnerType(kwargs[2])
        self.type = UnitType(kwargs[3])
        self.health = kwargs[4]


class Queen(Unit):
    def __init__(self, *kwargs):
        super().__init__(kwargs)
        self.gold = 0
        self.touchSite = -1


class Site:
    def __init__(self, *kwargs):
        self.id = kwargs[0]
        self.position = Position(kwargs[1], kwargs[2])
        self.radius = kwargs[3]


class StructureType(Enum):
    BARRACK = 2
    EMPTY = -1


class ProductionType(Enum):
    KNIGHT = 0
    ARCHER = 1


class Structure(Site):
    def __init__(self, *kwargs):
        site = kwargs[0]
        super().__init__(site.id, site.position.x, site.position.y, site.radius)
        self.ignored1 = kwargs[1]
        self.ignored2 = kwargs[2]
        self.structureType = StructureType(kwargs[3])
        self.owner = OwnerType(kwargs[4])
        self.timeout = kwargs[5]
        self.production = kwargs[6]


# Beginning of the main method

sites = {}

num_sites = int(input())
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    sites[site_id] = Site(site_id, x, y, radius)

# game loop
while True:
    structures = {}

    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        structures[site_id] = Structure(sites[site_id], ignore_1, ignore_2, structure_type, owner, param_1, param_2)

    units = []
    queen = None

    num_units = int(input())
    for i in range(num_units):
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        if unit_type == UnitType.QUEEN and owner == OwnerType.ALLY:
            queen = Queen(x, y, owner, unit_type, health, gold, touched_site)
        else:
            units.append(Unit(x, y, owner, unit_type, health))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # First line: A valid queen action
    # Second line: A set of training instructions
    print('WAIT')
    print('TRAIN')