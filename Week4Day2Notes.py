from collections import Counter
import operator
import string

class SuperReport():
    def __init__(self):
        self._master_counter = Counter(words = 0, characters = 0, sentences = 0)
        self._vocabulary_d = {}

    def update_counts_for_line(self, line):
        self._master_counter['characters'] += len(line)
        words = line.split()
        self._master_counter['words'] += len(words)
        self._master_counter['sentences'] += line.count('.')
        self._master_counter['sentences'] += line.count('?')
        self._master_counter['sentences'] += line.count('!')
        for w in words:
            no_punctuation = w.translate(None, string.punctuation)
            key = no_punctuation.lower()
            if key in self._vocabulary_d:
                self._vocabulary_d[key] += 1
            else:
                self._vocabulary_d[key] = 1

    def create_report(self, filename):
        with open(filename) as txt_file:
            for raw_line in txt_file:
                line = raw_line.strip()
                self.update_counts_for_line(line)
        return self._master_counter, self._vocabulary_d

if __name__ == '__main__':
    sr = SuperReport()
    counts, words_d = sr.create_report('sample.txt')
    sorted_vocabulary = sorted(words_d.items(), key = operator.itemgetter(1))
    print len(sorted_vocabulary)
    for count in sorted_vocabulary:
        print count
    print counts
