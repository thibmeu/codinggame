import sys
import math
from enum import Enum

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class console:
    @staticmethod
    def log(message):
        print(message, file=sys.stderr)


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
        return '{} {}'.format(self.x, self.y)

    def _sanitize(self):
        self.x = min(max(self.x, Position.MIN_X), Position.MAX_X)
        self.y = min(max(self.y, Position.MIN_Y), Position.MAX_Y)

    def add(self, _position):
        self._x += _position.x
        self._y += _position.y

    def sub(self, _position):
        self._x -= _position.x
        self._y -= _position.y

    def mult(self, _scale):
        self._x *= _scale
        self._y *= _scale

    def distance(self, _position):
        return math.sqrt((self._x - _position.x)**2 + (self._y - _position.y)**2)

    def round(self):
        self._x = round(self._x)
        self._y = round(self._y)

    def move(self, _position, _max_distance):
        if self.distance(_position) <= _max_distance:
            return _position
        ab = Position(_position.x, _position.y)
        ab.sub(self)
        console.log('Reine: {}, Site: {}, Step: {}'.format(self, _position, ab))
        ab.mult(_max_distance / self.distance(_position))
        console.log('Reine: {}, Site: {}, Step: {}'.format(self, _position, ab))
        ab.add(self)
        ab.round()
        console.log('Reine: {}, Site: {}, Step: {}'.format(self, _position, ab))
        return ab


class Circle:
    def __init__(self, _centre, _radius):
        self.centre = Position(_centre.x, _centre.y)
        self.radius = _radius

    def distance(self, _circle):
        return self.centre.distance(_circle.centre) - (self.radius + _circle.radius)

    def touch(self, _circle):
        return self.distance(_circle) == 0

    def borders(self):
        return [
            Position(self.centre.x + self.radius, self.centre.y),
            Position(self.centre.x - self.radius, self.centre.y),
            Position(self.centre.x, self.centre.y + self.radius),
            Position(self.centre.x, self.centre.y - self.radius)
        ]


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
    radius = 30
    maxDistance = 60

    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.gold = kwargs[5]
        self.touchSite = kwargs[6]

    def to_circle(self):
        return Circle(self.position, Queen.radius)


class Site(Circle):
    def __init__(self, *kwargs):
        super().__init__(Position(kwargs[1], kwargs[2]), kwargs[3])
        self.id = kwargs[0]


class StructureType(Enum):
    EMPTY = -1
    TOWER = 1
    BARRACK = 2


class ProductionType(Enum):
    KNIGHT = 0
    ARCHER = 1


class Structure(Site):
    def __init__(self, *kwargs):
        site = kwargs[0]
        super().__init__(site.id, site.centre.x, site.centre.y, site.radius)
        self.ignored1 = kwargs[1]
        self.ignored2 = kwargs[2]
        self.structureType = StructureType(kwargs[3])
        self.owner = OwnerType(kwargs[4])
        self.timeout = kwargs[5]
        self.production = kwargs[6]


class Methods:
    @staticmethod
    def performQueenAction(queen, structures):
        print('---- {}'.format(queen.touchSite), file=sys.stderr)
        if queen.touchSite != -1:
            site = structures[queen.touchSite]
            if site.structureType == StructureType.EMPTY:
                print('BUILD {} BARRACKS-KNIGHT'.format(site.id))
                return

        owned = [structure_id for structure_id in structures if structures[structure_id].owner == OwnerType.ALLY]

        if len(owned) >= 2:
            origin = Position(Position.MIN_X, Position.MIN_Y)
            max_position = Position(Position.MAX_X, Position.MAX_Y)
            distanceOrigin = queen.position.distance(origin)
            distanceMax = queen.position.distance(max_position)

            if distanceOrigin < distanceMax:
                print('MOVE {}'.format(origin))
            else:
                print('MOVE {}'.format(max_position))

            return

        closest_site = Methods.closest_site(queen, structures)
        if closest_site:
            step = queen.position.move(closest_site.centre, queen.maxDistance)
            print('MOVE {} {}'.format(step.x, step.y))
        else:
            print('WAIT')

    @staticmethod
    def closest_site(queen, sites):
        site_distances = []
        for key in sites:
            site = sites[key]
            site_distances.append({'site_id': site.id, 'distance': site.distance(queen.to_circle())})

        site_distances.sort(key=(lambda x: x['distance']))
        for site in site_distances:
            if sites[site['site_id']].structureType == StructureType.EMPTY \
                    or sites[site['site_id']].owner == OwnerType.ENEMY:
                return sites[site['site_id']]

        # Happens if we control every site
        return None

    @staticmethod
    def perform_training(_structures, _gold, _ennemy):
        goldTurn = _gold

        toTrain = []
        for structure_id in _structures:
            structure = _structures[structure_id]
            if goldTurn < 80:
                break
            if structure.owner == OwnerType.ALLY and structure.structureType == StructureType.BARRACK and \
                    structure.timeout == 0:
                toTrain.append(structure_id)
                goldTurn -= 80

        toTrain.sort(key=(lambda structure_id: _structures[structure_id].centre.distance(_ennemy.position)))

        return [str(structure) for structure in toTrain]


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
        if unit_type == UnitType.QUEEN.value and owner == OwnerType.ALLY.value:
            queen = Queen(x, y, owner, unit_type, health, gold, touched_site)
        else:
            units.append(Unit(x, y, owner, unit_type, health))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # First line: A valid queen action
    # Second line: A set of training instructions
    Methods.performQueenAction(queen, structures)

    ennemy_queen = [unit for unit in units if (unit.type == UnitType.QUEEN and unit.owner == OwnerType.ENEMY)][0]
    toTrain = Methods.perform_training(structures, queen.gold, ennemy_queen)

    if len(toTrain) > 0:
        print('TRAIN ' + ' '.join(toTrain))
    else:
        print('TRAIN')