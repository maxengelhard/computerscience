def main():
    while True:
        text = input("Text: ")
        if not text:
            continue
        else:
            break
    print(text)

    countLetters = 0;
    countWords = 0;
    countSentences = 0;
    for l in text:
        if isEndOfSentence(l): 
            countSentences +=1
        elif l ==' ':
            countWords += 1
        elif l!="'" or l!='-':
            countLetters+=1
    # end of all
    countWords+=1
    # average number of letters per 100 words
    L = (countLetters / countWords)*100
    S = (countSentences / countWords) *100

    level = round(calcLevel(L,S))

    if level >16:
        level = '16+'
    if level <1:
        level = 'Before Grade 1'
    else:
        level = 'Grade ' + str(level)
   
    print(level)
    return level

    


def calcLevel(L, S): 
    # where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
    return 0.0588 * L - 0.296 * S - 15.8

def isEndOfSentence(l):
    if l=='!' or l=='.' or l=='?':
        return True
    else:
        return False


if __name__ == "__main__":
    main()
