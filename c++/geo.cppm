export module geometry;

import math;
import std;

export namespace geometry {
    struct Circle {
        double radius;
        double area() const { return math::pi * math::square(radius); }
    };
}
