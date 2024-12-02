"""
Uniwersalne ujście -> to taki wierzchołek, jeśli z każdego innego wierzchołka istnieje krawędź prowadząca do niego, a
z niego nie wychodzi żadna krawędź

Szukamy wiersza w którym są same zera oraz kolumny z samymi jedynkami i jednym zerem.
Poruszamy się według zasady jeżeli trafimy na jedynkę to idziemy w dół a jeśli na zero w prawo.
Jeśli graf ma ujście to skończymy w wierszu, w którym ma być ujście i potem trzeba sprawdzić czy w kolumnie są same
jedynki z jednym zerem
"""