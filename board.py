import pgzrun
TILE_SIZE = 60
WIDTH = 480
HEIGHT = 480
background = Actor("background")
highlight = Actor("__")
pieces = []
selected = 0
valid_moves = []
takeable = []
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
for row in range(len(board)):
    for column in range(len(board[row])):
        x = (column * TILE_SIZE)+30
        y = (row * TILE_SIZE)+30
        tile = board[row][column]
        piece=Actor((board[row][column]),(x,y))
        pieces.append(piece)

def move(piece,to):
    img=piece.image
    piece.image = "__"
    for i in pieces:
        if i.pos == to:
            i.image = img
def draw():
    screen.clear()
    background.draw()
    highlight.draw()
    for piece in pieces:
        piece.draw()
    for squares in valid_moves:
        squares.draw()
    for take in takeable:
        take.draw()
def on_mouse_down(pos, button):
    valid_moves.clear()
    takeable.clear()
    for piece in pieces:
        if button == mouse.LEFT and piece.collidepoint(pos):
            highlight.image = "--"
            highlight.x=piece.x
            highlight.y=piece.y
            selected = piece
            check_valid(piece)
            if piece.image == "__":
                highlight.image = "__"
                selected = 0

def find_piece(piece):
    x = int((piece.y - 30) / 60)
    y = int((piece.x - 30) / 60)
    return (x, y)

def check_valid(piece):
    if piece.image == "wr":
        check_rook_moves(piece,"b")
    if piece.image == "br":
        check_rook_moves(piece,"w")
    # Add other piece checks here

def check_rook_moves(piece,op_colour):
    position = find_piece(piece)
    x, y = position
    x = int(x)
    y = int(y)
    # Check valid moves to the left
    for i in range(y - 1, -1, -1):
        current_square = board[x][i]
        if current_square == "__":
            valid_moves.append(Actor(("moves"),(i*60+30,x*60+30)))
        elif current_square[0] == op_colour:
            takeable.append(Actor(("take"),(i*60+30,x*60+30)))
            break
        else:
            break
    # Check valid moves to the right
    for i in range(y + 1, 8):
        current_square = board[x][i]
        if current_square == "__":
            valid_moves.append(Actor(("moves"),(i*60+30,x*60+30)))
        elif current_square[0] == op_colour:
            takeable.append(Actor(("take"),(i*60+30,x*60+30)))
            break
        else:
            break
    # Check valid moves upwards
    for i in range(x - 1, -1, -1):
        current_square = board[i][y]
        if current_square == "__":
            valid_moves.append(Actor(("moves"),(y*60+30,i*60+30)))
        elif current_square[0] == op_colour:
            takeable.append(Actor(("take"),(y*60+30,i*60+30)))
            break
        else:
            break
    # Check valid moves downwards
    for i in range(x + 1, 8):
        current_square = board[i][y]
        if current_square == "__":
            valid_moves.append(Actor(("moves"),(y*60+30,i*60+30)))
        elif current_square[0] == op_colour:
            takeable.append(Actor(("take"),(y*60+30,i*60+30)))
            break
        else:
            break

pgzrun.go()