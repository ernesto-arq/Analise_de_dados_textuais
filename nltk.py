# -*- coding: utf-8 -*-
"""NLTK.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EG2drjf7uh7_GoIoU2_r7lowtMlHoilQ
"""

import nltk

from nltk.corpus import machado, mac_morpho, floresta, genesis

nltk.download('machado')
nltk.download('mac_morpho')
nltk.download('floresta')
nltk.download('genesis')

machado.fileids

machado.fileids()

from nltk.text import Text

ptext1 = Text(machado.words('romance/marm05.txt'), name="Memórias Póstumas de Brás Cubas (1881)")

ptext1.vocab()

words_machado = machado.words('romance/marm05.txt')

words_machado

len(words_machado)

nltk.download('punkt')

sents_machado = machado.sents('romance/marm05.txt')

len(sents_machado)

sents_machado

texto = 'Existem teorias que defendem que antes das explorações do Império Português, houve duas passagens de espanhóis pelo litoral da atual Fortaleza. Os navegadores Vicente Yáñez Pinzón e Diego de Lepe teriam desembarcado nas costas cearenses antes da viagem de Pedro Álvares Cabral ao Brasil em 1500, embora, na versão tradicional, o desembarque de Pinzón tenha se dado no Cabo de Santo Agostinho em Pernambuco. Pinzón teria chegado no cabo que se acredita ser o Mucuripe e Lepe aportado na barra do rio Ceará. Tais descobertas de território não poderiam ser oficializadas em decorrência do Tratado de Tordesilhas, de 1494. A chegada de Pinzón ao Mucuripe foi, por várias vezes, desconsiderada como um dos possíveis pontos de descobrimento pré-cabralino do país'

texto

from nltk import tokenize

palavras_tokenize = tokenize.word_tokenize(texto, language='portuguese')

palavras_tokenize

sentence_tokenize = tokenize.sent_tokenize(texto,language='portuguese')

sentence_tokenize

from nltk.corpus import stopwords

nltk.download('stopwords')

lista_stop = stopwords.words('portuguese')

lista_stop

nltk.download('rslp')

stemmer = nltk.stem.RSLPStemmer()

stemmer.stem('copiar')

stemmer.stem('casar')

for words in palavras_tokenize:
  print(stemmer.stem(words))

import joblib

tagger = joblib.load('POS_tagger_brill.pkl')

phrase = 'O rato roeu a roupa do rei de Roma'

phrase

tagger.tag(tokenize.word_tokenize(phrase))

tagger.tag(tokenize.word_tokenize(sentence_tokenize[0]))

import pandas as pd
import altair as alt

url_df = 'belchior.csv'
df = pd.read_csv(url_df)

df.head()

len(df)

pts = alt.selection(type="interval", encodings=["x"])

rowbars = alt.Chart(df).mark_bar().encode(
    x='tamanho:Q',
    y= alt.Y('titulo:O', sort = alt.EncodingSortField(field="tamanho", order='descending')),   
    color = 'maisTocada:O',
    tooltip=['titulo', 'tamanho', 'keywords','letra']
).transform_filter(
    pts
).properties(    
    height=700,
    width = 300,
    title = 'Quantidade de palavras por música'
)


hist = alt.Chart(df).mark_bar().encode(
    x = alt.X('hbin:N',title='Quantidade de palavras'),
    y = alt.Y('count()',title='Contagem'),
    tooltip = [alt.Tooltip('count():Q', title='Contagem de letras'),
               alt.Tooltip('mbin:N', title='Quantidade de palavras')],
    color = alt.condition(pts, alt.value("steelblue"), alt.value("lightgray"))
).properties(
    height = 320,
    width = 320,
    title = 'Histograma da quantidade de palavras por música'
).add_selection(pts)

hconcat = alt.hconcat(
    rowbars,
    hist,
    data=df
).transform_bin(
    "hbin",
    field="tamanho",
    bin=alt.Bin(maxbins=50)
)

#hconcat = rowbars | hist

hconcat.save('1_tamanho_musicas.html')
hconcat

url_df_freq = 'belchior_dist_freq.csv'
df_freq = pd.read_csv(url_df_freq)
df_freq = df_freq.sort_values(by='frequencia',ascending=False)
df_freq.head()

df_freq50 = df_freq[0:50]

wordfreq = alt.Chart(df_freq50).mark_bar().encode(
    y='frequencia:Q',
    x= alt.X('termo:O', sort = alt.EncodingSortField(field="frequencia", order='descending')),
    color = alt.value('steelblue'),
    tooltip=[
        'termo:O',
        'frequencia:Q',
        alt.Tooltip('musicas:O', title='Letras onde o termo ocorre')
    ]
).properties(    
    height=300,
    width = 850,
    title = '50 termos mais frequentes'
)

wordfreq.save('2_frequencia_termos.html')
wordfreq

url_sim = 'belchior_similaridade.csv'

df_sim = pd.read_csv(url_sim)

df_sim.head()

source = df_sim.melt(id_vars=['titulo'])

alt.data_transformers.disable_max_rows()

matrix_sim = alt.Chart(source).mark_rect().encode(
    x='titulo:O',
    y='variable:O',
    color=alt.Color('value:Q', scale=alt.Scale(scheme="inferno")),
    tooltip=[
        alt.Tooltip('variable:O', title='Letra A'),
        alt.Tooltip('titulo:O', title='Letra B'),
        alt.Tooltip('value:Q', title='Similaridade'),
    ]
).properties(    
    width = 600,
    height= 600,    
    title = 'Matriz de similaridade entre letras'
)
matrix_sim.save('4_similaridade_musicas.html')
matrix_sim

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

todas_keywords = ''
for keyword in list(df['keywords']):
    todas_keywords += keyword + ', '
todas_keywords = todas_keywords[0:-2]
todas_keywords

def normalize_text(txt):
    txt = txt.lower()
    txt = txt.replace(',','')
    txt = txt.replace(';','')
    txt = txt.replace('.','')
    #txt = txt.replace('\'','')
    txt = txt.replace('(','')
    txt = txt.replace(')','')
    txt = txt.replace(':','')
    txt = txt.replace('!','')
    txt = txt.replace('?','')
    txt = txt.replace("\\","")
    txt = txt.replace("\"","")
    txt = txt.replace("`","")
    txt = txt.replace('</p>','')
    return txt

todas_letras = ' '.join(list(df['letra']))
todas_letras = normalize_text(todas_letras)
todas_letras

import matplotlib.pyplot as plt

wordcloud = WordCloud(background_color="white",width = 800, height = 600).generate(todas_letras)
wordcloud.to_file("wordcloud.png")

plt.figure(figsize=(15,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

brush = alt.selection(type='interval')

pts = alt.selection(type="interval", encodings=["x"])

points = alt.Chart(df).mark_circle().encode(
    x='polaridade:Q',
    y='subjetividade:Q',
    color=alt.condition(brush, 'sentimento:N', alt.value('lightgray')),
    tooltip=['titulo','polaridade','subjetividade','letra'],
    size='tamanho:Q'
).properties(    
    title = 'Polaridade x Subjetividade'
).add_selection(
    brush
).transform_filter(
    pts
)

bars = alt.Chart(df).mark_bar().encode(
    y=alt.Y('sentimento:N', title = 'Categorias'),
    color='sentimento:N',
    x=alt.X('count(sentimento):Q', title = 'Contagem'),
    tooltip = [alt.Tooltip('count():Q', title='Contagem')],
).properties(    
    title = 'Categorias de Polaridade'
).transform_filter(
    brush
).transform_filter(
    pts
)

hist_pol = alt.Chart(df).mark_bar().encode(
    x = alt.X("polaridade:Q", bin=alt.Bin(maxbins=30),title = 'polaridade'),
    y =alt.Y('count()',title='Contagem'),
    tooltip = [alt.Tooltip('count():Q', title='Contagem')],
    color = alt.condition(pts, 'sentimento:N', alt.value("lightgray"))
).properties(    
    width = 320,
    height = 200,
    title = 'Histograma da polaridade'
).add_selection(pts)


hist_sub = alt.Chart(df).mark_bar().encode(
    x = alt.X("subjetividade:Q", bin=alt.Bin(maxbins=30),title = 'subjetividade'),
    y =alt.Y('count()',title = 'Contagem'),
    tooltip = [alt.Tooltip('count():Q', title='Contagem')],
    color = alt.condition(pts, alt.value("lightblue"), alt.value("lightgray"))
).properties(    
    width = 320,
    height = 200,
    title = 'Histograma da subjetividade'
).add_selection(pts)

sent = alt.hconcat(
    points & bars,
    hist_pol & hist_sub,
    data=df
)

pol = alt.Chart(df).mark_bar().encode(
    y="polaridade:Q",
    x= alt.X("titulo:O", sort = alt.EncodingSortField(field="polaridade", order='descending')),
    tooltip = ['titulo','polaridade','letra'],
    color= 'sentimento'
).properties(
    width=800,
    height = 300,
    title = 'Polaridade das letras'
).transform_filter(
    pts
)

sent = ((points & bars) | (hist_sub & hist_pol)) & pol
sent.properties(title = 'Análise de Sentimentos')
sent.save('5_sentimentos.html')
sent