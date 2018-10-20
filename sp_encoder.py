import sentencepiece as sp
import codecs
import sys

spm = sp.SentencePieceProcessor()
spm.Load("./model_en_de/sentencepiece.model")

print(sys.argv[0], sys.argv[1], sys.argv[2])
text = codecs.open(sys.argv[1], "r", encoding = 'utf8').read()

toks = spm.EncodeAsPieces(text)
with codecs.open(sys.argv[2], "w", encoding='utf8') as f:
  for t in toks:
    f.write(t + " ")