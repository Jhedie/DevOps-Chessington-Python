from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, Any, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

    def to_json(self) -> dict[str, Any]:
        return {
            "piece": self.__class__.__name__,
            "player": self.player._name_.lower()
        }

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board: Board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        if self.player == Player.BLACK:
            moves = []
            # square_in_left_diagonal = Square.at(current_square.row - 1, current_square.col - 1)
            # square_in_right_diagonal = Square.at(current_square.row - 1, current_square.col + 1)
            if current_square.row == 0:
                return moves
            square_in_front = Square.at(current_square.row - 1, current_square.col)
            if board.get_piece(square_in_front) is None:
                moves.append(square_in_front)
                if current_square.row == 6:
                    second_square_in_front = Square.at(current_square.row - 2, current_square.col)
                    if board.get_piece(second_square_in_front) is None:
                        moves.append(second_square_in_front)
            # Check diagonal captures
            for col_offset in [-1, 1]:  # Left and right diagonals
                diagonal_square = Square.at(current_square.row - 1, current_square.col + col_offset)
                piece = board.get_piece(diagonal_square)
                if piece is not None and piece.player != self.player:
                    moves.append(diagonal_square)
            # if ((board.get_piece(square_in_left_diagonal) != None) and (board.get_piece(square_in_right_diagonal) == None)):
            #     if board.get_piece(square_in_left_diagonal).player != self.player:
            #         return [square_in_left_diagonal]
            # if ((board.get_piece(square_in_left_diagonal) == None) and (board.get_piece(square_in_right_diagonal) != None)):
            #     if board.get_piece(square_in_right_diagonal).player != self.player:
            #         return [square_in_right_diagonal]
            # if ((board.get_piece(square_in_left_diagonal) != None) and (board.get_piece(square_in_right_diagonal) != None)):
            #     if board.get_piece(square_in_left_diagonal).player != self.player and board.get_piece(square_in_right_diagonal).player != self.player:
            #         return [square_in_left_diagonal, square_in_right_diagonal]

        else:
            moves = []
            # square_in_left_diagonal = Square.at(current_square.row + 1, current_square.col - 1)
            # square_in_right_diagonal = Square.at(current_square.row + 1, current_square.col + 1)
            if current_square.row == 7:
                return moves
            square_in_front = Square.at(current_square.row + 1, current_square.col)
            if board.get_piece(square_in_front) is None:
                moves.append(square_in_front)
                if current_square.row == 1:
                    second_square_in_front = Square.at(current_square.row + 2, current_square.col)
                    if board.get_piece(second_square_in_front) is None:
                        moves.append(second_square_in_front)
            for col_offset in [-1, 1]:
                diagonal_square = Square.at(current_square.row + 1, current_square.col + col_offset)
                piece = board.get_piece(diagonal_square)
                if piece is not None and piece.player != self.player:
                    moves.append(diagonal_square)
            # if ((board.get_piece(square_in_left_diagonal) != None) and (board.get_piece(square_in_right_diagonal) == None)):
            #     if board.get_piece(square_in_left_diagonal).player != self.player:
            #         return [square_in_left_diagonal]
            # if ((board.get_piece(square_in_left_diagonal) == None) and (board.get_piece(square_in_right_diagonal) != None)):
            #     if board.get_piece(square_in_right_diagonal).player != self.player:
            #         return [square_in_right_diagonal]
            # if ((board.get_piece(square_in_left_diagonal) != None) and (board.get_piece(square_in_right_diagonal) != None)):
            #     if board.get_piece(square_in_left_diagonal).player != self.player and board.get_piece(square_in_right_diagonal).player != self.player:
            #         return [square_in_left_diagonal, square_in_right_diagonal]
        return moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []
