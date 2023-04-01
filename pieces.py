class Piece():
    """
    Put description of the Piece class here
    """
    def __init__(self):
        # standard initiation of a piece 
        pass
        
    def is_valid_move(self):
        return False

    def is_white(self):
        pass

    def __str__(self):
        # replace the body and return a string with how you want your piece
        # to be printed as when `print([A Piece Object])` is called
        return ''
        
class Rook(Piece):
    def __init__(self, color):
        pass

    def is_valid_move(self, board, start, to):
        pass

class Knight(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class Bishop(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class Queen(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class King(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass
    
    def can_castle(self):
        pass

# Class to represent a pseudo pawn that can be taken when
# en passant is possible
class GhostPawn(Piece):
    def __init__(self, color):
        pass

    def is_valid_move(self):
        return False

class Pawn(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass