import board
import displayio
import framebufferio
import rgbmatrix
import time


displayio.release_displays()

map = [
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0],
    [0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,5,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,3,0,0,5,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,3,5,0,0,0,0,0,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,5,5,5,3,0,0,0,0,0,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,5,0,0,0,3,0,0,0,0,0,0,0,0,0,0],
    [4,4,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,5,5,5,0,3,0,0,0,0,0,0,0,0,0,0],
    [0,4,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,5,0,3,0,0,0,0,0,0,0,0,0,6],
    [0,4,4,0,0,0,0,0,6,6,6,6,6,3,6,6,6,0,0,5,0,3,0,0,0,0,0,0,0,0,6,0],
    [0,0,4,4,0,0,0,0,6,4,4,4,4,3,4,4,6,0,1,5,0,3,0,0,0,0,0,0,0,6,0,0],
    [0,0,0,4,4,0,0,0,6,4,2,2,2,3,2,4,6,0,1,5,0,3,0,0,0,0,0,0,6,0,0,0],
    [0,6,6,6,4,6,6,6,6,4,2,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,6,0,0,0,0],
    [0,0,0,0,0,4,4,4,4,4,2,0,0,0,2,4,6,0,1,5,0,0,6,6,6,6,6,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,4,6,6,6,6,6,6,6,4,4,4,4,4,4,4,4,4],
    [0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,4,4,4,4,4,4,4,4,4,2,2,2,2,2,2,2,2],
    [0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,1,1,1,5,5,5,5,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,5,5,5,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

locations = {
    "Glenmont":((0,16),),
    "Wheaton":((1,16),),
    "Forest Glen":((2,16),),
    "Silver Spring":((3,16),),
    "Takoma":((5,17),),
    "Fort Totten":((7,19),(7,20),(8,19),(8,20)),
    "Brookland-CUA":((11,21),),
    "Rhode Island Ave":((12,21),),
    "NoMa-Gallaudet U":((13,21),),
    "Union Station":((14,21),),
    "Judiciary Sq":((15,20),),
    "Gallery Place":((15,18),(15,19)),
    "Metro Center":((15,14),(15,15),(15,16)),
    "Farragut North":((11,13),),
    "Dupont Circle":((10,12),),
    "Woodley Park":((9,11),),
    "Cleveland Park":((8,10),),
    "Van Ness-UDC":((8,9),),
    "Tenleytown-AU":((8,8),),
    "Friendship Heights":((7,7),),
    "Bethesda":((6,6),),
    "Medical Center":((5,5),),
    "Grosvenor-Strathmore":((4,4),),
    "North Bethesda":((3,3),),
    "Twinbrook":((2,2),),
    "Rockville":((1,1),),
    "Shady Grove":((0,0),),
    "Greenbelt":((3,24),),
    "College Park-U of Md":((4,23),),
    "Hyattsville Crossing":((5,22),),
    "West Hyattsville":((6,21),),
    "Georgia Ave-Petworth":((8,18),),
    "Columbia Heights":((9,17),),
    "U St":((10,18),),
    "Shaw-Howard U":((11,19),),
    "Mt Vernon Sq":((13,18),(13,19)),
    "Archives":((16,18),(16,19)),
    "L'Enfant Plaza":((17,18),(17,19),(18,18),(18,19),(19,18),(19,19)),
    "Waterfront":((21,20),),
    "Navy Yard-Ballpark":((21,21),),
    "Anacostia":((21,22),),
    "Congress Heights":((22,23),),
    "Southern Ave":((23,24),),
    "Naylor Rd":((23,25),),
    "Suitland":((24,26),),
    "Branch Ave":((25,27),),
    "Ashburn":((8,0),),
    "Loudoun Gateway":((9,0),),
    "Washington Dulles International Airport":((10,0),),
    "Innovation Center":((10,1),),
    "Herndon":((11,1),),
    "Reston Town Center":((12,1),),
    "Wiehle-Reston East":((12,2),),
    "Spring Hill":((13,2),),
    "Greensboro":((13,3),),
    "Tysons":((14,3),),
    "McLean":((14,4),),
    "East Falls Church":((15,4),),
    "Ballston-MU":((15,5),(16,5)),
    "Virginia Sq-GMU":((15,6),(16,6)),
    "Clarendon":((15,7),(16,7)),
    "Court House":((15,8),(16,8)),
    "Rosslyn":((15,8),(15,9),(15,10)),
    "Foggy Bottom-GWU":((12,11),(13,11),(14,11)),
    "Farragut West":((12,12),(13,12),(14,12)),
    "McPherson Square":((12,14),(13,14),(14,14)),
    "Federal Triangle":((16,14),(16,15),(16,16)),
    "Smithsonian":((19,14),(18,15),(17,16)),
    "Federal Center SW":((17,20),(18,20),(19,20)),
    "Capitol South":((17,21),(18,21),(19,21)),
    "Eastern Market":((17,22),(18,23),(19,24)),
    "Potomac Ave":((16,22),(17,23),(18,24)),
    "Stadium-Armory":((16,25),(17,25),(18,25)),
    "Benning Rd":((17,27),(18,27)),
    "Capitol Heights":((17,28),(18,28)),
    "Addison Rd":((17,29),(18,29)),
    "Morgan Blvd":((17,30),(18,30)),
    "Downtown Largo":((17,31),(18,31)),
    "Vienna":((15,1),),
    "Dunn Loring":((15,2),),
    "West Falls Church":((15,3),),
    "Minnesota Ave":((15,27),),
    "Deanwood":((14,28),),
    "Cheverly":((13,29),),
    "Landover":((12,30),),
    "New Carrollton":((11,31),),
    "Pentagon":((22,13),(22,14)),
    "Pentagon City":((23,13),(23,14)),
    "Crystal City":((24,14),(25,13)),
    "Ronald Reagan Washington National Airport":
}
def makeLines(bitmap):
    for x in range(32):
        for y in range(32):
            bitmap[x,y] = map[y][x]

def displayPoint(bitmap, point):
    bitmap[point[1],point[0]] = 7

def displayStation(bitmap, station):
    for point in station:
        displayPoint(bitmap, point)

def displayStations(bitmap, locations):
    for location in locations.values():
        displayStation(bitmap,location)


matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=12,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.A5, board.A4, board.A3, board.A2],
    clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1)
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)
SCALE = 1
bitmap = displayio.Bitmap(display.width,display.height,8)
pallete = displayio.Palette(8)
tilegrid = displayio.TileGrid(bitmap,pixel_shader=pallete)
group = displayio.Group(scale=SCALE)
group.append(tilegrid)
display.root_group = group
#black
pallete[0] = 0x000000
#metro yellow
pallete[1] = 0xffd200
#metro blue
pallete[2] = 0x0076c0
#metro red
pallete[3] = 0xe31837
#metro silver
pallete[4] = 0xa1a2a1
#metro green
pallete[5] = 0x00a94f
#metro orange
pallete[6] = 0xf7941e
#white
pallete[7] = 0xffffff

display.auto_refresh = True

makeLines(bitmap)
displayStations(bitmap,locations)