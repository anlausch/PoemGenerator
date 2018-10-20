import sentencepiece as sp
import codecs
import sys

spm = sp.SentencePieceProcessor()
spm.Load("./model_en_de/sentencepiece.model")

print(sys.argv[0], sys.argv[1], sys.argv[2])
lines = codecs.open(sys.argv[1], "r", encoding = 'utf8').readlines()
decoded_lines = []
for l in lines:
  decoded_lines.append(spm.DecodePieces(l.split()))

with codecs.open(sys.argv[2], "w", encoding='utf8') as f:
  for dl in decoded_lines:
    f.write(dl + "\n")