class ShakespeareStream():
    def __init__(self, algorithms):
        self.algorithms = algorithms

    def stream(self, path, work):
        with open(path + '/' + str(work) + '.txt', 'r') as f:
            text = f.read()
            words = text.split(' ')
            for word in words:
                for algorithm in self.algorithms:
                    algorithm.process(word.replace("'", '').lower())

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