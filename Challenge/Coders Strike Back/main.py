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

    opponent_dist = math.sqrt((opponent_x - x) ** 2 + (opponent_y - y) ** 2)

    xc_x = next_checkpoint_x - x
    xc_y = next_checkpoint_y - y

    theta = next_checkpoint_angle * math.pi / 180
    m = xc_x * math.cos(theta) - xc_y * math.sin(theta)
    n = xc_x * math.sin(theta) + xc_y * math.cos(theta)

    a = (n / m) if abs(next_checkpoint_angle) < 10 else (xc_y / xc_x)
    b = y - a * x
    nx = next_checkpoint_x
    ny = a * nx + b

    if opponent_dist < 1000 and next_checkpoint_dist < 2000:
        print("-------", file=sys.stderr)
        alpha = 2
        if a * opponent_x + b < opponent_y:
            alpha = alpha
        else:
            alpha = 1 / alpha
        a *= alpha
        b = y - a * x
        ny = a * nx + b

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    thrust = precThrust
    if abs(next_checkpoint_angle) > 90:
        thrust = 0
    else:
        thrust += 100
    # thrust = 100*(math.cos(next_checkpoint_angle/400*math.pi)**4)

    if next_checkpoint_dist < 4000:
        thrust = 100 * (next_checkpoint_dist / 4000)**(1/3)

    print('y = %lf*x+%lf' % (a, b), 'angle', next_checkpoint_angle, file=sys.stderr)
    thrust = 100 if thrust > 100 else abs(int(thrust))

    if (next_checkpoint_dist > 5000 and abs(next_checkpoint_angle) == 0) and isBoost:
        thrust = "BOOST"
        isBoost = False

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print('dist:', next_checkpoint_dist, 'thrust:', thrust, file=sys.stderr)
    # print(next_checkpoint_x, next_checkpoint_y, thrust)
    nx, ny = int(nx), int(ny)
    print(nx, ny, thrust)

    precThrust = thrust if type(thrust) is int else 100
