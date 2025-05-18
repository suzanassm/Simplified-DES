from s_des import permutation10, left_shift, circular_shift, permutation8, circular_double_shift, initial_permutation, div, xor_bits, s_box_substitutions,feistel_round, permutation_inverse
from operating_modes import permutation10, circular_shift, circular_double_shift, permutation8, sdes_encrypt_block, sdes_decrypt_block, initial_permutation,permutation_inverse, feistel_round, xor_bits, split_blocks,cbc_encrypt, cbc_decrypt, generate_subkeys
def main():
    key10 = '1010000010'
    mensagem = '11010111011011001011101011110000'  # 4 blocos de 8 bits
    iv = '01010101'

    print("Mensagem original (binário):")
    print(mensagem)

    print("\n--- Modo ECB ---")
    # ECB: cifrar
    key_p10 = permutation10(key10)
    k1 = permutation8(circular_shift(key_p10))
    k2 = permutation8(circular_double_shift(key_p10))

    ciphertext_ecb = ''
    for i in range(0, len(mensagem), 8):
        block = mensagem[i:i+8]
        cipher_block = sdes_encrypt_block(block, k1, k2)
        ciphertext_ecb += cipher_block
    print("Cifra ECB:")
    print(ciphertext_ecb)

    # ECB: decifrar
    plaintext_ecb = ''
    for i in range(0, len(ciphertext_ecb), 8):
        block = ciphertext_ecb[i:i+8]
        plain_block = sdes_decrypt_block(block, k1, k2)
        plaintext_ecb += plain_block
    print("Decifra ECB:")
    print(plaintext_ecb)

    print("\n--- Modo CBC ---")
    # CBC: cifrar
    ciphertext_cbc = cbc_encrypt(mensagem, key10, iv)
    print("Cifra CBC:")
    print(ciphertext_cbc)

    # CBC: decifrar
    plaintext_cbc = cbc_decrypt(ciphertext_cbc, key10, iv)
    print("Decifra CBC:")
    print(plaintext_cbc)

if __name__ == "__main__":
    main()
