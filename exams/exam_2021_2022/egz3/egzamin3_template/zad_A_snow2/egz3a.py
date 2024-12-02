from egz3atesty import runtests


def snow( T, I ):
    road = [0 for _ in range(T)]

    for u, v in I:

        for i in range(u, v + 1):
            road[i] += 1

    return max(road)


# Na poczatku tworzę nowa listę zawierajaca początki oraz końće przedziałów z podanej listy I, przy czym przy tworzeniu
# nowej listy do każej współrzędnej dodaje opis czy jest to początek czy koniec przedziału oraz współrzędne końcowe
# zwiększam o jeden aby poźniej poprawnie rozpatrywać dany przedział.Kolejno sortuje listę najpierw po wspołrzędnej x a
# jeśli są one równe to najpierw znajdzie się ta będąca końćem przedziału, tak aby poprawnie rozpartywać przedziały.
# Następnie iterujać przez tak stworzoną listę,jeśli napotkam początek przedziału to zwięszkam o jeden zmienna
# reprezentujacą obecną wysokość śniegu oraz aktualizuje maksymalną napotkaną dotychczas grubosć śniegu.Jeśli napotkam
# na koniec przedziału to dekrementuje zmienną przechowującą aktulaną grubość śniegu.
def snow1(T, I):
    events = []

    # Step 1: Create events for all intervals
    for a, b in I:
        events.append((a, 'start'))
        events.append((b+1 , 'end'))

    # Step 2: Sort events
    events.sort(key=lambda x: (x[0], x[1] == 'start'))

    max_snow = 0
    current_snow = 0

    # Step 3: Process events
    for position, event_type in events:
        if event_type == 'start':
            current_snow += 1
            max_snow = max(max_snow, current_snow)
        else:  # event_type == 'end'
            current_snow -= 1

    return max_snow




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow1, all_tests =True )
