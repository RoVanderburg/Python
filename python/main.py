import sys, pygame, time, random
pygame.init()

print("Loading Resources:")
def updt(total, progress):
    """
    Displays or updates a console progress bar.

    Original source: https://stackoverflow.com/a/15860757/1391441
    """
    barLength, status = 30, ""
    progress = float(progress) / float(total)

    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()
    
runs = 150
for run_num in range(runs):
    time.sleep(0.03)
    updt(runs, run_num + 1)

size = (1024, 576)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Brave New World")

bg_image = pygame.image.load("olivia.png").convert()
face = pygame.image.load("face.gif")
facerect = face.get_rect()
speed = [3,3]
facerect.x = 0
facerect.y = 0

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]  
 # Create an empty array
snow_list = []
 
# Loop 50 times and add a snow flake in a random x,y position
for i in range(150):
    x = random.randrange(0, 1024)
    y = random.randrange(0, 576)
    snow_list.append([x, y])
 
clock = pygame.time.Clock()

dead = False
while (dead == False):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      dead = True
  screen.blit(bg_image,[0,0])

  facerect = facerect.move(speed)
  if facerect.right > 1024 or facerect.left < 0:
  	speed[0] = -speed[0]
  if facerect.bottom > 576 or facerect.top <0:
   speed[1] = -speed[1]	
 
  for event in pygame.event.get():   # User did something
      if event.type == pygame.QUIT:  # If user clicked close
          done = True   # Flag that we are done so we exit this loop
 
    # Set the screen background
    #screen.fill(BLACK)
 
    # Process each snow flake in the list
  for i in range(len(snow_list)):
 
        # Draw the snow flake
      pygame.draw.circle(screen, WHITE, snow_list[i], 2)
 
        # Move the snow flake down one pixel 
      snow_list[i][1] += 1
 
        # If the snow flake has moved off the bottom of the screen
      if snow_list[i][1] > 576:
            # Reset it just above the top
          y = random.randrange(-50, -10)
          snow_list[i][1] = y
            # Give it a new x position
          x = random.randrange(0, 1024)
          snow_list[i][0] = x
 
    # Go ahead and update the screen with what we've drawn.
  clock.tick(40)
  screen.blit(face, facerect)
  pygame.display.flip()


 
# Loop until the user clicks the close button.
done = False
while not done:

 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit
  pygame.quit() 


print('finished')
