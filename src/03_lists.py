# 1. Separate a list of integers into two lists of positive/negative integers, sort and print each.

with open('resources/random_integers.txt', 'r') as fin:
    pos_neg_list = [int(s) for s in fin.read().split()]
    positives = []
    negatives = []
    for index, item in enumerate(pos_neg_list):
        negatives.append(item) if item < 0 else positives.append(item)

    print(', '.join(map(str, sorted(positives))))
    print(', '.join(map(str, sorted(negatives))))
        
# 2. Determine the # of occurrences of the maximum number in an integer array.

with open('resources/random_integers.txt', 'r') as fin:
    int_list = [int(s) for s in fin.read().split()]

    # alternatively, iterate through the array counting current max and reset the count to 1 when new max encountered
    # pros: only one array pass, cons: less pythonic
    count = int_list.count(max(int_list)) 

    print(count)

# 3. Remove the words starting with the letters 'd' or 'w' from a string list.

with open('resources/golden_beetle_randomcase.txt', 'r') as fin:
    string_list = fin.read().split()
    for index, item in enumerate(string_list):
        if item[0].lower() in 'dw':
            string_list.pop(index)
    print(' '.join(string_list))   

# 4. Format a string list so that
# - words are separated by 1 space
# - sentences start with a titlecase word
# - all other words are lowecase

with open('resources/golden_beetle_randomcase.txt', 'r') as fin:
    text = fin.read().split()
    newSentence = True
    for index, item in enumerate(text):
        if newSentence:
            text[index] = item.title()
            newSentence = False
        else:
            if item[-1] == '.':
                newSentence = True
            text[index] = item.lower()
    print(' '.join(text))
