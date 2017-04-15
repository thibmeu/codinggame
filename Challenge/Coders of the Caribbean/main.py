# TODO: Make the code vector friendly
#  Will be used in firing opponent and mining

import sys
import math


class Point:
    pass


class Point2D (Point):
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def __ne__(self, other):
        return not other or self.x != other.x or self.y != other.y

    def shift(self, x, y):
        self.x += x
        self.y += y

    def toCube(self):
        x = self.x - (self.y - (self.y & 1)) / 2
        z = self.y
        y = -x - z
        return Point3D(x, y, z)

    def __str__(self):
        return "".join([str(self.x), " ", str(self.y)])

class Point3D (Point):
    def __init__(self, x_init, y_init, z_init):
        self.x = x_init
        self.y = y_init
        self.z = z_init

    def shift(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def toOffset(self):
        return Point2D(self.x + (self.z - (self.z & 1)) / 2, self.z)

    def __str__(self):
        return "".join([str(self.x), " ", str(self.y), " ", str(self.z)])


def distance(a, b):
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)


def cubeDistance(a, b):
    return (abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) / 2


def offsetDistance(a, b):
    ac = a.toCube()
    bc = b.toCube()
    return cubeDistance(ac, bc)


class Entity:
    def __init__(self, id_init, position_init):
        self.id = id_init
        self.position = position_init

    def __ne__(self, other):
        return not other or self.id != other.id or self.position != other.position


class Entities:
    def __init__(self):
        self.entities = []

    def add(self, entity):
        self.entities.append(entity)

    def getEntitiesOfType(self, t):
        e = []
        for entity in self.entities:
            if isinstance(entity, t):
                e.append(entity)
        return e


class Ship (Entity):
    def __init__(self, id_init, pos_init, orientation_init, speed_init, rum_init, mine_init):
        super().__init__(id_init, pos_init)
        self.orientation = orientation_init
        self.speed = speed_init
        self.rum = rum_init
        self.mine = mine_init == 1

    def __str__(self):
        return "".join(["~~ SHIP: ",
                        "Id: ", str(self.id),
                        ", Position: ", str(self.position),
                        ", Orientation: ", str(self.orientation),
                        ", Speed: ", str(self.speed),
                        ", Rum: ", str(self.rum),
                        ", Controlled by: ", "ME" if self.mine else "OPPONENT",
                        " ~~"])

    def getNearestBarrel(self, barrels):
        minBarrel, minDist = None, 1000*1000
        for barrel in barrels:
            if offsetDistance(self.position, barrel.position) < minDist:
                minDist = offsetDistance(self.position, barrel.position)
                minBarrel = barrel
        return minBarrel

    def isMine(self):
        return self.mine


class Barrel (Entity):
    def __init__(self, id_init, pos_init, rum_init):
        super().__init__(id_init, pos_init)
        self.rum = rum_init

    def __str__(self):
        return "".join(["~~ BARREL: ",
                        "Id: ", str(self.id),
                        ", Position: ", str(self.position),
                        ", Rum: ", str(self.rum),
                        " ~~"])


class Cannonball (Entity):
        def __init__(self, id_init, pos_init, owner_init, turn_init):
            super().__init__(id_init, pos_init)
            self.owner = owner_init
            self.turn = turn_init

        def __str__(self):
            return "".join(["~~ CANNONBALL: ",
                            "Id: ", str(self.id),
                            ", Position: ", str(self.position),
                            ", Owner: ", str(self.owner),
                            ", Turn: ", str(self.turn),
                            " ~~"])


class Mine (Entity):
    def __str__(self):
        return "".join(["~~ MINE: ",
                        "Id: ", str(self.id),
                        ", Position: ", str(self.position),
                        " ~~"])

# game loop

precBarrel = None
mineCountdown = 0
while True:
    plan = {}  # current map
    my_ship_count = int(input())  # the number of remaining ships
    entity_count = int(input())  # the number of entities (e.g. ships, mines or cannonballs)

    entities = Entities()
    for _ in range(entity_count):
        entity_id, entity_type, x, y, arg_1, arg_2, arg_3, arg_4 = input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)

        # Add current entity
        entity = None
        position = Point2D(x, y)
        if entity_type == "SHIP":
            entity = Ship(entity_id, position, arg_1, arg_2, arg_3, arg_4)
        elif entity_type == "BARREL":
            entity = Barrel(entity_id, position, arg_1)
        elif entity_type == "CANNONBALL":
            entity = Cannonball(entity_id, position, arg_1, arg_2)
        elif entity_type == "MINE":
            entity = Mine(entity_id, position)

        if entity:
            entities.add(entity)
            plan[position] = entity

    # Get entities
    ships = entities.getEntitiesOfType(Ship)
    barrels = entities.getEntitiesOfType(Barrel)
    cannonballs = entities.getEntitiesOfType(Cannonball)
    mines = entities.getEntitiesOfType(Mine)

    for ship in ships:
        if not ship.isMine():
            continue
        # Going to the nearest barrel
        # TODO: optimizing distance, opponent and rum quantity of barrel
        if not precBarrel or precBarrel.position not in plan:
            barrel = ship.getNearestBarrel(barrels)
        else:
            barrel = precBarrel
        print(barrel, file=sys.stderr)

        command = None

        if barrel and (barrel != precBarrel or ship.speed < 1):
            command = "MOVE " + str(barrel.position)
        elif mineCountdown == 0:
            command = "MINE"
            mineCountdown = 4
        else:
            command = "WAIT"

        # Print the command
        print(command)

        # Save current parameters
        precBarrel = barrel
        mineCountdown = mineCountdown-1 if mineCountdown > 0 else 0
