from sys import stdin

def hent_gjennomsnitt(liste, antall):
    sum = 0
    for score in liste:
        sum += score

    return sum / antall;

def over_gjennomsnitt(liste, antall_studenter, score):
    antall_over_gjennomsnitt = 0
    for student_score in liste:
        if student_score > score:
            antall_over_gjennomsnitt += 1
    
    prosentandel = round((antall_over_gjennomsnitt / antall_studenter) * 100, 3)
    formatted_prosentandel = "{:.3f}".format(prosentandel)
    return formatted_prosentandel

def main():
    output = []
    antall_test = int(input())
    for linje in stdin:
        innlest = linje.strip().split()
        resultater = [int(tall) for tall in innlest]
        antall_studenter = int(resultater.pop(0))
        gjennomsnitt_score = hent_gjennomsnitt(resultater, antall_studenter)
        above_average = over_gjennomsnitt(resultater, antall_studenter, gjennomsnitt_score)
        output.append(str(above_average) + "%")

    for score in output:
        print(score)

main()
    


