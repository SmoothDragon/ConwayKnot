#!/usr/bin/env python3

import json
import solid
import numpy as np


def eisenstein(x,y):
    a = x-y/2
    b = y*np.sqrt(3)/2
    return a,b

r = .35

knot = json.load(open('conwayKnot.json'))
# print(knot)
# print(dir(solid))
ball = solid.sphere(r)

points = [[*eisenstein(*point[:2]), point[2]] for point in knot['path']]
# print(points)
balls = [solid.translate(p)(ball) for p in points]
bars = [solid.hull()(a,b) for a,b in zip(balls, balls[1:])]
result = solid.union()(*bars)
result = solid.scale(10)(result)

print(solid.scad_render(result))
