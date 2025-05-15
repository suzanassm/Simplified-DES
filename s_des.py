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

def initial_permutation(block):
    if len(block) != 8:
        raise ValueError("O bloco deve ter 8 bits.")
    ip_order = [1, 5, 2, 0, 3, 7, 4, 6]
    new_block = ''.join(block[i] for i in ip_order)

    return new_block

def div(block):
    if len(block) != 8:
        raise ValueError("O bloco deve ter 8 bits.")
    block_left = block[0:5]
    block_right = block[5:]
    return block_left, block_right

def s_box_substitutions(bits, s):
    linha = int(bits[0] + bits[3], 2)  # bits 1 e 4
    coluna = int(bits[1] + bits[2], 2)  # bits 2 e 3
    valor_sbox = s[linha][coluna]
    return valor_sbox # acho que aqui tá errado

def feistel_round(block_left, block_right, k):
    ep_order = [3, 0, 1, 2, 1, 2, 3, 0]
    new_right = ''.join(block_right[i] for i in ep_order)
    new_rigth = (new_right and not k) or (not new_right and k)
    first = new_right[0:4]
    last = new_right[4:8]

    s0 =[[1,  0,  11,  10],
        [11,  10,  1,  0],
        [0,  10,  1,  11],
        [11,  1,  11,  10]]
    s1=[[0, 1, 10, 11],
        [10, 0, 1, 11],
        [11, 0, 1, 0],
        [10, 1, 0, 11]]
    new_first = s_box_substitutions(first, s0)
    new_last = s_box_substitutions(last, s1)

    p4_order = [1, 3, 2, 0]
    new_right = ''.join(new_first[i] for i in p4_order)
    new_right = ''.join(new_last[i] for i in p4_order)  #fim da funcao f





