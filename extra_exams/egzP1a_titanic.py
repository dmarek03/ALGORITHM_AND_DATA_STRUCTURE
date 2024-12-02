from egzP1atesty import runtests 
from math import inf
# Complexity -> O(nlogm)
# Zamieniamy napis na alfabet morsa oraz tworzymy tablicę rozpoznawalnych liter.Następnie dla każdego znaku z
# przetłumaczonej wiadomości bierzemy fragment tej wiadomośći o  długosci z zakres od 1 do 4 i sprawdzamy czy akurat
# taki znak jest dostępny. Kolejno dla i-tego znaku zakodowanej wiadomosći znajdujemy minimalną ilość liter potrzebną
# do przesłania tego znaku.
# dp[i] -> ilość liter do zakodowania fragmentu wiadomości od zera od i

def to_morse_alphabet(text: str, alphabet: list[tuple[str, str]]) -> str:
    return ''.join([alphabet[ord(text[i])-65][1] for i in range(len(text))])


def titanic( W, M, D ):
    recognizable_letters = set([M[d][1] for d in D])

    translated_message = to_morse_alphabet(W, M)
    n = len(translated_message)
    dp = [0]*n
    dp[0] = 1
    for i in range(1, n):
        min_len = inf
        for j in range(4):
            if i-j >= 0:
                word = translated_message[i-j:i+1]
                if word in recognizable_letters:
                    curr_len = dp[i-j-1]
                    if curr_len < min_len:
                        min_len = curr_len
        dp[i] = min_len+1# dodajemy jeden bo dokładamy kolejną literę
    if n < 20:
        print(f'{recognizable_letters=}')
        print(f'{translated_message=}')
        print(f'{dp=}')
    return dp[n-1]



runtests ( titanic, recursion=False )


