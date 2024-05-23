# Tokenization

Tokenization in simple words is the process of splitting a phrase, sentence, paragraph, one or multiple text documents into smaller units. Each of these smaller units is called a token. Now, these tokens can be anything — a word, a subword, or even a character. Different algorithms follow different processes in performing tokenization but the below given example will give you a basic idea about the difference between these three.

Word-based 算法将apples和apple看作不同的token这种策略将使得词汇表非常的庞大；Character-based的算法将a,b,c...视为一个token，虽然词汇表规模大大减小，但损失了word的语义信息。从大模型角度考虑，Character-based 虽然词减少了汇表的大小，但是输入的sequence长度增加了（一个word需要多个表示向量），那么attention的计算量增加了，这对于LLM是不可接受的；subword在两者之间取折中，例如常用的BPE算法迭代的将当前corpus中频率最高的byte pair组成新的token，这个过程会增加词汇表的大小，但是会降低输入sequence的长度。另一方面其实，tokenization可以看作一个文本压缩算法，但是既要考虑压缩效率，又要考虑到模型的训练。

## Subword-based

The subword-based tokenization algorithms uses the following principles.

1. Do not split the frequently used words into smaller subwords.
   
2. Split the rare words into smaller meaningful subwords.

### Byte-Pair Encoding（BPE）

BPE算法是一个迭代算法，首先对文本进行编码，比如利用utf-8将每个字符编码为由1\~4个byte的字节流，每个byte的范围为0\~255，然后每次迭代将，出现频率最高的两个byte（byte pair）合并赋予新的编号（大于255），直到满足终止条件（迭代次数，词汇表大小）。具体实现参考`intro_bpe.py`

**总结：**

根据BPE算法我们知道，当训练tokenizer的数据中包含了95%英文，5%的中文，那么根据频率merge的过程大多集中在英文token，这样的偏斜数据上训练出来的tokenizer会相对拉长中文文本缩短英文文本，导致Tansformer训练中文的计算量相对大，而且对于上下文有限的LM来说能学习的中文上下文长度更短，如果训练LM的数据集中中文的占比也很少，那么这个LM在中文任务上表现应该不好。由于tokenizer和LLM的训练是分两步完成的，所以从该角度来说LLM的构建过程不是end-2-end。

**参考：**

[Word, Subword, and Character-Based Tokenization: Know the Difference](https://towardsdatascience.com/word-subword-and-character-based-tokenization-know-the-difference-ea0976b64e17)


[Byte-Pair Encoding: Subword-based tokenization algorithm](https://towardsdatascience.com/byte-pair-encoding-subword-based-tokenization-algorithm-77828a70bee0)

[karpathy's code](https://github.com/karpathy/minbpe)


## Sub

### WordPiece


### Unigram


### SentencePiece
