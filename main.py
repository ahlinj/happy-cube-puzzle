FACES = ["front", "left", "right", "top", "bottom", "back"]

def create_cube():
    return {
        FACES[0]:  [[0] * 5 for _ in range(5)],
        FACES[1]:  [[0] * 5 for _ in range(5)],
        FACES[2]:  [[0] * 5 for _ in range(5)],
        FACES[3]:  [[0] * 5 for _ in range(5)],
        FACES[4]:  [[0] * 5 for _ in range(5)],
        FACES[5]:  [[0] * 5 for _ in range(5)]
}

pink_1 = [[0,1,0,1,0],[0,1,1,1,0],[1,1,1,1,0],[0,1,1,1,1],[1,1,0,1,1]]
pink_2 = [[1,0,1,1,0],[1,1,1,1,0],[1,1,1,1,1],[0,1,1,1,1],[0,0,1,0,1]]
pink_3 = [[1,1,0,1,0],[1,1,1,1,0],[0,1,1,1,1],[0,1,1,1,0],[0,1,0,1,1]]
pink_4 = [[0,0,1,0,0],[0,1,1,1,1],[1,1,1,1,0],[1,1,1,1,0],[1,1,0,1,0]]
pink_5 = [[0,1,0,1,0],[0,1,1,1,0],[1,1,1,1,1],[1,1,1,1,0],[0,0,0,1,1]]
pink_6 = [[0,0,1,0,0],[1,1,1,1,0],[0,1,1,1,1],[1,1,1,1,0],[0,1,0,0,0]]

orange_1 = [[1,0,1,0,1],[1,1,1,1,1],[0,1,1,1,0],[1,1,1,1,1],[0,0,1,0,0]]
orange_2 = [[0,0,1,1,0],[0,1,1,1,1],[1,1,1,1,0],[0,1,1,1,1],[1,1,0,1,0]]
orange_3 = [[0,1,0,1,0],[0,1,1,1,1],[1,1,1,1,0],[0,1,1,1,0],[0,0,1,0,0]]
orange_4 = [[0,1,0,1,0],[1,1,1,1,0],[0,1,1,1,0],[1,1,1,1,1],[1,0,1,0,1]]
orange_5 = [[0,0,1,0,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
orange_6 = [[1,1,0,1,1],[0,1,1,1,0],[0,1,1,1,1],[1,1,1,1,0],[0,1,0,1,1]]

green_1 = [[1,1,0,1,1],[1,1,1,1,0],[0,1,1,1,1],[1,1,1,1,0],[0,0,1,0,0]]
green_2 = [[0,0,1,0,0],[1,1,1,1,1],[0,1,1,1,0],[1,1,1,1,1],[0,0,1,0,0]]
green_3 = [[1,1,0,1,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
green_4 = [[1,1,0,1,1],[1,1,1,1,0],[0,1,1,1,1],[1,1,1,1,0],[0,1,0,1,1]]
green_5 = [[0,1,0,1,0],[1,1,1,1,1],[0,1,1,1,0],[1,1,1,1,1],[0,0,1,0,0]]
green_6 = [[1,1,0,1,1],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]

yellow_1 = [[1,1,0,1,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,1,0,1,0]]
yellow_2 = [[0,1,0,1,0],[1,1,1,1,0],[0,1,1,1,1],[1,1,1,1,0],[0,0,1,0,0]]
yellow_3 = [[1,0,1,0,1],[1,1,1,1,1],[0,1,1,1,0],[1,1,1,1,1],[0,0,1,0,1]]
yellow_4 = [[0,0,1,0,1],[1,1,1,1,1],[0,1,1,1,1],[1,1,1,1,0],[1,0,1,0,0]]
yellow_5 = [[0,1,0,1,0],[0,1,1,1,1],[0,1,1,1,0],[1,1,1,1,1],[1,0,1,0,0]]
yellow_6 = [[1,1,0,1,0],[0,1,1,1,1],[1,1,1,1,0],[0,1,1,1,1],[0,0,1,0,0]]

blue_1 = [[1,1,0,1,1],[1,1,1,1,0],[0,1,1,1,1],[1,1,1,1,0],[0,1,0,1,0]]
blue_2 = [[0,0,1,0,1],[1,1,1,1,1],[0,1,1,1,0],[1,1,1,1,1],[0,1,0,1,0]]
blue_3 = [[0,1,0,1,1],[0,1,1,1,1],[1,1,1,1,0],[0,1,1,1,1],[0,1,0,1,0]]
blue_4 = [[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
blue_5 = [[1,0,1,0,1],[1,1,1,1,1],[0,1,1,1,0],[1,1,1,1,1],[1,0,1,0,1]]
blue_6 = [[0,0,1,0,0],[0,1,1,1,1],[1,1,1,1,0],[0,1,1,1,1],[0,0,1,0,0]]

pieces = {
    "pink": [pink_1, pink_2, pink_3, pink_4, pink_5, pink_6],
    "orange": [orange_1, orange_2, orange_3, orange_4, orange_5, orange_6],
    "green": [green_1, green_2, green_3, green_4, green_5, green_6],
    "yellow": [yellow_1, yellow_2, yellow_3, yellow_4, yellow_5, yellow_6],
    "blue": [blue_1, blue_2, blue_3, blue_4, blue_5, blue_6]
}

def rotate(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def flip(matrix):
    return [row[::-1] for row in matrix]

def place_piece(cube, piece, face):
    for i in range(5):
        for j in range(5):
            cube[face][i][j] = piece[i][j]

def get_edges(piece):
    return {
        "top": piece[0],
        "bottom": piece[4],
        "left": [row[0] for row in piece],
        "right": [row[4] for row in piece]
    }

def edges_connect(edge1, edge2):
    return all(a != b for a, b in zip(edge1[1:-1], edge2[1:-1]))

def corner_connects(corner1, corner2, corner3):
    return corner1 + corner2 + corner3 == 1

def can_place_piece(cube, piece, face):
    if not all(cell == 0 for row in cube[face] for cell in row): 
        return False

    piece_edges = get_edges(piece)
    match face:
        case "front":
            return True
        
        case "left":
            return edges_connect(get_edges(cube["front"])["left"],piece_edges["right"])

        case "right":
            return edges_connect(get_edges(cube["front"])["right"], piece_edges["left"])

        case "top":
            return (edges_connect(get_edges(cube["front"])["top"],piece_edges["bottom"]) and 
                    edges_connect(get_edges(cube["left"])["top"],piece_edges["left"]) and 
                    edges_connect(get_edges(cube["right"])["top"][::-1],piece_edges["right"]) and
                    corner_connects(cube["front"][0][0], cube["left"][0][4], piece[4][0]) and
                    corner_connects(cube["front"][0][4], cube["right"][0][0], piece[4][4])
            )

        case "bottom":
            return (edges_connect(get_edges(cube["front"])["bottom"],piece_edges["top"]) and
                    edges_connect(get_edges(cube["left"])["bottom"][::-1],piece_edges["left"]) and
                    edges_connect(get_edges(cube["right"])["bottom"],piece_edges["right"]) and
                    corner_connects(cube["front"][4][0], cube["left"][4][4], piece[0][0]) and
                    corner_connects(cube["front"][4][4], cube["right"][4][0], piece[0][4])
            )

        case "back":
            return (edges_connect(get_edges(cube["top"])["top"][::-1],piece_edges["top"]) and
                    edges_connect(get_edges(cube["bottom"])["bottom"][::-1],piece_edges["bottom"]) and
                    edges_connect(get_edges(cube["left"])["left"],piece_edges["right"]) and
                    edges_connect(get_edges(cube["right"])["right"],piece_edges["left"]) and
                    corner_connects(cube["top"][0][0], cube["left"][0][0], piece[0][4]) and
                    corner_connects(cube["top"][0][4], cube["right"][0][4], piece[0][0]) and
                    corner_connects(cube["bottom"][4][0], cube["left"][4][0], piece[4][4]) and
                    corner_connects(cube["bottom"][4][4], cube["right"][4][4], piece[4][0])
            )

        case _:
            return False

def get_orientations(piece):
    orientations = []
    current = piece

    for _ in range(4):
        if current not in orientations:
            orientations.append(current)

        current = rotate(current)

    current = flip(piece)

    for _ in range(4):
        if current not in orientations:
            orientations.append(current)

        current = rotate(current)

    return orientations

def get_children(cube, pieces, used_pieces):
    children = []

    next_face = FACES[len(used_pieces)]

    for piece_index, piece in enumerate(pieces):
        if piece_index in used_pieces:
            continue

        for orientatied_piece in get_orientations(piece):
            new_cube = {
                face: [row[:] for row in matrix]
                for face, matrix in cube.items()
            }

            if can_place_piece(new_cube, orientatied_piece, next_face):
                place_piece(new_cube, orientatied_piece, next_face)
                new_used_pieces = used_pieces + [piece_index]
                children.append((new_cube, new_used_pieces))

    return children

def breadth_first_search(pieces):
    queue = [(create_cube(), [])]

    while queue:
        cube, used_pieces = queue.pop(0)

        if len(used_pieces) == 6:
            return cube

        children = get_children(cube, pieces, used_pieces)

        for child in children:
            queue.append(child)

    return None

def breadth_first_search_count(pieces):
    queue = [(create_cube(), [])]
    solution_count = 0

    while queue:
        cube, used_pieces = queue.pop(0)

        if len(used_pieces) == 6:
            solution_count += 1
            continue

        children = get_children(cube, pieces, used_pieces)

        for child in children:
            queue.append(child)

    return solution_count

def depth_first_search(cube, pieces, used_pieces):
    if len(used_pieces) == 6:
        return cube
    
    for child_cube, child_used_pieces in get_children(cube, pieces, used_pieces):
        solution = depth_first_search(child_cube, pieces, child_used_pieces)
        if solution is not None:
            return solution
    return None

def depth_first_search_count(cube, pieces, used_pieces):
    if len(used_pieces) == 6:
        return 1

    solution_count = 0

    for child_cube, child_used_pieces in get_children(cube, pieces, used_pieces):
        solution_count += depth_first_search_count(
            child_cube, pieces, child_used_pieces
        )

    return solution_count

def depth_first_limited(cube, pieces, used_pieces, limit):
    if len(used_pieces) == 6:
        return cube
    if limit == 0:
        return None
    
    for child_cube, child_used_pieces in get_children(cube, pieces, used_pieces):
        solution = depth_first_limited(child_cube, pieces, child_used_pieces, limit - 1)
        if solution is not None:
            return solution
    return None

def rotate_cube(cube, axis):
    new_cube = create_cube()

    match axis:
        case "front_back":
            new_cube["front"] = rotate(cube["front"])
            new_cube["back"] = rotate(rotate(rotate(cube["back"])))

            new_cube["right"] = rotate(cube["top"])
            new_cube["bottom"] = rotate(cube["right"])
            new_cube["left"] = rotate(cube["bottom"])
            new_cube["top"] = rotate(cube["left"])

        case "left_right":
            new_cube["left"] = rotate(cube["left"])
            new_cube["right"] = rotate(rotate(rotate(cube["right"])))

            new_cube["bottom"] = cube["front"]
            new_cube["back"] = rotate(rotate(cube["bottom"]))
            new_cube["top"] = rotate(rotate(cube["back"]))
            new_cube["front"] = cube["top"]

        case "top_bottom":
            new_cube["top"] = rotate(cube["top"])
            new_cube["bottom"] = rotate(rotate(rotate(cube["bottom"])))

            new_cube["front"] = cube["right"]
            new_cube["left"] = cube["front"]
            new_cube["back"] = cube["left"]
            new_cube["right"] = cube["back"]

        case _:
            raise ValueError("Unknown rotation axis")

    return new_cube

def main():
    solution = depth_first_limited(create_cube(), pieces["yellow"], [], 6)

    if solution:
        print("Solution found!")

        for face in FACES:
            print(face)
            for row in solution[face]:
                print(row)
    else:
        print("No solution found.")

    #yellow
    print(f"Total number of solutions BFS (yellow): {breadth_first_search_count(pieces['yellow'])}")
    print("Total number of solutions DFS: (yellow)", depth_first_search_count(create_cube(), pieces["yellow"], []))

    #green
    print(f"Total number of solutions BFS (green): {breadth_first_search_count(pieces['green'])}")
    print("Total number of solutions DFS: (green)", depth_first_search_count(create_cube(), pieces["green"],[]))

    #blue
    print(f"Total number of solutions BFS (blue): {breadth_first_search_count(pieces['blue'])}")
    print("Total number of solutions DFS: (blue)", depth_first_search_count(create_cube(), pieces["blue"],[]))

    #orange
    print(f"Total number of solutions BFS (orange): {breadth_first_search_count(pieces['orange'])}")
    print("Total number of solutions DFS: (orange)", depth_first_search_count(create_cube(), pieces["orange"],[]))

    #pink
    print(f"Total number of solutions BFS (pink): {breadth_first_search_count(pieces['pink'])}")
    print("Total number of solutions DFS: (pink)", depth_first_search_count(create_cube(), pieces["pink"],[]))


if __name__ == "__main__":
    main()