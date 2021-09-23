def main():
    #write your code below this line
    names = []
    while True:
        name = input()
        if (name == ""):
            break
        else:
            names.append(name)
    print("In total: " + str(len(names)))

if __name__ == '__main__':
    main()
