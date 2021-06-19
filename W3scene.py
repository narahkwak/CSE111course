import tkinter as tk
import math

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    #background
    sky_background(canvas, 0, 0, 800, 400)
    ground_background(canvas, 0, 400, 800, 600)
    house_brick(canvas, 50, 200, 250, 400)
    draw_window(canvas, 60, 220, 110, 270)
    draw_garage(canvas, 270, 270, 380, 400)
    draw_fence(canvas,scene_left, 350, scene_right, 400, 15)
    draw_fence_2(canvas,0, 350, 800, 400, 15)

    tree_center = scene_left + 500
    tree_top = scene_top + 300
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 300
    tree_top = scene_top + 300
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 400
    tree_top = scene_top + 250
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 600
    tree_top = scene_top + 250
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 700
    tree_top = scene_top + 300
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    drawn_sun(canvas, 100, 50)
   
    #draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    draw_cloud(canvas,250,100,400,180)
    draw_cloud(canvas,320,50,450,150)
    draw_cloud(canvas,350,100,500,180)
    draw_cloud(canvas,620,100,780,180)
    draw_cloud(canvas,650,130,800,200)
    draw_cloud(canvas,560,120,710,190)
    

    
# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

#draw house
def house_brick(canvas, top_left, bottom_left, top_right, bottom_right):
    canvas.create_rectangle(top_left, bottom_left, top_right, bottom_right,  fill = 'red4', width = False)
    canvas.create_rectangle(top_left+200, bottom_left + 50, top_right+150, bottom_right,  fill = 'red4', width = False)
    canvas.create_rectangle(top_left+60, bottom_left+100, top_right-60, bottom_right,  fill = 'goldenrod', width = 1)

def draw_window(canvas, top_left, bottom_left, top_right, bottom_right):
    canvas.create_rectangle(top_left, bottom_left, top_right, bottom_right,  fill = 'gold2', width = 1)
    canvas.create_rectangle(top_left+60, bottom_left, top_right+60, bottom_right,  fill = 'gold2', width = 1)
    canvas.create_rectangle(top_left+120, bottom_left, top_right+120, bottom_right,  fill = 'gold2', width = 1)

def draw_garage(canvas, top_left, bottom_left, top_right, bottom_right):
    canvas.create_rectangle(top_left, bottom_left, top_right, bottom_right,  fill = 'coral1', width = 1)

#the ground 
def ground_background(canvas, top_left, bottom_left, top_right, bottom_right):
    canvas.create_rectangle(top_left, bottom_left, top_right, bottom_right,  fill = 'seaGreen', width = False)

#put in the background
def sky_background(canvas, top_left, bottom_left, top_right, bottom_right):
     sky_width = 500
     sky_height = 300
     canvas.create_rectangle(top_left, bottom_left, top_right, bottom_right,  fill = 'lightBlue1', width = False)

#draw sun
def drawn_sun(canvas, sun_left, sun_top):
    sun_width = 100
    sun_height = 100
    ray_length = 100
    ray_width = 3
    ray_count = 10

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)
    

    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill = "#FFF7B4", width = False)

    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, fill = "#FFF7B4", width = ray_width )

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

#draw_cloud
def draw_cloud(canvas, left, bottom, right, top):

     canvas.create_oval(left, bottom, right, top, fill="white" , width = False)



#draw_fence
def draw_fence(canvas,left, top, right,bottom, grid_spacing):
    grid_spacing = 30

    for i in range(0, 800, grid_spacing):
        canvas.create_line(i, top, i, bottom, fill = "burlywood4", width = 10)

def draw_fence_2(canvas,left, top, right,bottom, grid_spacing):
    grid_spacing = 15

    for i in range(350, 400, grid_spacing):
        canvas.create_line(left, i, right, i,  fill = "burlywood4", width = 5)


    
def draw_grid(canvas,left, top, right,bottom, grid_spacing):
    text_horizontal_margin = 20
    text_vertical_margin = 10
    #draw horizontal
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i, text=f"{i}")
    #draw vertical
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f"{i}")

# Call the main function so that
# this program will start executing.
main()