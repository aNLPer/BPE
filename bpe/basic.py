from base import Tokenizer

class BasicTokenizer(Tokenizer):
    
    def __init__(self) -> None:
        super().__init__()
        
    def train(self, corpus, vocab_size, verbose):
        assert vocab_size >= 256
        num_merges = vocab_size-256

        ids = list(corpus.encode("utf-8"))
        
        for i in range(num_merges):
            pass
        

