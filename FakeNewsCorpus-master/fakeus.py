import pandas as pd
import os
"""
                0 id
                1 domain
                2 type
                3 url
                4 content
                5 scraped_at
                6 inserted_at
                7 updated_at
                8 title
                9 authors
                10 keywords
                11 meta_keywords
                12 meta_description
                13 tags
                14 summary
                15 source
"""
#df = pd.read_csv('../Fake.br-Corpus-master/full_texts/fake-meta-information/1-meta.txt', header=None)

#print(df)

novo = pd.DataFrame()

# percorre o diretorio para ler cada um dos arquivos
for caminho, diretorio, arquivo in os.walk('news_sample.csv'):
    #print('caminho....: ', caminho)        #print('diretório..: ', diretorio)
    cont = 0
    #row terá o nome de cada arquivo lido do diretório
    for row in arquivo:
        arq = caminho + '/' + row
        # lê cada arquivo, lê o conteúdo e armazena cada parte do arquivo
        df = pd.read_csv(arq, header=None)
        data = {'id': df[0][0],
                'domain': df[0][1],
                'type': df[0][2],
                'url': df[0][3],
                'content': df[0][4],
                'scraped_at': df[0][5],
                'inserted_at': df[0][6],
                'updated_at': df[0][7],
                'title': df[0][8],
                'authors': df[0][9],
                'keywords': df[0][10],
                'meta_keywords': df[0][11],
                'meta_description': df[0][12],
                'summary': df[0][13],
                'source': df[0][14],

        }
        # cria um DataFrame baseado no data
        n1 = pd.DataFrame(data, index=[cont],  columns=['id','domain','type','url','content','scraped_at','inserted_at','updated_at','title','authors','keywords','meta_keywords','meta_description','summary','source'])
        #adiciona o dataframe n1 ao novo
        novo = novo.append(n1)
        cont += 1

# gera o arquivo csv com os dados para análise
novo.to_csv('../arquivo.csv', sep=',')