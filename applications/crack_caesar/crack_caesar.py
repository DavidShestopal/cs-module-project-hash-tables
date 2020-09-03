# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("/Users/david/Desktop/cs/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt") as f:
    words = f.read()


word_list = words.split()


letters = ('E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
           'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z')


count = {}

for word in word_list:
    for char in word:
        if char.isalpha():

            if char not in count:
                count[char] = 1

            else:
                count[char] += 1
        else:
            continue


letter_count = list(count.items())

letter_count.sort(key=lambda x: x[1], reverse=True)


decoded = {}

for num in range(len(letter_count)):
    decoded[letter_count[num][0]] = letters[num]


def crack_caeser(s):

    translated_cipher = ''

    for char in s:
        if char.isalpha():

            translated_cipher += decoded[char]
        else:

            translated_cipher += char

    return translated_cipher


final_decode = map(crack_caeser, word_list)


print(" ".join(final_decode))
