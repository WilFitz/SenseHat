from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
maze = [[r,r,r,r,r,r,r,r],
        [r,b,r,b,b,b,b,r],
        [r,b,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,r,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,r,r,r,r,r]]

game_over = False

marble = w
maze[1][1] = marble
sense.set_pixels(sum(maze,[]))
def move_marble(pitch, roll, x, y):
  new_x = x
  new_y = y
  if 1 < pitch < 179:
    new_x -= 1

while game.over == False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = 0["roll"]
    x,y = move_marble(pitch,roll,x,y,)
    maze[x][y] = w
    sense.set_pixels(sum(maze,[]))
    
                    
