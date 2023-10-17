from replit import clear


from readchar import readchar
import time


class Coord:

  def __init__(self, x, y):
    self.x = x
    self.y = y


MapX = 10

MapY = 10

P = Coord(0, 0)

BaseMap = [["#"] * MapX for _ in range(MapY)]


def Render(Map):
  RenderMap = Map

  display = ""
  for a in range(MapY):
    for i in range(MapX):
      if a == P.y and i == P.x:
        display += "P"
      else:
        display += RenderMap[i][a]
    display += "\n"

  print(display)


def Run():
  clear()
  Render(BaseMap)
  while True:
    input = readchar()
    if input == "w":
      if P.y != 0:
        P.y -= 1
        Run()
    elif input == "d":
      if P.x != MapX:
        P.x += 1
        Run()
    elif input == "s":
      if P.y != MapY:
        P.y += 1
        Run()
    elif input == "a":
      if P.x != 0:
        P.x -= 1
        Run()
    time.sleep(.1)


Run()
