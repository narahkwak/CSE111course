
def main():
    provinces = read_file("provinces.txt")
    print (provinces)
    #removing the first element
    provinces.pop(0)
    print (provinces)
    #removing the last element
    provinces.pop()
    print (provinces)

    #replcae AB with Alberta
    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"
    print (provinces)

    #counting
    count = provinces.count("Alberta")
    print(f"The number of occurances for Alberta is {count} times")
        



def read_file(filename): 
    text_list =[]
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list
    
if __name__ == "__main__":
    main()