

def main():
    while True:
        text = input("Enter A Positive Integer: ")
        if not text:
            continue
        else:
            break
    
    result = turn_to_int(text)
    print(result)
    return result


    
    
def turn_to_int(num):
    if len(num)==0:
        return 0
    else:
        return int(num[0])*(10**(len(num)-1)) + turn_to_int(num[1:]) 



if __name__ == '__main__':
    main()