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
black_castle = True
white_castle = True
#board = [
#    ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
#    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
#    ['__', '__', '__', '__', '__', '__', '__', '__'],
#    ['__', '__', '__', '__', '__', '__', '__', '__'],
#    ['__', '__', '__', '__', '__', '__', '__', '__'],
#    ['__', '__', '__', '__', '__', '__', '__', '__'],
#    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
#    ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
#    ]
board = [
    ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', '__', 'bp'],
    ['__', '__', '__', '__', '__', '__', 'bk', '__'],
    ['bp', '__', 'bp', '__', '__', '__', '__', '__'],
    ['__', 'wp', 'wq', 'wk', 'wn', '__', 'wb', '__'],
    ['__', '__', 'wp', '__', '__', 'bn', '__', '__'],
    ['__', '__', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wb', '__', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
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
    for take in takeable:
        take.draw()
    for piece in pieces:
        piece.draw()
    for squares in valid_moves:
        squares.draw()

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
    if piece.image == "wb":
        check_bishop_moves(piece,"b")
    if piece.image == "bb":
        check_bishop_moves(piece,"w")
    if piece.image == "wq":
        check_rook_moves(piece,"b")
        check_bishop_moves(piece,"b")
    if piece.image == "bq":
        check_rook_moves(piece,"w")
        check_bishop_moves(piece,"w")  
    if piece.image == "wp":
        check_pawn_moves(piece,"b")
    if piece.image == "bp":
        check_pawn_moves(piece,"w")
    if piece.image == "wn":
        check_knight_moves(piece,"b")
    if piece.image == "bn":
        check_knight_moves(piece,"w")
    if piece.image == "wk":
        check_king_moves(piece,"b")
    if piece.image == "bk":
        check_king_moves(piece,"w")

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
    #TODO: add castling

def check_bishop_moves(piece, op_colour):
    position = find_piece(piece)
    x, y = position
    x = int(x)
    y = int(y)
    # Check valid moves to the top-left
    for i, j in zip(range(x-1, -1, -1), range(y-1, -1, -1)):
        current_square = board[i][j]
        if current_square == "__":
            valid_moves.append(Actor(("moves"),(j*60+30,i*60+30)))
        elif current_square[0] == op_colour:
            takeable.append(Actor(("take"),(j*60+30,i*60+30)))
            break
        else:
            break

    # Check valid moves to the top-right
    for i, j in zip(range(x-1, -1, -1), range(y+1, 8)):
        current_square = board[i][j]
        if current_square == "__":
            valid_moves.append(Actor(("moves"),(j*60+30,i*60+30)))
        elif current_square[0] == op_colour:
            takeable.append(Actor(("take"),(j*60+30,i*60+30)))
            break
        else:
            break

    # Check valid moves to the bottom-left
    for i, j in zip(range(x+1, 8), range(y-1, -1, -1)):
        current_square = board[i][j]
        if current_square == "__":
            valid_moves.append(Actor(("moves"),(j*60+30,i*60+30)))
        elif current_square[0] == op_colour:
            takeable.append(Actor(("take"),(j*60+30,i*60+30)))
            break
        else:
            break

    # Check valid moves to the bottom-right
    for i, j in zip(range(x+1, 8), range(y+1, 8)):
        current_square = board[i][j]
        if current_square == "__":
            valid_moves.append(Actor(("moves"),(j*60+30,i*60+30)))
        elif current_square[0] == op_colour:
            takeable.append(Actor(("take"),(j*60+30,i*60+30)))
            break
        else:
            break

def check_pawn_moves(piece,op_colour):
    position = find_piece(piece)
    x, y = position
    x = int(x)
    y = int(y)

    #Check moves for white pawn
    if op_colour == "b":
        if board[x-1][y] == "__":
            valid_moves.append(Actor(("moves"),(y*60+30,(x-1)*60+30)))
        if y > 0:
            if board[x-1][y-1][0]=="b":
                takeable.append(Actor(("take"),((y-1)*60+30,(x-1)*60+30))) 
        if y < 7:
            if board[x-1][y+1][0]=="b":
                takeable.append(Actor(("take"),((y+1)*60+30,(x-1)*60+30))) 
        if x == 6 and board[x-2][y] == "__":
            valid_moves.append(Actor(("moves"),(y*60+30,(x-2)*60+30)))

    #Check moves for black pawn
    else:
        if board[x+1][y] == "__":
            valid_moves.append(Actor(("moves"),(y*60+30,(x+1)*60+30)))
        if y > 0:
            if board[x+1][y-1][0]=="w":
                takeable.append(Actor(("take"),((y-1)*60+30,(x+1)*60+30))) 
        if y < 7:
            if board[x+1][y+1][0]=="w":
                takeable.append(Actor(("take"),((y+1)*60+30,(x+1)*60+30))) 
        if x == 1 and board[x+2][y] == "__":
            valid_moves.append(Actor(("moves"),(y*60+30,(x+2)*60+30)))
    #TODO: add en passeunt rule
    #TODO: add promotion

def check_knight_moves(piece,op_colour):
    position = find_piece(piece)
    x, y = position
    x = int(x)
    y = int(y)
    #The different offsets for the knight movement
    knight_moves = [
        [ 2, 1],
        [ 2,-1],
        [ 1,-2],
        [ 1, 2],
        [-1, 2],
        [-1,-2],
        [-2, 1],
        [-2,-1]]
    for i in range(len(knight_moves)):
        new_x = x + knight_moves[i][1]
        new_y = y + knight_moves[i][0]
        if new_x<0 or new_x>7 or new_y<0 or new_y>7:
            continue
        if board[new_x][new_y][0] == op_colour:
            takeable.append(Actor(("take"),(new_y*60+30,new_x*60+30))) 
        elif board[new_x][new_y] == "__":
            valid_moves.append(Actor(("moves"),(new_y*60+30,new_x*60+30)))

def check_king_moves(piece,op_colour):
    position = find_piece(piece)
    x, y = position
    x = int(x)
    y = int(y)
    #Check squares around king
    for i in range(-1,2):
        for j in range(-1,2):
            new_x = x + i
            new_y = y + j
            if new_x<0 or new_x>7 or new_y<0 or new_y>7 or(i==0 and j==0):
                continue
            if board[new_x][new_y][0] == op_colour:
                takeable.append(Actor(("take"),(new_y*60+30,new_x*60+30))) 
            elif board[new_x][new_y] == "__":
                valid_moves.append(Actor(("moves"),(new_y*60+30,new_x*60+30)))
    #TODO: add castling
            
pgzrun.go()