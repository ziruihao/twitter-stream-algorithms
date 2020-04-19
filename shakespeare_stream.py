class ShakespeareStream():
    def __init__(self, limit, algorithms):
        self.algorithms = algorithms
        self.limit = limit

    def stream(self, path):
        work = 1
        while (self.limit > 0 and work <= 219):
            with open(path + '/' + str(work) + '.txt', 'r') as f:
                text = f.read()
                words = text.split(' ')
                while (self.limit > 0 and len(words) > 0):
                    word = words.pop(0)
                    if (word not in ['rt', ' ', ' ']):
                        self.limit += -1
                        print(word.replace("'", '').lower())
                        for algorithm in self.algorithms:
                            algorithm.process(word.replace("'", '').lower())
            work += 1

    def extract(self, path):
        with open(path, 'r') as f_r:
            text = f_r.read()
            works = text.split('@')
            for i, work in enumerate(works):
                with open('shakespeare/' + str(i) + '.txt', 'w') as f_w:
                    work = work.replace('\n', ' ').replace('  ', '')
                    print(len(work))
                    f_w.write(work)
                    f_w.close()