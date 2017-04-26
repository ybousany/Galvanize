def main():
    print 'Inside reportgen'
    report = create_report('sample.txt') #have file name
    print report


def create_report(fn):
    counts_d = {'words': 0, 'characters': 0}
    with open (fn) as txt_file: #open file
        for raw_line in txt_file:
            line = raw_line.strip()
            words = line.split()
            characters = len(line)
            counts_d['words'] += len(words)
            counts_d['characters'] += characters
        return counts_d

if __name__=='__main__':
    main()
