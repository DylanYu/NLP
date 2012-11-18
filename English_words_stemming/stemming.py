def end_with_what(word):
    word = word.lower()
    ending = []
    word = word[::-1]
    if word.find('dei') == 0:
        ending.append('ied')
    if word.find('de') == 0:
        ending.append('ed')
    if word.find('gniy') == 0:
        ending.append('ying')
    if word.find('gni') == 0:
        ending.append('ing')
    if word.find('sei') == 0:
        ending.append('ies')
    if word.find('s') == 0:
        ending.append('s')
    if word.find('se') == 0:
        ending.append('es')
    return ending

def pre_process(word):
    word = word.lower()
    ending = end_with_what(word)
    processed_words = []
    for e in ending:
        if e == 'ied':
            w = word[:len(word) - 3]
            w += 'y'
            processed_words.append(w)
        elif e == 'ed':
            w = word[:len(word) - 1]
            processed_words.append(w)
            w = word[:len(word) - 2]
            processed_words.append(w)
        elif e == 'ying':
            w = word[:len(word) - 4]
            w += 'ie'
            processed_words.append(w)
        elif e == 'ing':
            w = word[:len(word) - 3]
            processed_words.append(w)
            w = word[:len(word) - 3]
            w += 'e'
            processed_words.append(w)
        elif e == 'ies':
            w = word[:len(word) - 3]
            w += 'y'
            processed_words.append(w)
        elif e == 's':
            w = word[:len(word) - 1]
            processed_words.append(w)
        elif e == 'es':
            w = word[:len(word) - 2]
            processed_words.append(w)
    processed_words.append(word)
    return processed_words

def search(file_name, target_word):
    with open(file_name, 'r') as ffile:
        line = ffile.readline()
        while line:
            content = line.split('|')
            word = content[0].lower()
            if cmp(word, target_word) == 0:
                return line
            line = ffile.readline()
    return None

def stemming(file_name, word):
    results = []
    words = pre_process(word)
    for target_word in words:
        result = search(file_name, target_word)
        if result:
            results.append(result)
    return results


file_name = "dic_ec.txt"
print """Please type the word.
Quit the program with command 'tuichu'
""",
while True:
    word = raw_input("word: ")
    if word == "tuichu":
        break
    results = stemming(file_name, word)
    print "results:"
    if not results:
        print "word not registered"
    else:
        for s in results:
            print '#:', s,
