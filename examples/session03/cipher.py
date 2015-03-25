import random

alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = [alphabet[i] for i in range(len(alphabet))]
#alphabet_list = list(alphabet)


message_text = "gfzljqgfzljqewqvqhfzyfj"

cipher_list = ['v', 'y', 'h', 'l', 'a', 'n', 'i', 'g', 'e', 'd', 'k', 'c', 'w', ' ', 'f', 's', 'm', 'p', 'r', 't', 'o', 'u', 'z', 'b', 'j', 'x', 'q'] 
# random.shuffle(cipher_list)

cipher_text = ""

for x in message_text:
    index = alphabet_list.index(x)
    cipher_char = cipher_list[index]
    cipher_text += cipher_char

print cipher_text
# print cipher_list
new_cipher_text = "eqzergqtgvtqeqgvlqrfwaqa hgecvlvrqpeigtq fz"
decrypted_text = ""
for y in new_cipher_text:
    index = cipher_list.index(y)
    decrypted_char = alphabet_list[index]
    decrypted_text += decrypted_char
print decrypted_text

