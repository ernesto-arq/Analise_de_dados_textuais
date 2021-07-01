# -*- coding: utf-8 -*-
"""Analise_dados_textuais_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UD6rJRSzkgtceiJ8XUGbwT1VSSDWRdMz

"Curso: Ciência de Dados"

---


"Disciplina: Analise de Dados Textuais"

---


"Alauno: Ernesto Gurgel Valente Neto"

---
Material: Lista 2
"""

print('Importação de Pacotes')
import nltk

nltk.download('gutenberg')

nltk.download('punkt')

nltk.corpus.gutenberg.fileids()

"""# **1- Questão**
Calcule os seguintes itens, Esse procedimento deve ser feito para os seguintes:

---
# **Textos**
1.   shakespeare-caesar.txt
2.   shakespeare-hamlet.txt
1.   shakespeare-macbeth.txt




"""

caesar = nltk.corpus.gutenberg.words('shakespeare-caesar.txt')
hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
macbeth = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')

"""# **a.   Número total de palavras**"""

print("Tamanho palavras livro Caesar:", len(caesar))
print("Tamanho palavras livro Hamlet:", len(hamlet))
print("Tamanho palavras livro Macbeth:", len(macbeth))

"""# **b.   Número total de sentenças**"""

sent_caesar = nltk.corpus.gutenberg.sents('shakespeare-caesar.txt')
sent_hamlet = nltk.corpus.gutenberg.sents('shakespeare-hamlet.txt')
sent_macbeth = nltk.corpus.gutenberg.sents('shakespeare-macbeth.txt')

print("Tamanho sentenças livro Caesar:", len(sent_caesar))
print("Tamanho sentenças livro Hamlet:", len(sent_hamlet))
print("Tamanho sentenças livro Macbeth:", len(sent_macbeth))

"""# **c.   Número total de palavras não repetidas**



"""

ceaser_dist = set(caesar)
print("Palavras Não Repetidas Livro Cesar:", ceaser_dist)
print("Palavras Não Repetidas Nº Livro Cesar:", len(ceaser_dist))

hamlet_dist = set(hamlet)
print("Palavras Não Repetidas Livro hamlet:", hamlet_dist)
print("Palavras Não Repetidas Nº Livro hamlet:", len(hamlet_dist))

macbeth_dist = set(macbeth)
print("Palavras Não Repetidas Livro macbeth:", macbeth_dist)
print("Palavras Não Repetidas Nº Livro macbeth:", len(macbeth_dist))

"""# **c.   Número total de palavras repetidas**"""

ceaser_pr = nltk.corpus.gutenberg.words("shakespeare-caesar.txt")
ceaser_pr
hamlet_pr = nltk.corpus.gutenberg.words("shakespeare-hamlet.txt")
hamlet_pr
macbeth_pr = nltk.corpus.gutenberg.words("shakespeare-macbeth.txt")
macbeth_pr

ceaser_prFreq = nltk.FreqDist(ceaser_pr)
hamlet_prFreq = nltk.FreqDist(hamlet_pr)
macbeth_prFreq = nltk.FreqDist(macbeth_pr)
#macbeth_prFreq

ceaser_prFreqResult = ceaser_prFreq.most_common()
hamlet_prFreqResult = hamlet_prFreq.most_common()
macbeth_prFreqResult = macbeth_prFreq.most_common()
#macbeth_prFreqResult

#Lista Palavras Repetidas Maior Que 1
ListaPP1 = []
ListaPP2 = []
ListaPP3 = []

ListaPP1 = [word[1] for word in ceaser_prFreqResult if word[1] > 1]
ListaPP2 = [word[1] for word in hamlet_prFreqResult if word[1] > 1]
ListaPP3 = [word[1] for word in macbeth_prFreqResult if word[1] > 1]

ListaPP1.append(ListaPP2)
ListaPP1.append(ListaPP3)

#n consigo fazer essa conversao de satan, porem ela daria a resposta da soma
#for i in range(0, len(ListaPP1)):
#  Sum = int(sum(ListaPP1[i]))

"""# **d.   Média de palavras por sentenças**"""

#Ceaser
for documents in nltk.corpus.gutenberg.fileids():
  words_total_caesar = len(nltk.corpus.gutenberg.words("shakespeare-caesar.txt"))
  sents_total_caesar = len(nltk.corpus.gutenberg.sents("shakespeare-caesar.txt"))
  mean_caesar = words_total_caesar/sents_total_caesar

print("Media de sentenças livro Caesar:", mean_caesar)

#hamlet
for documents in nltk.corpus.gutenberg.fileids():
  words_total_hamlet = len(nltk.corpus.gutenberg.words("shakespeare-hamlet.txt"))
  sents_total_hamlet = len(nltk.corpus.gutenberg.sents("shakespeare-hamlet.txt"))
  mean_hamlet = words_total_hamlet/sents_total_hamlet

print("Media de sentenças livro Hamlet:", mean_hamlet)

#macbeth
for documents in nltk.corpus.gutenberg.fileids():
  words_total_macbeth = len(nltk.corpus.gutenberg.words("shakespeare-macbeth.txt"))
  sents_total_macbeth = len(nltk.corpus.gutenberg.sents("shakespeare-macbeth.txt"))
  mean_macbeth = words_total_macbeth/sents_total_macbeth

print("Media de sentenças livro Macbeth:", mean_macbeth)

"""# **# 2- Questão**

---


Em relação ao corpus “gutenberg” implemente os algoritmos para responder às seguintes questões:

# **a.   Total de palavras em cada documento do corpus "gutenberg"**
"""

for documents in nltk.corpus.gutenberg.fileids():
  words_total = len(nltk.corpus.gutenberg.words(documents))

print("Total de Palavras de palavras gutenber:", words_total)

"""# **b.   Quem é o maior documento do corpus?**"""

documents_len = [(len(nltk.corpus.gutenberg.words(documents)), documents)
  for documents in nltk.corpus.gutenberg.fileids()]

print("MAIOR DOCUMENTO:", max(documents_len))

"""# **c.   Quem é o menor documento do corpus?**"""

print("MENOR DOCUMENTO:", min(documents_len))

"""# **d.   Calcular a média da quantida desentenças por palavras do corpus “gutenberg”**"""

for documents in nltk.corpus.gutenberg.fileids():
  words_total = len(nltk.corpus.gutenberg.words(documents))
  sents_total = len(nltk.corpus.gutenberg.sents(documents))
meand = words_total/sents_total

print("MEDIA SENTENCA POR PALAVRA DOS DOCUMENTOS:", meand)

"""# **e. Calcule a distribuição de frequência das palavras do livro "shakespeare-macbeth.txt".**


"""

macbethFreq = nltk.FreqDist('shakespeare-macbeth.txt')

print("Distribuição Fequencia palavras Macbeth:", macbethFreq)

macbethFreq

"""# **f. Calcule 5 palavras mais frequentes nesse corpus.**"""

for documents in nltk.corpus.gutenberg.fileids():
  freqcorpus = nltk.corpus.gutenberg.words(documents)

corpusFreq = nltk.FreqDist(freqcorpus)

print("Distribuição 5 mais Fequentes palavras Macbeth:", corpusFreq.most_common(5))

"""# **g. Mostre a diferença entre de palavras entre dois livros.  (shakespeare-caesar.txt, shakespeare-hamlet.txt)**"""

dif_words_ceaser = nltk.corpus.gutenberg.words("shakespeare-caesar.txt")
dif_words_hamlet = nltk.corpus.gutenberg.words("shakespeare-hamlet.txt")

dif_ceaser_hamlet = list(set(dif_words_ceaser) - set(dif_words_hamlet))

print("Diferença entre os dois livros:", dif_ceaser_hamlet)