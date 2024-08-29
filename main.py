'''     
Manipulando arquivos .PDF com Python
    Estou explorando a manipulação de arquivos PDF usando Python, com foco na leitura da documentação e na prática para entender as funcionalidades da biblioteca PyPDF2.

 - Documentação PyPDF2: https://pypdf2.readthedocs.io/en/3.x/
 
OBJETIVOS:
Estudar e aplicar as funcionalidades da biblioteca PyPDF2.
Aprender a extrair imagens e textos de PDFs.
Criar novos arquivos PDF e se aprofundar no uso dessa biblioteca, dada sua relevância em várias áreas.

ORGANIZAÇÃO DOS ESTUDOS:
Leitura da Documentação: Iniciei com a leitura da documentação e assisti a vídeos explicativos para entender o uso da biblioteca.
Prática: Comecei a colocar em prática o que aprendi, criando os caminhos dos arquivos e pastas para salvar os resultados.
Extração de Conteúdo: Aprendi a ler arquivos PDF, extrair textos e imagens.
Criação de PDFs: Explorei a criação de documentos PDF e como escrever neles.

CONCLUSÃO: 
   Estudar a biblioteca PyPDF2 me trouxe pensamentos positivos sobre sua importância, e acredito que em algum momento da minha carreira esse conhecimento será útil.
   Além disso, é sempre gratificante estar em constante aprendizado. Seguimos em frente!!


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
