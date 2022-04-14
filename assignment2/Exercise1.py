import graphics
import game
win = graphics.GraphWin("Practical Example", 500, 500)
win.setBackground("white")
# Create game block at position x=250, y=250, size of 20 pixels and colour red
#block = game.GameBlock(250, 250, 20, 20, 'red', None, None, 0)
#block.draw(win)
# The following code moves the block dx (20) units in the x direction and
# dy (50) units in the y direction
#block.move(20, 50)
win.getMouse()
win.close()