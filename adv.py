from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def traversal():
    visited = {}
    path = []
    visited[player.current_room.id] = player.current_room.get_exits()
    while len(visited) < len(room_graph):
        room_id = player.current_room.id
        room_dir = player.current_room.get_exits()
        if room_id not in visited:
            visited[room_id] = room_dir
            previous = path[-1]
            visited[room_id].remove(previous)

        if len(visited[room_id]) == 0:
            previous = path[-1]
            path.pop()
            traversal_path.append(previous)
            player.travel(previous)

        else:
            direction = random.choice(visited[room_id])
            visited[room_id].pop(visited[room_id].index(direction))
            traversal_path.append(direction)
            if direction == 'n':
                path.append('s')
            elif direction == 's':
                path.append('n')
            elif direction == 'e':
                path.append('w')
            elif direction == 'w':
                path.append('e')
            player.travel(direction)


traversal()


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
