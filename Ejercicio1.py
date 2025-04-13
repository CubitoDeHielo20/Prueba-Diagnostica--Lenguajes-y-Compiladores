def FEN (fen_string):
   
    parts = fen_string.split()
    if len(parts) != 6:
        return False

    
    piece_placement = parts[0]
    ranks = piece_placement.split('/')
    if len(ranks) != 8:
        return False
    for rank in ranks:
        square_count = 0
        for char in rank:
            if char.isdigit():
                square_count += int(char)
            elif char in 'rnbqkpRNBQKP':
                square_count += 1
            else:
                return False
        if square_count != 8:
            return False

    
    active_color = parts[1]
    if active_color not in ('w', 'b'):
        return False

    
    castling_availability = parts[2]
    if not all(char in 'KQkq-' for char in castling_availability):
        return False

    
    en_passant_target = parts[3]
    if en_passant_target != '-':
        if not (len(en_passant_target) == 2 and
                'a' <= en_passant_target[0] <= 'h' and
                '1' <= en_passant_target[1] <= '8'):
            return False

    
    halfmove_clock = parts[4]
    if not halfmove_clock.isdigit():
        return False

    
    fullmove_number = parts[5]
    if not fullmove_number.isdigit():
        return False

    return True

if __name__ == "__main__":
    fen_a_validar = input("Ingrese la cadena a validar como notación FEN: ")
    if FEN (fen_a_validar):
        print(f"La cadena '{fen_a_validar}' parece estar en notación FEN ")
    else:
        print(f"La cadena '{fen_a_validar}' no parece estar en notación FEN ")