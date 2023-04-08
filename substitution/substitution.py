import sys

def main():
    try:
        token = sys.argv[1] 
    except:
        raise ValueError("Usage: substitution.py key")
    # assert that it's 26 characters 
    if not len(token)==26: raise ValueError("Key must contain 26 characters.")

    token += token.lower()

    hash_token = {i:x for i,x in enumerate(token)}

    # get input of word
    while True:
        text = input("plaintext: ")
        if not text:
            continue
        else:
            break
    
    # map the words
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet += alphabet.lower()
    hash_alpha = {x:i for i,x in enumerate(alphabet)}
    result = ''
    for l in text:
        # get the index of the aplhabet
        if l not in hash_alpha:
            result += l
        else:
            result += hash_token[hash_alpha[l]]

    print(result)
    return result


if __name__ == "__main__":
    main()