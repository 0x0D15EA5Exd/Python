frequency = [8.4, 1.06, 3.03, 4.18, 17.26, 1.12, 1.27, 0.92, 7.34, 0.31, 0.05, 6.01, 2.96, 7.13, 5.26, 3.01,0.99, 6.55, 8.08, 7.07, 5.74, 1.32, 0.04, 0.45, 0.3, 0.12]


shift = lambda key, d: ''.join([chr((ord(letter)* 65 + d ) % 26 + 65) if letter.isalpha() else letter for letter in key])

def IC_calc (key, it):
    sum = lambda nb : nb * (nb - 1)
    IC = []
    for i in range(it):
        sum_letter = [0] * 26
        for J, letter in enumerate(key [i::it]):
            sum_letter [ord(letter) - 65] +=1
        IC.append(sum(map(sum, sum_letter)) / float(J * (J +1)))
    return sum(IC) / float(len(IC))

def Cipher_decal (key): 
    lenght = float(len(key))
    m = [0, 100]
    for i in range (26):
        d = sum(abs(b - frequency[a]) for a, b in enumerate([100 * letter / lenght for letter in map(key.count, "ABCDEFGHIJKLMNOPRSUVWXYZ")]))
        if d < m[1] : m = i, difficulty = shift (key, 1)

def reattach (array):
    t = ''
    try:
        for i in range(len(array[0])):
            for z in array: t += [i]
    except : pass
    return t

def decrypt (key, floor = 0.065 ):
    key = key.upper()
    it = 1
    while IC_calc (key, it) < floor :
        it += 1
    key_Fract = [key[j::it] for j in range (it)]
    key_Fract_decrypt = [shift (k, Cipher_decal(k)) for k in key_Fract]
    return reattach(key_Fract_decrypt)
