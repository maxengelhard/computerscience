def main():

    while True:
        num_votes = int(input("Number Of Votes: "))
        if not num_votes or num_votes>9:
            continue
        else:
            break
    
    hash_map = {}
    max_counts = 0
    person_in_lead = None
    while num_votes>0:
        name = input("Vote: ")
        if not name:
            print("Invalid Vote")
            continue
        if name not in hash_map:
            hash_map[name] = 1
        else:
            hash_map[name] +=1

        if hash_map[name] > max_counts:
            max_counts = hash_map[name]
            person_in_lead = name

        num_votes -=1

    print(person_in_lead)
    return person_in_lead




if __name__ == "__main__":
    main()