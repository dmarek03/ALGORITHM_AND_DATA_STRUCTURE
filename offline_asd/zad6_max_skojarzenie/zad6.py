# DOMINIK MAREK
# Rozwiązanie tego zadnia sprowadza się do znalezienia licznośći największego skojarzenia w grafie, w którym jeden zbiór
# wierzchołków to pracownicy(liczba tablic w tablicy M) a drugi to maszyny(elemnty z tablic w tablicy M).
# Za pomocą funkcji employee_to_machines dla każdego pracownika sprawdzam czy można przyporządkować mu maszynę nie
# zmiejszająć tym samym liczby już pracujących maszyn, jeśli jest to możliwe to funkcją zwraca True wpp False. Dla
# danego pracownika przechodzę przez jego kwalifiakcje i przypisuję go do pierwszej wolnej maszyny, którą może
# obłsugiwać.Jeśli wszytskie maszyny, na które ma zezwolenie są zajęte to sprawdzam czy jest możliwe przesunięcie innego
# pracownika na wolną maszynę, tak aby pracownik, któremu chcę przporządować maszynę mógł wykonywać pracę.
# Następnie w głównej funkcji przechodząć przez wszytskich pracowników sprawdzam czy funkcją employee_to_machine
# zwróciła True ,czyli że udało się zwiększyć liczbę pracujących maszyn,jeśli tak to  zwiększam licznik pracujących
# pracowników,jego końcowa wartość jest rozwiązaniem zadanego problemu.

from zad6testy import runtests


def employee_to_machine(employees_qualifications: list[list[int]], working_machines: list[int], machines: list[int], employee: int) -> bool:
    for q in employees_qualifications[employee]:
        if not working_machines[q]:
            working_machines[q] = True
            if machines[q] < 0 or employee_to_machine(employees_qualifications, working_machines, machines, machines[q]):
                machines[q] = employee
                return True

    return False


def binworker(M: list[list[int]]) -> int:

    n = len(M)
    machines = [-1] * n
    max_employees_cnt = 0
    for employee in range(n):
        working_machines = [False]*n
        max_employees_cnt += 1 if employee_to_machine(M, working_machines, machines, employee) else 0
    return max_employees_cnt

# zmien all_tests na True zeby uruchomic wszystkie testy


runtests(binworker, all_tests=True)
