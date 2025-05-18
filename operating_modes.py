from s_des import permutation10, left_shift, circular_shift, permutation8, circular_double_shift, initial_permutation, div, xor_bits, s_box_substitutions,feistel_round, permutation_inverse



def eco(binary_text, key10):
    if len(key10) != 10:
        raise ValueError("A chave deve ter 10 bits.")
    if len(binary_text) % 8 != 0:
        raise ValueError("O texto binário deve ter tamanho múltiplo de 8.")

    key_p10 = permutation10(key10)
    k1 = permutation8(circular_shift(key_p10))
    k2 = permutation8(circular_double_shift(key_p10))

    ciphertext = ''
    for i in range(0, len(binary_text), 8):
        block = binary_text[i:i+8]

        block_ip = initial_permutation(block)
        l, r = block_ip[:4], block_ip[4:]

        l, r = feistel_round(l, r, k1, is_first_round=True)

        result = feistel_round(l, r, k2, is_first_round=False)

        cipher_block = permutation_inverse(result)
        ciphertext += cipher_block

    return ciphertext



def generate_subkeys(key10):
    p10 = permutation10(key10)
    k1 = permutation8(circular_shift(p10))
    k2 = permutation8(circular_double_shift(p10))
    return k1, k2


def sdes_encrypt_block(block8, k1, k2):
    ip = initial_permutation(block8)
    L, R = ip[:4], ip[4:]
    L1, R1 = feistel_round(L, R, k1, is_first_round=True)
    final = feistel_round(L1, R1, k2, is_first_round=False)
    return permutation_inverse(final)


def sdes_decrypt_block(block8, k1, k2):
    ip = initial_permutation(block8)
    L, R = ip[:4], ip[4:]
    L1, R1 = feistel_round(L, R, k2, is_first_round=True)  # Inverso da cifragem
    final = feistel_round(L1, R1, k1, is_first_round=False)
    return permutation_inverse(final)


def split_blocks(text):
    if len(text) % 8 != 0:
        raise ValueError("Texto binário deve ter múltiplos de 8 bits.")
    return [text[i:i + 8] for i in range(0, len(text), 8)]


def cbc_encrypt(text_bin, key10, iv):
    k1, k2 = generate_subkeys(key10)
    blocks = split_blocks(text_bin)
    ciphertext = ''
    prev_cipher = iv

    for block in blocks:
        xored = xor_bits(block, prev_cipher)
        cipher_block = sdes_encrypt_block(xored, k1, k2)
        ciphertext += cipher_block
        prev_cipher = cipher_block

    return ciphertext


def cbc_decrypt(ciphertext_bin, key10, iv):
    k1, k2 = generate_subkeys(key10)
    blocks = split_blocks(ciphertext_bin)
    plaintext = ''
    prev_cipher = iv

    for block in blocks:
        decrypted = sdes_decrypt_block(block, k1, k2)
        plain_block = xor_bits(decrypted, prev_cipher)
        plaintext += plain_block
        prev_cipher = block

    return plaintext

    