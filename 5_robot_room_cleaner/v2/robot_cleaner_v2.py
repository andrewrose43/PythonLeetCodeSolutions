class Solution:
    def cleanRoom(self, robot):
        checked = {(0, 0)}  # this set records which cells have been visited or revealed as obstacles/borders
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))  # down left up right, indexed 0 1 2 3

        # Turn right and return new direction
        def _my_right(direction: int):
            robot.turnRight()
            return (direction + 1) % 4

        # Turn left and return new direction
        def _my_left(direction: int):
            robot.turnLeft()
            return (direction - 1) % 4

        # Compute the adjacent cell in any direction
        def _adj_cell(curr: tuple, direction: int):
            return tuple(map(lambda x, y: x+y, curr, directions[direction]))

        def _backtrack(curr: tuple, direction=0):
            robot.clean()
            direction = _my_left(direction)  # turn left to start sweeping left-to-right
            for i in (0, 1, 2):  # run 3 times; the for-each is Python's fastest loop even if you don't use the
                # tuple's contents for anything
                new_cell = _adj_cell(curr, direction)
                if new_cell not in checked:  # if you haven't yet visited this cell
                    checked.add(new_cell)  # you've now visited this cell
                    if robot.move():
                        _backtrack(new_cell, direction)
                        robot.move()  # robot will be facing the way it came by this point
                        # note the "+ 2" in the next line because the recursive call's changes to direction would not
                        # otherwise be recorded
                        direction = _my_left((direction + 2) % 4)  # face correct direction to resume execution
                    else:
                        direction = _my_right(direction)  # turn to face next cell
                else:
                    direction = _my_right(direction)  # turn to face next cell

        # Because only the first cell requires 4 checks, this clone of _backtrack does what _backtrack does,
        # except that it checks all 4 adjacent cells. I could have passed 4 as a parameter to _backtrack just once,
        # with 3 being the default, and used range() to change the length of the internal loop, but that would cause
        # inefficiency via 1) using a range loop instead of a for-each loop, which is faster, and 2) one unnecessary left turn operation at the start, though that's minor.
        direction = 0
        curr = (0, 0)
        robot.clean()
        for i in (0, 1, 2, 3):  # run 4 times; the for-each is Python's fastest loop even if you don't use the
            # tuple's contents for anything
            new_cell = _adj_cell(curr, direction)
            if new_cell not in checked:  # if you haven't yet visited this cell
                checked.add(new_cell)  # you've now visited this cell
                if robot.move():
                    _backtrack(new_cell, direction)
                    robot.move()  # robot will be facing the way it came by this point
                    # note the "+ 2" in the next line because the recursive call's changes to direction would not
                    # otherwise be recorded
                    direction = _my_left((direction + 2) % 4)  # face correct direction to resume execution
                else:
                    direction = _my_right(direction)  # turn to face next cell
            else:
                direction = _my_right(direction)  # turn to face next cell