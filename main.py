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
    return all(a != b for a, b in zip(edge1, edge2))

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
                    edges_connect(get_edges(cube["right"])["top"],piece_edges["right"])
            )

        case "bottom":
            return (edges_connect(get_edges(cube["front"])["bottom"],piece_edges["top"]) and
                    edges_connect(get_edges(cube["left"])["bottom"],piece_edges["left"]) and
                    edges_connect(get_edges(cube["right"])["bottom"],piece_edges["right"])
            )

        case "back":
            return (edges_connect(get_edges(cube["top"])["top"],piece_edges["top"]) and
                    edges_connect(get_edges(cube["bottom"])["bottom"],piece_edges["bottom"]) and
                    edges_connect(get_edges(cube["left"])["left"],piece_edges["right"]) and
                    edges_connect(get_edges(cube["right"])["right"],piece_edges["left"])
            )

        case _:
            return False

def get_orientations(piece):
    orientations = []

    current = piece

    for _ in range(4):
        orientations.append(current)
        current = rotate(current)

    current = flip(piece)

    for _ in range(4):
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

def main():
    solution = breadth_first_search(pieces["pink"])

    if solution:
        print("Solution found!")

        for face in FACES:
            print(face)
            for row in solution[face]:
                print(row)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()