import pandas as pd
import os
"""
		0  author
		1  link
		2  category
		3  date of publication
		4  number of tokens
		5  number of words without punctuation
		6  number of types
		7  number of links inside the news
		8  number of words in upper case
		9  number of verbs
		10 number of subjuntive and imperative verbs
		11 number of nouns
		12 number of adjectives
		13 number of adverbs
		14 number of modal verbs (mainly auxiliary verbs)
		15 number of singular first and second personal pronouns
		16 number of plural first personal pronouns
		17 number of pronouns
		18 pausality
		19 number of characters
		20 average sentence length
		21 average word length
		22 percentage of news with speeling errors
		23 emotiveness
		24 diversity
"""
#df = pd.read_csv('../Fake.br-Corpus-master/full_texts/fake-meta-information/1-meta.txt', header=None)

#print(df)

novo = pd.DataFrame()

# percorre o diretorio para ler cada um dos arquivos
for caminho, diretorio, arquivo in os.walk('../Fake.br-Corpus-master/full_texts/fake-meta-information'):
    #print('caminho....: ', caminho)        #print('diretório..: ', diretorio)
    cont = 0
    #row terá o nome de cada arquivo lido do diretório
    for row in arquivo:
        arq = caminho + '/' + row
        # lê cada arquivo, lê o conteúdo e armazena cada parte do arquivo
        df = pd.read_csv(arq, header=None)
        data = {'author': df[0][0],
                'link': df[0][1],
                'category': df[0][2],
                'date_of_publication': df[0][3],
                'number_of_tokens': df[0][4],
                'number_of_words_without_punctuation': df[0][5],
                'number_of_types': df[0][6],
                'number_of_links_inside_the_news': df[0][7],
                'number_of_words_in_upper_case': df[0][8],
                'number_of_verbs': df[0][9],
                'number_of_subjuntive_and_imperative_verbs': df[0][10],
                'number_of_nouns': df[0][11],
                'number_of_adjectives': df[0][12],
                'number_of_adverbs': df[0][13],
                'number_of_modal_verbs': df[0][14],
                'number_of_singular_first': df[0][15],
                'number_of_plural_first': df[0][16],
                'number_of_pronouns': df[0][17],
                'pausality': df[0][18],
                'number_of_characters': df[0][19],
                'average_sentence_length': df[0][20],
                'average_word_length': df[0][21],
                'percentage_of_news': df[0][22],
                'emotiveness': df[0][23],
                'diversity': df[0][24]




        }
        # cria um DataFrame baseado no data
        n1 = pd.DataFrame(data, index=[cont],  columns=['author','link','category','date_of_publication','number_of_tokens','number_of_words_without_punctuation','number_of_types','number_of_links_inside_the_news','number_of_words_in_upper_case','number_of_verbs','number_of_subjuntive_and_imperative_verbs','number_of_nouns','number_of_adjectives','number_of_adverbs','number_of_modal_verbs','number_of_singular_first','number_of_plural_first','number_of_pronouns','pausality','number_of_characters','average_sentence_length','average_word_length','percentage_of_news','emotiveness','diversity'])
        #adiciona o dataframe n1 ao novo
        novo = novo.append(n1)
        cont += 1

# gera o arquivo csv com os dados para análise
novo.to_csv('../arquivo.csv', sep=';')







