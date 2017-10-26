# Set the size of the window
WIDTH = 600
HEIGHT = 500

# Create the actors
mao = Actor('codemao')    # The spacecraft actor
mao.pos = WIDTH/2, HEIGHT/2  # The initial position of Codemao

# ---------------------------------------
# The draw function
def draw():
  screen.clear()
  mao.draw()

# ---------------------------------------
# The update function
def update():

  # If the cursor keys are pressed, then move
  # Codemao within the limits of the screen.
  if keyboard.left and mao.left > 2:
    mao.x -= 2
  if keyboard.right and mao.right < WIDTH+2:
    mao.x += 2
  if keyboard.down and mao.bottom < HEIGHT+2:
    mao.y += 2
  if keyboard.up and mao.top > 2:
    mao.y -= 2
  
  
