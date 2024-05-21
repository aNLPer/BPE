# 打印字符的unicode code point 
text = """在Python中处理文本数据是使用str对象，也称为字符串。字符串是由Unicode码位构成的不可变序列。如果给出了关键字参数，则关键字参数及其值会被加入到基于位置参数创建的字典。 如果要加入的键已存在，来自关键字参数的值将替代来自位置参数的值。
The tokens with 0 frequency count have been removed from the table. We can now see that the total token count is 11, which is less than our initial count of 12. This is a small corpus but in practice, the size reduces a lot. This list of 11 tokens will serve as our vocabulary.
You must have also noticed that when we add a token, either our count increases or decreases or remains the same. In practice, the token count first increases and then decreases. The stopping criteria can be either the count of the tokens or the number of iterations. We choose this stopping criterion such that our dataset can be broken down into tokens in the most efficient way.
"""
print("-------")
print("text:")
print(text)
print(f"length:{len(text)}")

tokens = list(text.encode("utf-8"))
print("-------")
print("tokens:")
print(tokens)
print(f"length:{len(tokens)}")

def get_stats(ids):
    # 计算pair出现的频率
    counts = {}
    for pairs in zip(ids, ids[1:]):
        counts[pairs] = counts.get(pairs, 0)+1
    return counts

# stats = get_stats(tokens)
# print(stats)
# print(sorted(((v,k) for k, v in stats.items()), reverse=True))
# print(chr(32),chr(116))
# 获取频率最高的pair
# top_pair = max(stats, key=stats.get)
# print(top_pair)

def merge(ids, pair, idx):
    # 用idx替换ids中出现的pair
    newids = []
    i = 0
    while i<len(ids):
        if i<len(ids)-1 and ids[i]==pair[0] and ids[i+1]==pair[1]:
            newids.append(idx)
            i+=2
        else:
            newids.append(ids[i])
            i+=1
    return newids
# 用idx替换tokens中出现频率最高的pair
# new_tokens = merge(ids=tokens, pair=top_pair, idx=1000)
# print(new_tokens)
# print(f"length:{len(new_tokens)}")

# bpe 算法训练词汇表
vocab_size = 300 # 目标此词汇表大小
merge_iter = vocab_size-256 # 需要迭代merge的次数，为什么是-256？因为经过utf-8编码后，每个字符编码为1~4个byte，每个byte表示范围为0~255
ids = list(tokens) # 保留utf-8编码的token

merge_rec = {} # 记录mrege的token
for i in range(merge_iter):
    stats = get_stats(ids) # 统计当前pair的频率
    top_pair = max(stats, key=stats.get) # 频率最大的pair
    idx = 256+i
    print(f"merge {top_pair} with {idx}")
    ids = merge(ids, top_pair, idx)
    merge_rec[top_pair] = idx
print(merge_rec)
print(len(set(ids)))
print(len(set(tokens)))
print(f"compression ratio: {len(tokens)/len(ids)}") # 同一片文档，uft-8编码后的长度是bpe算法压缩后长度的1.5倍


