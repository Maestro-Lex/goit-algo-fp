import tkinter as tk
from math import sqrt, sin, cos, pi
import time


def pifagor_tree(side: int, x1: int, y1: int, depth: int, colors: list, angle: float = 0):
    '''
    Побудова класичного дерева Піфагора
    '''
    if depth == 0:
        return
    canvas.update()
   
    # Побудова блоку дерева
    x2 = x1 + side * cos(angle)
    y2 = y1 + side * sin(angle)
    x3 = x2 + side * cos(angle - pi / 2)
    y3 = y2 + side * sin(angle - pi / 2)
    x4 = x1 + side * cos(angle - pi / 2)
    y4 = y1 + side * sin(angle - pi / 2)
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill = colors[depth - 1], width=1)

    new_side = side / sqrt(2)

    # Визначаємо перві координати натупних блоків
    left_x = x4
    left_y = y4
    right_x = x4 + new_side * sin(angle + pi / 4)
    right_y = y4 - new_side * cos(angle + pi / 4)

    time.sleep(0.2)
    pifagor_tree(new_side, left_x, left_y, depth - 1, colors, angle - pi / 4)
    pifagor_tree(new_side, right_x, right_y, depth - 1, colors, angle + pi / 4)
    

def det_colors(start: tuple, end: tuple, depth: int) -> list[str]:
    '''
    Створюємо палітру кольорів
    '''
    result = []
    for i in range(depth):
        t = i / (depth - 1)
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        result.append(f'#{r:02x}{g:02x}{b:02x}')
    return result


def main():
    side = int(input("Enter a size of root square of tree (default 150): ") or 150)
    depth = int(input("Enter a depth of pifagor algorithm (default 7): ") or 7)
    x = 900 / 2 - side / 2
    y = 700 - 50
    
    # Визначаємо палітру кольорів
    color_1 =  (139, 69, 19) # brown
    color_2 =  (34, 139, 34) # green
    colors = det_colors(color_2, color_1, depth)

    pifagor_tree(side, x, y, depth, colors)


if __name__ == "__main__":
    screen = tk.Tk()
    screen.title("Pifagor tree")
    screen.geometry("900x700+100+50")
    screen.resizable(False, False)
    canvas = tk.Canvas(screen, width=900, height=700)
    canvas.pack(fill = "both", expand = False)  

    main()

    screen.mainloop()