def ordbok_innsetting():
    ordbok = {}
    while True:
        innskrevet = input()
        if(innskrevet == ""):
            break
        linje = innskrevet.split()
        key = linje[1]
        value = linje[0]
        ordbok[key] = value

    return ordbok

def hent_melding():
    meldingsListe = []
    while True:
        innskrevet = input()
        if(innskrevet == ""):
            break
        meldingsListe.append(innskrevet)

    return meldingsListe

def main():
    ordbok = ordbok_innsetting()
    melding = hent_melding()
    
    oversettelse = []
    for ord in melding:
        if ord not in ordbok.keys():
            oversettelse.append("eh")
        else:
            oversettelse.append(ordbok.get(ord))

    for oversatt_ord in oversettelse:
        print(oversatt_ord)

main()
