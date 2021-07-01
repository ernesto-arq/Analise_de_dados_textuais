# -*- coding: utf-8 -*-
"""Analise_dados_textuais_11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gjD46TA0FmoFjfO3WCDuhfkXPQKsvtDW

Nome: Ernesto Gurgel Valente Neto

> Disciplina: Analise de Dados Textuais
"""

import nltk
import math
import numpy
nltk.download('punkt')

"""# **Importando os arquivos de trabalho**"""

dataset = {
    "tfidf_1.txt":open("tfidf_1.txt").read(),
    "tfidf_2.txt":open("tfidf_2.txt").read(),
    "tfidf_3.txt":open("tfidf_3.txt").read(),
    "tfidf_4.txt":open("tfidf_4.txt").read(),
    "tfidf_5.txt":open("tfidf_5.txt").read(),
    "tfidf_6.txt":open("tfidf_6.txt").read(),
    "tfidf_7.txt":open("tfidf_7.txt").read(),
    "tfidf_8.txt":open("tfidf_8.txt").read(),
    "tfidf_9.txt":open("tfidf_9.txt").read(),
    "tfidf_10.txt":open("tfidf_10.txt").read() }

len(dataset)

dataset

dataset['tfidf_1.txt']

"""# **Criar uma frequencia de termos em documento**"""

def tf(dataset, file_name):
    text = dataset[file_name]
    tokens = nltk.word_tokenize(text)
    fd = nltk.FreqDist(tokens)
    return fd

"""# **Função apra calcular o inverso da frequencia do termo de cada docuemtno**"""

# Calcular o inverso da frequencia de um termo em determinado documento
def idf(dataset, term):
    count = [term in dataset[file_name] for file_name in dataset]
    inv_df = math.log(len(count)/sum(count))
    return inv_df

"""# **Criar a função do Term Frequenci, Inverse Documetn Frequency**"""

def tfidf(dataset, file_name, n):
    term_scores = {}
    file_fd = tf(dataset,file_name)
    for term in file_fd:
        if term.isalpha():
            idf_val = idf(dataset,term)
            tf_val = tf(dataset, file_name)[term]
            tfidf = tf_val*idf_val
            term_scores[term] = round(tfidf,2)
    return sorted(term_scores.items(), key=lambda x:-x[1])[:n]

tfidf(dataset,"tfidf_1.txt",1)

tfidf(dataset,"tfidf_1.txt",10)

tfidf(dataset,"tfidf_1.txt",10)

for file_name in dataset:
    print("{0}: \n {1} \n".format(file_name, tfidf(dataset,file_name,5)))

"""# Similaridade de textos"""

nltk.download('stopwords')

#nltk.corpus.stopwords.words("portuguese")
#ja incluso no pacote

"""extracao de palavras"""

#funcao ajuda nos trabalhos
def word_extraction(sentence):    
  ignore = nltk.corpus.stopwords.words("english") 
  words = nltk.word_tokenize(sentence)  
  cleaned_text = [w.lower() for w in words if w not in ignore]    
  return cleaned_text

#normalizando todas as sentenças em letra minuscula
def word_normalize(sentence):
  return [word.lower() for word in sentence if word.isalpha()]

#quebrar as frases em sentensas processo de tokenização
def tokenize(sentence):
  tokens = nltk.word_tokenize(sentence)
  return tokens

#tokenizar as sentenças, uma lista com as palavras tokenizadas
#imoporntate para montar vetores de palavras e elas estarao alinhadas novetor em questao da similaridade
def tokenize_sent(sentences):    
  words = []    
  for sentence in sentences:       
    w = word_extraction(sentence)        
    words.extend(w)            
    words = sorted(list(set(words)))    
    return words

def generate_bow(allsentences):        
  vocab = tokenize(allsentences)    
  print("Word List for Document \n{0} \n".format(vocab));
  for sentence in allsentences:        
    words = word_normalize(sentence)        
    bag_vector = numpy.zeros(len(vocab))        
    for w in words:            
      for i,word in enumerate(vocab):                
        if word == w:                    
          bag_vector[i] += 1                           
          print("{0}\n{1}\n".format(sentence,numpy.array(bag_vector)))

allsentences1 = ["Joe waited for the train train"]

generate_bow(str(allsentences1))

allsentences2 = ["Joe waited for the train train", "The train was late", "Mary and Samantha took the bus"]

generate_bow(str(allsentences2))

"""# **Utilizando a funcao do Sklearn para fazer as mesmas coisas**"""

from sklearn.feature_extraction.text import CountVectorizer

corpus = [
'All my cats in a row',
'When my cat sits down, she looks like a Furby toy!',
'The cat from outer space',
'Sunshine loves to sit like this for some reason.'
]

vectorizer = CountVectorizer()

print(vectorizer.fit_transform(corpus).todense())

print(vectorizer.vocabulary_)

"""*Distância* Jaccard"""

#poderiamos normalizar ou tokenizar, visto que essa funcao so compara palavras iguais
def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

get_jaccard_sim("All my cat in a row", "The cats from outer space")

def cos_sim(a, b):
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)

from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import CountVectorizer

from collections import Counter

"""# **Distancia Cosseno**


"""

def get_cosine_sim(*strs): 
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)

def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()

get_vectors("All my cat in a row", "The cats from outer space")

#Comparando duas sentenças
get_cosine_sim("All my cat in a row", "The cats from outer space")

#Comparando duas sentenças
lista = get_cosine_sim("All my cat in a row", "The cats from outer space")

#Comparando duas sentenças
lista[0:]

"""# **Fim da lista**"""