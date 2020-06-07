import os, random, string, shutil
from time import sleep
from colorama import Fore, Style

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def rand_char():
  return random.choice(
          string.ascii_letters + string.digits + string.punctuation
        )

class Grid():
  def __init__(self, width, height):
    self.width, self.height = width, height
    self.grid = [[0 for y in range(self.height)] for x in range(self.width)]

  def add_droplets(self):
    num_to_add = random.randint(1, int(width / 10))
    for i in range(num_to_add):
      x = random.randint(0, self.width - 1)
      self.grid[x][0] = 5

  def update(self):
    for x in range(self.width):
      for y in reversed(range(1, self.height)):
        if(self.grid[x][y] > 0):
          self.grid[x][y] = self.grid[x][y] - 1
        elif(self.grid[x][y - 1] > 0):
          self.grid[x][y] = self.grid[x][y - 1]

    for x in range(self.width):
      if(self.grid[x][0] > 0):
        self.grid[x][0] = self.grid[x][0] - 1

  def row_to_string(self, y):
    r = ''
    for x in range(self.width):
      if(self.grid[x][y] == 0):
        r = r + ' '
      else:
        r = r + f'{Fore.GREEN}{rand_char()}{Style.RESET_ALL}'
    return r

  def print(self):
    for y in range(self.height):
      print(self.row_to_string(y))

if __name__ == '__main__':
  clear()

  width, height = shutil.get_terminal_size(fallback=(80, 24))
  grid = Grid(width, height)
  counter = 0

  while True:
    counter = (counter + 1) % 2

    if(counter == 0):
      grid.add_droplets()

    grid.update()
    grid.print()
    sleep(.5)
    clear()
