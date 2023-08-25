def fjern(liste):
    output = []
    for i in range(len(liste)):
        if liste[i] != "<":
            output.append(liste[i])
        else:
            output.pop(-1)
    
    return output

def main():
    innlest = input()
    liste = list(innlest)
    ny_liste = fjern(liste)
    output = "".join(ny_liste)
    print(output)

main()
