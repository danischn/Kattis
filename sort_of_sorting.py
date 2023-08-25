def stable_sort(navneliste):
    sortert_liste = []
    for _ in range(len(navneliste)):
        sortert_liste.append(finn_minste(navneliste))

    return sortert_liste

def finn_minste(liste):
    minste_element = liste[0]
    for navn in liste:
        if navn[:2] < minste_element[:2]:
            minste_element = navn

    liste.remove(minste_element)
    return minste_element

def main():
    sortert_liste = []

    while(True):
        antall_navn = int(input())
        if(antall_navn == 0):
            break
        alle_navn = []

        for _ in range(antall_navn):
            et_navn = input()
            alle_navn.append(et_navn)

        sortert_liste_for_en_case = stable_sort(alle_navn)
        sortert_liste.append(sortert_liste_for_en_case)

    
    for liste in sortert_liste:
        for navn in liste:
            print(navn)
        print()

main()
