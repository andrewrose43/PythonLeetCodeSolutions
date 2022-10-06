# This first attempt at a solution DOES NOT WORK! The problem here is at the core of the algorithm: because the for
# loop has no memory of what the previously-visited square was, there's no way to return to the previously-visited
# square. This solution attempts to use direction_index for that purpose, but in the event that a dead end has been
# reached, direction_index has no relationship to the direction of the previously-visited square, so it does not
# work. Thus, there's no way to "fix" this other than replacing the whole algorithm. Time to consult LeetCode's
# solution.

class Solution:
    def cleanRoom(self, robot):

        # CONSTANTS
        visited = set()  # A record of every cell that we've visited so far
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))  # down, right, up, left (assuming "down" is the original direction the robot was pointing at the start. It's all relative to the original direction, so... the enemy's gate is down.)
        curr = (0, 0)  # The starting square
        visited.add(curr)

        def backtrack():
            nonlocal curr  # To avoid an UnboundLocalError
            robot.clean()
            # find_solution is simply what happens when all adjacent spaces have already been visited: backtrack() returns without doing anything

            for direction_index, direction in enumerate(directions):  # Look in every direction around the robot
                adj_space = tuple(map(lambda x, y: x+y, curr, direction))
                if adj_space not in visited:  # the is_valid check
                    # First up, whether it's an obstacle/map edge or a dirty space, it has now been visited.
                    visited.add(adj_space)
                    # "place()" begins here
                    for t in range(direction_index):  # Rotate to face the proper direction.
                        robot.turnLeft()
                    moved = robot.move()
                    for t in range(direction_index):  # Rotate to face down again
                        robot.turnRight()
                    # There's only a need to call backtrack() and undo the steps if an obstacle/edge of map was not encountered
                    if moved:
                        tmp_space = curr
                        curr = adj_space
                        # backtrack - self-explanatory
                        backtrack()
                        # "remove()" begins here
                        curr = tmp_space
                        for t in range(direction_index):  # Rotate to return to previous location
                            robot.turnRight()
                        robot.move()
                        for t in range(direction_index):  # Rotate to face down again
                            robot.turnLeft()

        backtrack()  # Start the operation!