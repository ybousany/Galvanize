from collections import Counter

class SuperReport():
    def __init__(self):
        self._master_counter = Counter(words = 0, characters = 0, sentences = 0)

    def update_counts_for_line(self, line):
        pass

    def create_report(self, filename):
        with open(filename) as txt_file:
            for raw_line in txt_file:
                line = raw_line.strip()
                self.update_counts_for_line(line)
        return self._master_counter

if __name__ == '__main__':
    sr = SuperReport()
    result = sr.create_report('sample.txt')
    print result              
