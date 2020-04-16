import abc

class FrequencyEstimationAlgorithm(abc.ABC):
    def __init__(self):
        super().__init__()
    
    @abc.abstractmethod
    def initialize(self):
        self.est_freqs = {}
        self.actual_freqs = {}
        self.stream_length = 0
        pass

    @abc.abstractmethod
    def process(self, token):
        pass

    @abc.abstractmethod
    def query(self, query):
        pass

