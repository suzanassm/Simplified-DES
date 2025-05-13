def permutation10(key):
    if len(key) != 10:
        raise ValueError("A chave deve ter 10 bits.")

    p10_order = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]  #indices começam em zero
    new_key = ''.join(key[i] for i in p10_order)
    return new_key

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def circular_shift(key, shift=1):
    if len(key) != 10:
        raise ValueError("A chave deve ter 10 bits.")

    left  = key[0:5]
    right = key[5:]

    new_right = left_shift(right, shift)
    new_left = left_shift(left, shift)

    new_key = new_left + new_right

    return new_key

def permutation8(key):
    if len(key) != 10:
        raise ValueError("A chave deve ter 10 bits.")
    p8_order = [5, 2, 6, 3, 7, 4, 9, 8] #indices começam em zero
    sub_key = ''.join(key[i] for i in p8_order)

    return sub_key

def circular_double_shift(key, shift=2):
    if len(key) != 10:
        raise ValueError("A chave deve ter 10 bits.")
    left  = key[0:5]
    right = key[5:]

    new_right = left_shift(right, shift)
    new_left = left_shift(left, shift)

    new_key = new_left + new_right

    return new_key





