def main():
    number_of_busses = int(input()) 
    bus_list = input().split()
    bus_list = [int(item) for item in bus_list]
    bus_list.sort()

    for i in range(number_of_busses):
        if i == 0:
            continue
        elif i == len(bus_list) - 1:
            break;
        else:
            inbetween(bus_list, i)
   
            
    bus_list = [str(item) for item in bus_list]
    output = ""
    for i in range(len(bus_list)):
        #Last one
        if i == len(bus_list) - 1:
            if bus_list[i - 1] == "-":
                output += bus_list[i]
            else:
                output += " " + bus_list[i]
        else:
            if i == 0:
                output += bus_list[i]
            elif bus_list [i] == "-" and bus_list[i + 1] == "-":
                continue
            elif bus_list[i - 1] != "-" and bus_list[i] == "-":
                output += bus_list[i]
            elif bus_list[i - 1] != "-":
                output += " " + bus_list[i]
            else:
                output += bus_list[i]

    print(output)
    
def inbetween(arr, index):
    prev = index - 1
    curr = index
    next = index + 1 

    if(arr[curr] == "-"):
        return

    if(arr[prev] == "-"):
        if arr[curr] + 1 == arr[next]:
            arr[curr] = "-"
            return
        else:
            return

    if(arr[prev] + 1 == arr[curr] and arr[curr] + 1 == arr[next]):
        arr[curr] = "-"

main()
