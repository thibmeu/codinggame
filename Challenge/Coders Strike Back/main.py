import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
precThrust = 100
isBoost = True
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in
                                                                                               input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    thrust = int(precThrust * 2)
    if abs(next_checkpoint_angle) > 90:
        thrust = 0
    else:
        thrust = 100
    # thrust = 100*(math.cos(next_checkpoint_angle/400*math.pi)**4)
    print(next_checkpoint_dist, file=sys.stderr)

    if next_checkpoint_dist < 4000:
        thrust *= (next_checkpoint_dist / 4000) ** (0.75)

    thrust = 100 if thrust > 100 else abs(int(thrust))

    if (next_checkpoint_dist > 10000 or abs(next_checkpoint_angle) < 2) and isBoost:
        thrust = "BOOST"
        isBoost = False

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(next_checkpoint_x, next_checkpoint_y, thrust)

    precThrust = thrust if type(thrust) is int else 100
