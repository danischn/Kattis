from sys import stdin

def main():
    output = []
    for linje in stdin:
        to_tall_string = linje.strip().split()
        to_tall_int = [int(tall) for tall in to_tall_string]
        differanse = to_tall_int[1] - to_tall_int[0]
        output.append(abs(differanse))

    for tall in output:
        print(tall)
main()
