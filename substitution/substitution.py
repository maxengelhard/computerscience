import sys

def main():
    token = sys.argv[1] 
    # assert that it's 26 characters
    assert len(token)==26

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