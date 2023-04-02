import pgzrun
TILE_SIZE = 60
WIDTH = 480
HEIGHT = 480
background = Actor("background")
board = [
    ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
    ]
def draw():
    screen.clear()
    background.draw()
    for row in range(len(board)):
        for column in range(len(board[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = board[row][column]
            screen.blit(tile, (x, y))
def update():
    pass

pgzrun.go()