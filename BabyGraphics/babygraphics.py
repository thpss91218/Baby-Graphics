"""
File: babygraphics.py
Name: Tina Tsai
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    drawing_size = width - 2*GRAPH_MARGIN_SIZE
    line_space = drawing_size / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * line_space
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # draw the top and bottom horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    # draw the vertical lines
    for year in YEARS:
        year_index = YEARS.index(year)
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    rank_space = (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)/(MAX_RANK-1)

    for name in lookup_names:
        xy_coordinate = []
        for year in YEARS:
            year_index = YEARS.index(year)
            year = str(year)
            x = get_x_coordinate(CANVAS_WIDTH, year_index)
            xy_coordinate.append(x)
            if year in name_data[name]:
                rank = name_data[name][year]
                # calculate the height of y
                y = GRAPH_MARGIN_SIZE + (int(rank)-1) * rank_space
            else:
                rank = '*'
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            xy_coordinate.append(y)
            # color will be assigned according to the order passed in
            color_loc = lookup_names.index(name) % len(COLORS)
            canvas.create_text(x + TEXT_DX, y, text=name + " " + rank, anchor=tkinter.SW, fill = COLORS[color_loc])
            # when two coordinates stored, clear first coordinate and draw a line in between
            if len(xy_coordinate) == 4:
                canvas.create_line(xy_coordinate[0], xy_coordinate[1], xy_coordinate[2], xy_coordinate[3], width = LINE_WIDTH, fill = COLORS[color_loc])
                xy_coordinate.pop(0)
                xy_coordinate.pop(0)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
