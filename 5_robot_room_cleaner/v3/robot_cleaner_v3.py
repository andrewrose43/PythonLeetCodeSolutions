class Solution:

    def cleanRoom(self, robot):
        # INITIALIZATION
        cell_0 = (0, 0)  # Starting cell
        checked = {cell_0}  # Set of checked cells
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))  # down, right, up, left. Counter-clockwise order.
        arr3 = (0, 1, 2)  # Cached for fast access.
        robot.clean()  # Clean starting cell

        def _adj_cell(cell: tuple, direction: tuple):
            return tuple(map(lambda x, y: x+y, cell, direction))

        def _backtrack(curr: tuple, d: int):  # current cell; direction currently faced
            robot.clean()
            robot.turnLeft()  # start with the left cell

            for i in arr3:  # left, forward, right
                new_d = (d + 1 - i) % 4  # Calculate new direction. + 1 because of the initial left turn
                new_cell = _adj_cell(curr, directions[new_d])
                if not new_cell in checked:
                    checked.add(new_cell)
                    if robot.move():
                        _backtrack(new_cell, new_d)
                        robot.move()
                        robot.turnLeft()
                    else:
                        robot.turnRight()
                else:
                    robot.turnRight()
                # By now, the robot is facing the cell it came from.

        # FIRST CELL RUN
        # This is needed because only the starting cell needs all 4 directions around it checked.
        # _backtrack is identical except that:
            # -_backtrack sweeps 3 directions instead of 4, thus saving time
            # -_backtrack uses fancy logic to determine the direction relative to the starting direction, whereas this
            # code just takes the starting direction as "0" whatever it is
        for i in (0, 1, 2, 3):  # All 4 directions, not just left-forward-right.
            new_cell = _adj_cell(cell_0, directions[i])
            if not new_cell in checked:
                checked.add(new_cell)
                if robot.move():
                    _backtrack(new_cell, i)
                    robot.move()
                    robot.turnLeft()
                else:
                    robot.turnRight()
            else:
                robot.turnRight()
