import abc
class AbstractStreamingAlgorithm(abc.ABC):
    def __init__(self):
        super().__init__()
        self.freqs = {}
        self.count = 0

    @abc.abstractmethod
    def process(self, token):
        pass

    @abc.abstractmethod
    def query(self, query):
        pass

    @abc.abstractmethod
    def query_all(self, id):
        pass

