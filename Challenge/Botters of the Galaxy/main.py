import sys
import math
from enum import Enum


class Debugger:
    _index = 0

    def log(_message):
        print('+++++ {}: {}'.format(Debugger._index, _message), file=sys.stderr)


class Position:
    MIN_X = 0
    MIN_Y = 0
    MAX_X = 1920
    MAX_Y = 750

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
        self.x = min(max(self.x, MIN_X), MAX_X)
        self.y = min(max(self.y, MIN_Y), MAX_Y)

    def __addition(self, _position, _range):
        self._x += _position.x * _range
        self._y += _position.y * _range
        self._sanitize()

    def move(_direction, _range = 1):
        if _direction in Direction:
            self.__addition(_direction, _range)

    def distance(self, _position):
        return math.sqrt((self._x - _position.x)**2 + (self._y - _position.y)**2)


class Direction(Enum):
    LEFT = Position(-1, 0)
    RIGHT = Position(1, 0)
    UP = Position(0, 1)
    DOWN = Position(0, -1)


class Units(Enum):
    UNIT = 0
    HERO = 1
    TOWER = 2
    GROOT = 3

class Unit:
    def __init__(self, *kwargs):
        self.id = kwargs[0]
        self.team = kwargs[1]
        self.type = kwargs[2]
        self.position = Position(kwargs[3], kwargs[4])
        self.attack_range = kwargs[5]
        self.health = kwargs[6]
        self.max_health = kwargs[7]
        self.shield = kwargs[8]
        self.attack_damage = kwargs[9]
        self.movement_speed = kwargs[10]
        self.stun_duration = kwargs[11]
        self.gold = kwargs[12]
        self.hero = Hero(*kwargs[13:]) if self.type == 'HERO' else None

    # @self is in attack range of @_hero
    def inrange(self, _hero):
        Debugger.log(_hero.hero)
        return self.position.distance(_hero.position) <= _hero.hero.range


class AbstractHero:
    def __init__(self, _name, _health, _mana, _damage, _move_speed, _mana_regen, _range):
        self.name = _name
        self.health = _health
        self.mana = _mana
        self.damage = _damage
        self.move_speed = _move_speed
        self.mana_regen = _mana_regen
        self.range = _range


class Heroes(Enum):
    DEADPOOL = AbstractHero('Deadpool', 1380, 100, 80, 200, 1, 110)
    DOCTOR_STRANGE = AbstractHero('Doctor_Strange', 955, 300, 50, 200, 2, 245)
    HULK = AbstractHero('Hulk', 1450, 90, 80, 200, 1, 95)
    IRONMAN = AbstractHero('IronMan', 820, 200, 60, 200, 2, 270)
    VALKYRIE = AbstractHero('Valkyrie', 1400, 155, 65, 200, 2, 130)

    def hero(_hero_type):
        hero_type = _hero_type.lower()
        for hero in Heroes:
            if hero_type == hero.name.lower():
                return hero
        return 'Unknown'


class Hero(AbstractHero):
    def __init__(self, *kwargs):
        self.count_down_1 = kwargs[0]
        self.count_down_2 = kwargs[1]
        self.count_down_3 = kwargs[2]
        self.mana = kwargs[3]
        self.max_mana = kwargs[4]
        self.mana_regeneration = kwargs[5]
        hero = Heroes.hero(kwargs[6]).value
        self.visible = kwargs[7]
        self.items_owned = kwargs[8]
        super().__init__(hero.name, hero.health, hero.mana, hero.damage, hero.move_speed, hero.mana_regen, hero.range)

    def move(self, _direction):
        return self.position.move(_direction, self.move_speed)

class Actions(Enum):
    WAIT = 0
    MOVE = 1
    ATTACK = 2
    ATTACK_NEAREST = 3
    MOVE_ATTACK = 4
    BUY = 5
    SELL = 6


class Game:
    def __init__(self):
        self.turn = 0

    def perform(self, action):
        return True

    def next(self, _my_entities, _enemy_entities, _gold, _enemy_gold):
        self.turn += 1
        enemy_hero = None
        for entity in _enemy_entities:
            if entity.type == Units.HERO.name:
                enemy_hero = entity

        my_hero = None
        action = Actions.WAIT.name
        for entity in _my_entities:
            if entity.type == Units.HERO.name:
                my_hero = entity
                if enemy_hero.inrange(my_hero):
                    action = '{} {}'.format(Actions.ATTACK_NEAREST.name, Units.HERO.name)

        if action == Actions.WAIT.name:
            if self.turn <= 10:
                action = '{} {}'.format(Actions.MOVE.name, Position(0, 590))
            else:
                if my_hero.hero.range > enemy_hero.hero.range:
                    action = '{} {}'.format(Actions.ATTACK_NEAREST.name, Units.HERO.name)

        return action


my_team = int(input())
bush_and_spawn_point_count = int(input())  # useful from wood1, represents the number of bushes and the number of places where neutral units can spawn
for i in range(bush_and_spawn_point_count):
    # entity_type: BUSH, from wood1 it can also be SPAWN
    entity_type, x, y, radius = input().split()
    x = int(x)
    y = int(y)
    radius = int(radius)
item_count = int(input())  # useful from wood2
for i in range(item_count):
    # item_name: contains keywords such as BRONZE, SILVER and BLADE, BOOTS connected by "_" to help you sort easier
    # item_cost: BRONZE items have lowest cost, the most expensive items are LEGENDARY
    # damage: keyword BLADE is present if the most important item stat is damage
    # move_speed: keyword BOOTS is present if the most important item stat is moveSpeed
    # is_potion: 0 if it's not instantly consumed
    item_name, item_cost, damage, health, max_health, mana, max_mana, move_speed, mana_regeneration, is_potion = input().split()
    item_cost = int(item_cost)
    damage = int(damage)
    health = int(health)
    max_health = int(max_health)
    mana = int(mana)
    max_mana = int(max_mana)
    move_speed = int(move_speed)
    mana_regeneration = int(mana_regeneration)
    is_potion = int(is_potion)

# game loop
game = Game()
while True:
    gold = int(input())
    enemy_gold = int(input())
    round_type = int(input())  # a positive value will show the number of heroes that await a command
    entity_count = int(input())

    my_entities = []
    enemy_entities = []
    for i in range(entity_count):
        # unit_type: UNIT, HERO, TOWER, can also be GROOT from wood1
        # shield: useful in bronze
        # stun_duration: useful in bronze
        # count_down_1: all countDown and mana variables are useful starting in bronze
        # hero_type: DEADPOOL, VALKYRIE, DOCTOR_STRANGE, HULK, IRONMAN
        # is_visible: 0 if it isn't
        # items_owned: useful from wood1
        unit_id, team, unit_type, x, y, attack_range, health, max_health, shield, attack_damage, movement_speed, stun_duration, gold_value, count_down_1, count_down_2, count_down_3, mana, max_mana, mana_regeneration, hero_type, is_visible, items_owned = input().split()
        unit_id = int(unit_id)
        team = int(team)
        x = int(x)
        y = int(y)
        attack_range = int(attack_range)
        health = int(health)
        max_health = int(max_health)
        shield = int(shield)
        attack_damage = int(attack_damage)
        movement_speed = int(movement_speed)
        stun_duration = int(stun_duration)
        gold_value = int(gold_value)
        count_down_1 = int(count_down_1)
        count_down_2 = int(count_down_2)
        count_down_3 = int(count_down_3)
        mana = int(mana)
        max_mana = int(max_mana)
        mana_regeneration = int(mana_regeneration)
        is_visible = int(is_visible)
        items_owned = int(items_owned)

        entity = Unit(unit_id, team, unit_type, x, y, attack_range, health, max_health, shield, attack_damage, movement_speed, stun_duration, gold_value, count_down_1, count_down_2, count_down_3, mana, max_mana, mana_regeneration, hero_type, is_visible, items_owned)
        if entity.team == my_team:
            my_entities.append(entity)
        else:
            enemy_entities.append(entity)

    # If roundType has a negative value then you need to output a Hero name, such as "DEADPOOL" or "VALKYRIE".
    # Else you need to output roundType number of any valid action, such as "WAIT" or "ATTACK unitId"
    if round_type < 0:
        print(Heroes.VALKYRIE.name)
    else:
        print(game.next(my_entities, enemy_entities, gold, enemy_gold))
