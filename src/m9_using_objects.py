"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Sam Alvares.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------

    width = 400
    height = 400
    window = rg.RoseWindow(width, height)
    center_point1 = rg.Point(100,200)
    center_point2 = rg.Point(300, 200)
    radius1 = 10
    radius2 = 30
    circle1 = rg.Circle(center_point1, radius1)
    circle2 = rg.Circle(center_point2, radius2)
    circle2.fill_color = 'orange'
    circle2.attach_to(window)
    circle1.attach_to(window)

    window.render()

    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    width = 400
    height = 400
    window = rg.RoseWindow(width, height)

    center_point = rg.Point(100, 200)
    radius = 30
    circle = rg.Circle(center_point, radius)
    ccol = 'blue'
    circle.fill_color = ccol
    cthick = 2
    circle.outline_thickness = cthick
    circle.attach_to(window)
    print(cthick)
    print(ccol)
    print(center_point)
    print(center_point.x)
    print(center_point.y)


    p1 = rg.Point(200,300)
    p2 = rg.Point(300,100)
    rectangle = rg.Rectangle(p1,p2)
    rectangle.attach_to(window)
    rthick=1
    rectangle.outline_thickness = rthick
    rect_center=rectangle.get_center()
    print(rthick)
    print(None)
    print(rectangle.get_center())
    print(rect_center.x)
    print(rect_center.y)


    window.render()

    window.close_on_mouse_click()

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.

    width = 400
    height = 400
    window = rg.RoseWindow(width, height)
    line1 = rg.Line(rg.Point(100,300),rg.Point(200,100))
    line1.thickness = 3
    mid1=line1.get_midpoint()
    line1.attach_to(window)
    print(mid1)
    print(mid1.x)
    print(mid1.y)

    line2 = rg.Line(rg.Point(200, 300), rg.Point(300, 100))
    mid2 = line2.get_midpoint()
    line2.attach_to(window)
    print(mid2)
    print(mid2.x)
    print(mid2.y)

    window.render()

    window.close_on_mouse_click()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
