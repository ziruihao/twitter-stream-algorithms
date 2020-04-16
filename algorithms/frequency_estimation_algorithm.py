import abc

class FrequencyEstimationAlgorithm(abc.ABC):
    def __init__(self):
        super().__init__()
        self.freqs = {}
        self.stream_length = 0

    @abc.abstractmethod
    def process(self, token):
        pass

    @abc.abstractmethod
    def query(self, query):
        pass

    @abc.abstractmethod
    def query_all(self):
        pass

