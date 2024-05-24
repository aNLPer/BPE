
def get_stats(ids, counts=None):
    """
    统计的token序列
    ids = [1,2,3,1,2] ===> {(1,2):2, (2,3):1, (3,1):1} 
    """
    counts = {} if counts is None else counts
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0)+1
    return counts

def merge(ids, pair, idx):
    """
    将ids中出现的pair用idx取代
    Args:
        ids (_type_): token sequence
        pair (_type_): pair to be merged by idx
        idx (_type_): idx to replace pair
    e.g., ds = [1,2,3,1,2]; pair = (1,2) idx = 4
    ds = [1,2,3,1,2] ===> ds=[4,3,4]
    """
    new_ids = []
    i = 0
    while i<len(ids):
        if ids[i]==pair[0] and ids[i+1]==pair[1] and i<len(ids)-1:
            new_ids.append(idx)
            i+=2
        else:
            new_ids.append(ids[i])
            i+=1
    return new_ids

class Tokenizer:
    """Tokenizer 的父类"""
    def __init__(self) -> None:
        pass
    
    # 训练
    def train(self, corpus):
        pass
    
    # 编码
    def encode(self):
        pass
    
    # 解码
    def decode(self):
        pass
    
    # 存储
    def save(self):
        pass
    
    # 加载
    def load(self):
        pass
    