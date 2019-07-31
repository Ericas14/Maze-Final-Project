def setup():
    global sprites
    global maze
    size(600,600)
    sprite = []
    img1 = loadImage("empty.jpg")
    img2 = loadImage("smiley.jpg")
    img3 = loadImage("wall.jpg")
    img4 = loadImage("key.jpg")
    img5 = loadImage("lock.jpg")
    sprites = [ img1, img2, img3, img4, img5]
    maze = [
            [sprites[2],sprites[2],sprites[1],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2]]
            ]

def draw():
    global sprites  
    global maze  
    for row in range(len(maze)):
        for col in range(10):
            sprite = maze[row][col]
            image(sprite, col*30, row*30)
