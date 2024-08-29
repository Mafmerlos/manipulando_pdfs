'''     
Manipulando arquivos .PDF com Python
    Mantendo o sistema de ler a documentacao e explorar ela para aprender
as diversas funções sobre a mesma

 - Documentação PyPDF2: https://pypdf2.readthedocs.io/en/3.x/
 - Aprender e colocar em pratica a manipulação de pdfs e extracao de imagens e texto de dentro dos mesmo
 - Criar um novo arquivo em PDF e se aprofundar no uso dessa bibliteca, pois é um assunto relevante em diversas áreas.

ORGANIZAÇÃO DOS ESTUDOS:
* Primeiro realizei a leitura da documentação e assisti videos para aprender sobre o uso da biblioteca
* Logo após comecei a colocar a mão na massa criando os caminhos dos arquivos e pastas para salvar
* Aprendi a ler o arquivo PDF, extrair textos e imagens dos mesmos
* Aprendi a criar documentos PDF e escrever dentro dos mesmos 

CONCLUSÃO: 
    Todo o estudo da biblioteca so me trouxeram pensamentos positivos sobre a importancia disso e que em algum 
    momento da minha carreira isso vai ser util, alem de que é sempre bom estar em constante aprendizado. Seguimos!! 
'''




from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter , PdfMerger

# Aprendendo a manipular os caminhos para fazer a leitura do PDF
PASTA_RAIZ = Path(__file__).parent
PASTA_DOC = PASTA_RAIZ /'pdf_original'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

ARQUIVOS = PASTA_DOC / '123.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

# Lendo o arquivo PDF
leitor = PdfReader(ARQUIVOS)

# Printando o numero de paginas que contem no PDF
    # print(len(leitor.pages))

# Percorrendo as paginas e printando o conteudo 
    #for page in leitor.pages:
       # print(page)
       # print()

# Extraindo textos das páginas
page0 = leitor.pages[0]
    #imagem0 = page0.images[0]
    #print(page0.extract_text())

# Extraindo imagem e salvando na pasta criada acima
    #with open(PASTA_NOVA/ imagem0.name,'wb') as fp:
     #fp.write(imagem0.data) 

# Percorrendo as imagens e salvando todas elas na pasta escolhida 
count = 0

for image_file_object in page0.images:
    with open(PASTA_NOVA / image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)
        count += 1

# Criando apenas uma imagem do pdf principal em um novo PDF
# Se for preciso copiar as paginas todas apenas realizar um for e salvar em um novo pdf da mesma forma
writer = PdfWriter()
writer.add_page(page0)

with open(PASTA_NOVA / 'criando_pdf.pdf','wb') as arq:
    writer.write(arq)

# Como unir arquivos pdf separados com PdfMerger
files =  [
    PASTA_DOC/ '123.pdf',
    PASTA_DOC / 'Curriculo.Teste.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(str(file))

merger.write(PASTA_NOVA / 'merged.pdf')
merger.close()