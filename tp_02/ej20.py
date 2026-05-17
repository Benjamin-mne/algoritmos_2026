# Consigna: Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from enum import Enum, auto
from common.Stack import Stack

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
    NORTHEAST = auto()
    NORTHWEST = auto()
    SOUTHEAST = auto()
    SOUTHWEST = auto()


class Robot:
    def __init__(self, initial_x: int = 0, initial_y: int = 0):
        self.current_coords = (initial_x, initial_y)
        self.route = Stack()

    def _apply_movement(self, steps: int, direction: Direction, x: int, y: int) -> tuple[int, int]:
        match direction:
            case Direction.NORTH:
                y += steps
            case Direction.SOUTH:
                y -= steps
            case Direction.EAST:
                x += steps
            case Direction.WEST:
                x -= steps
            case Direction.NORTHEAST:
                x += steps
                y += steps
            case Direction.NORTHWEST:
                x -= steps
                y += steps
            case Direction.SOUTHEAST:
                x += steps
                y -= steps
            case Direction.SOUTHWEST:
                x -= steps
                y -= steps
        return x, y

    def move(self, steps: int, direction: Direction) -> None:
        x, y = self.current_coords
        x, y = self._apply_movement(steps, direction, x, y)
        self.current_coords = (x, y)
        self.route.push((steps, direction, self.current_coords))

    def _get_opposite_direction(self, direction: Direction) -> Direction:
        opposites = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST,
            Direction.NORTHEAST: Direction.SOUTHWEST,
            Direction.NORTHWEST: Direction.SOUTHEAST,
            Direction.SOUTHEAST: Direction.NORTHWEST,
            Direction.SOUTHWEST: Direction.NORTHEAST,
        }
        return opposites[direction]

    def generate_return_path(self) -> Stack:
        return_stack = Stack()
        restore_stack = Stack()
        simulated_coords = self.current_coords

        while self.route.size() > 0:
            steps, direction, _ = self.route.pop()
            opposite_dir = self._get_opposite_direction(direction)
            x, y = self._apply_movement(steps, opposite_dir, *simulated_coords)
            simulated_coords = (x, y)
            return_stack.push((steps, opposite_dir, simulated_coords))
            restore_stack.push((steps, direction, _))

        while restore_stack.size() > 0:
            self.route.push(restore_stack.pop())

        return return_stack

    def get_readable_movements(self, stack: Stack) -> list[str]:
        readable = []
        temp = Stack()

        while stack.size() > 0:
            steps, direction, coords = stack.pop()
            readable.append(f"Direction: {direction.name} -> Coordinates: {coords}")
            temp.push((steps, direction, coords))

        while temp.size() > 0:
            stack.push(temp.pop())

        readable.reverse()
        return readable


if __name__ == "__main__":
    robot = Robot(0, 0)
    robot.move(steps=5, direction=Direction.NORTH)
    robot.move(steps=2, direction=Direction.EAST)
    robot.move(steps=3, direction=Direction.SOUTHEAST)

    print("Outbound route:")
    for move in robot.get_readable_movements(robot.route):
        print(f"  {move}")

    return_path = robot.generate_return_path()
    print("\nReturn route:")
    for move in robot.get_readable_movements(return_path):
        print(f"  {move}")
