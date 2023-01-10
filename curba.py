import os
from geomdl import NURBS
from geomdl import utilities
from geomdl.visualization import VisMPL


def puncte_de_control_ponderi(n):
    a = []

    for index in range(n):
        print("punctul", index)
        x = float(input("x = "))
        y = float(input("y = "))
        w = float(input("w = "))
        a.append((x, y, w))

    return a



def main():
    n = 4
    puncte = puncte_de_control_ponderi(n)
    # !/usr/bin/env python
    # -*- coding: utf-8 -*-

    """
        Examples for the NURBS-Python Package
        Released under MIT License
        Developed by Onur Rauf Bingol (c) 2018
        3rd degree 3-dimensional Bezier curve
    """

    # Fix file path
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Create a 3D B-Spline curve instance (Bezier Curve)
    curve = NURBS.Curve()

    # Set up the Bezier curve
    curve.degree = 3
    curve.ctrlptsw = [[list(puncte_de_control_ponderi(0))], [list(puncte_de_control_ponderi(1))], [list(puncte_de_control_ponderi(2))],
                      [list(puncte_de_control_ponderi(3))]]

    # Auto-generate knot vector
    curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlptsw))

    # Set evaluation delta
    curve.sample_size = 40

    # Evaluate curve
    curve.evaluate()

    # Draw the control point polygon and the evaluated curve
    vis_comp = VisMPL.VisCurve2D()
    curve.vis = vis_comp

    # Don't pop up the plot window, instead save it as a PDF file
    curve.render()

    pass

main()