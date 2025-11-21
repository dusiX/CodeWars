# Task
# Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

# Notes
# Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other 
# and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].

def dir_reduc(arr):
    dir = 0
    while dir + 1 < len(arr):
        match arr[dir]:
            case "NORTH":
                if arr[dir + 1] == "SOUTH":
                    del arr[dir]
                    del arr[dir]
                    dir = -1
            case "SOUTH":
                if arr[dir + 1] == "NORTH":
                    del arr[dir]
                    del arr[dir]
                    dir = -1
            case "EAST":
                if arr[dir + 1] == "WEST":
                    del arr[dir]
                    del arr[dir]
                    dir = -1
            case "WEST":
                if arr[dir + 1] == "EAST":
                    del arr[dir]
                    del arr[dir]
                    dir = -1
        dir += 1
    return arr
