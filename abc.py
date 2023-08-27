def main():
    numbers = input().split()
    numbers = [int(nr) for nr in numbers]
    numbers.sort()
    numbers.reverse()
    
    order = input()
    output = ""
    
    for i in range(len(order)):
        if order[i] == "A":
            output += str(numbers[2]) + " "
        elif order[i] == "B":
            output += str(numbers[1]) + " "
        else:
            output += str(numbers[0]) + " "

    output.strip()
    print(output)

main()
