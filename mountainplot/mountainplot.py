from math import sqrt
from collections import namedtuple
from statistics import mean

from shapely.geometry import Polygon, MultiPolygon

Mountain = namedtuple(
    'Mountain', ['name', 'height', 'level', 'color', 'text_color'])


def mountainplot(ax, mountains):
    average_height = mean([m.height for m in mountains])
    space_between = average_height / 10.0
    text_space = average_height / 20.0
    begin_x = 0
    for mountain in mountains:
        width = golden_ration(mountain.height)
        polygon = get_triangle(begin_x=begin_x,
                               height=mountain.height, width=width)
        trapez = get_trapez_in_triangle(
            begin_x=begin_x, height=mountain.height, width=width, percentage=mountain.level)
        ax.plot(*polygon.exterior.xy, color=mountain.color)
        ax.fill(*trapez.exterior.xy, color=mountain.color)
        middle = begin_x + (width / 2.0)
        ax.text(middle, text_space, mountain.name, color=mountain.text_color,
                fontweight='bold', rotation=90, ha='center', fontsize='large')
        begin_x += width + space_between


def golden_ration(value):
    return value * 0.618


def get_triangle(begin_x=0.0, height=2.0, width=2.0):
    polygon = Polygon(
        [(begin_x, 0.0), (begin_x + (width / 2.0), height), (begin_x + width, 0.0), ])
    return polygon


def get_point_on_line(point1, point2, percentage):
    d = sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    d2 = d * percentage
    top_x = point1[0] - ((d2*(point1[0]-point2[0]))/d)
    top_y = point1[1] - ((d2*(point1[1]-point2[1]))/d)
    return (top_x, top_y)


def get_trapez_in_triangle(begin_x=0.0, height=2.0, width=2.0, percentage=0.5):
    left = (begin_x, 0.0)
    right = (begin_x + width, 0.0)
    top = (begin_x + (width / 2.0), height)
    left_top = get_point_on_line(left, top, percentage)
    right_top = get_point_on_line(right, top, percentage)
    polygon = Polygon([left, left_top, right_top, right])
    return polygon
