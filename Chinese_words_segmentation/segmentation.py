# coding=utf-8
class Segmentation:
    file_name = 'dic_ce.txt'
    dictionary = []
    #max length of dictionary item
    dict_maxlen = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.dictionary = []
    def __del__(self):
        pass

    def read_file(self):
        dictionary = []
        with open(self.file_name) as f:
            line = f.readline()
            while line:
                #encode the phrase with utf-8
                phrase = unicode(line.split(',')[0], "utf-8")
                #define the max length of dictionary item
                if len(phrase) > self.dict_maxlen:
                    self.dict_maxlen = len(phrase)
                self.dictionary.append(phrase)
                line = f.readline()
        return self.dictionary

    def search(self, target_word):
        for word in self.dictionary:
            if cmp(word, target_word) == 0:
                return target_word
        return None

    def segment(self, sentence):
        #We can't do encoding recursively, so 'sentence' should be encoded outside the function
        phrase = ''
        max_phrase = ''
        max_phrase_len = 0
        count = 0
        for count in range(0, len(sentence)):
            phrase += sentence[count]
            if len(phrase) > self.dict_maxlen:
                break
            r = self.search(phrase)
            if r:
                if len(r) > max_phrase_len:
                    max_phrase = phrase
                    max_phrase_len = len(r)
        #phrase not in the dict
        if max_phrase_len == 0:
            print sentence[0], '|',
            max_phrase_len = 1
        #phrase in the dict
        else:
            print max_phrase, '|',
        #recurse
        if max_phrase_len < len(sentence):
            self.segment(sentence[max_phrase_len :])


seg = Segmentation('dic_ce.txt')
seg.read_file()
print """
Please input the sentence you want to do segmentation.
Quit the program with command 'tuichu'
"""
while True:
    sentence = raw_input('input sentence: ')
    #encode the sentence with utf-8
    sentence = unicode(sentence, "utf-8")
    if sentence != 'tuichu':
        print 'results:'
        seg.segment(sentence)
    else:
        break
    print '\n'
