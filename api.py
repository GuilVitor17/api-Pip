from distutils.log import debug
from importlib.resources import path
from multiprocessing.sharedctypes import Value
from unicodedata import name
from flask import Flask, render_template, request
from flask_cors import CORS
from pkg_resources import Requirement, require


app = Flask (__name__)
CORS(app)

app.config['JSON_AS_ASCII'] = False

livros_data = {

     1:{
        "id" : 1,
        "titulo" : "A Arte da Guerra",
        "autor" : "Sun Tzu",
        "capa" : "https://www.baixelivros.com.br/media/2019/04/arte-da-guerra-1.jpg",
        "Ano": "2010 – 1ª Edição",
        "Nº de Páginas" : "058",
        "Tipo" : "Livro Digital",
        "Formato" : ".pdf",
        "Licença" : "Domínio Público",
        "Descrição" : "Filósofo que se tornou general cujo nome individual era Wu, nasceu no Estado de Ch’i na China, próximo de 500 a.C., em um auge das ciências militares e legislativas daquele país. Sun Tzu escreveu a “Arte da Guerra”."
    },
    2:{
        "id" : 2,
        "Título": "O Filho do Impostor",
        "Autor": "Joe M.",
        "capa": "https://www.baixelivros.com.br/media/2019/04/o-filho-do-impostor.jpg",
        "Editora": "A.S.",
        "Ano": "1978 – 1ª Edição",
        "Nº de Páginas": "057",
        "Tipo": "Livro Digital",
        "Formato": ".pdf",
        "Licença": "Gratuito",
        "Descrição":
        "No decorrer da história ele acaba se envolvendo com um gangster da pesada chamado Murdock, que tem um bando de safados trabalhando pra ele e que aperta o cerco em torno de Dickson até que este aceita fazer alguns trabalhos pra ele.",
    },
    3:{
        "id" : 3,
       "Título": "Apenas Mais Uma Tentativa",
       "Autor": "Luana Karoline",
       "capa": "https://www.baixelivros.com.br/media/2019/10/apenas-mais-uma-tentaiva.jpg",
       "Editora": "Independente",
       "Ano": "2019 – 1ª Edição",
       "Nº de Páginas": "073",
       "Tipo": "Livro Digital",
       "Formato": ".pdf",
       "Licença": "Gratuito",
       "Descrição" :
       "Uma brasileira chamada Elizabeth entra em uma enrascada em Nova York, ela conhece um pintor mundialmente famoso chamado Aaron que lhe oferece ajuda, mas ela ira descobrir que esse homem gentil não é oque parece ser."


    },
    4:{
        "id" : 4,
        "capa" : "http://www.ebooksbrasil.org/eLibris/imagens/paraisoperdido.jpg",
        "Título": "Paraíso Perdido",
        "Autor": "John Milton",
        "Coleção": "Clássicos da Literatura",
        "Instituição": "eBooks Brasil",
        "Ano": "1856 – 1ª Edição",
        "Nº de Páginas": "554",
        "Tipo": "Livro Digital",
        "Formato": ".pdf",
        "Licença": "Domínio Público",
        "Descrição":
        "Ela o toca, ela o arranca, e logo o come. A terra estremeceu com tal ferida; Desde os cimentos seus a natureza. Pela extensão das maravilhas suas. Aflita suspirou, sinais mostrando. Da ampla desgraça e perdição de tudo."


    },
    5:{
        "id" : 5,
        "capa" : "https://m.media-amazon.com/images/I/41r-Z0sbizL.jpg",
        "Título": "O Cortiço",
        "Autor": "Aluísio Azevedo",
        "Instituição": "Edições Câmara",
        "ISBN": "978-85-402-0791-2",
        "Ano": "2019 – 2ª Edição",
        "Nº de Páginas": "233",
        "Tipo": "Livro Digital",
        "Formato": ".pdf",
        "Licença": "Gratuito",
        "Descrição":
        "A obra-prima de Aluísio de Azevedo, O Cortiço, é a principal referência da estética realista-naturalista na literatura brasileira. Ambição e exploração se misturam nessa envolvente e sombria história de uma habitação coletiva da capital do Segundo império"

    },
      6:{
        "id" : 6,
        "capa" : "https://m.media-amazon.com/images/I/41OVopCAXiL.jpg",
    "Título": "Senhora",
    "Autor": "José de Alencar",
    "Instituição": "Câmaras Edições",
    "Ano": "2019 – 1ª Edição",
    "Nº de Páginas": "255",
    "ISBN": "978-85-402-0774-5",
    "Tipo": "Livro Digital",
    "Formato":  ".pdf",
     "Licença": "Gratuito",
     "Descrição":
     "Uma das obras mais românticas da literatura nacional, Senhora, de José de Alencar, apresenta como protagonista Aurélia Camargo, mulher de caráter firme e personalidade imperiosa, que aos dezoito anos já é dona de si." ,
    
},

 7:{
        "id" : 7,
        "capa" : "https://www.baixelivros.com.br/media/2019/02/romeu-e-julieta.jpg",
        "Título": "Romeu e Julieta",
"Autor": "William Shakespeare",
"Editora": "JAHR",
"Ano": "1595 – 1ª Edição",
"Nº de Páginas": "173",
"Tipo": "Livro Digital",
"Formato": ".pdf",
"Licença": "Domínio Público",

"Descrição" :
"Há muito tempo duas famílias banham em sangue as ruas de Verona. Enquanto isso, na penumbra das madrugadas, ardem as brasas de um amor secreto. Romeu, filho dos Montéquio, e Julieta, desafiam a rixa familiar e sonham com um impossível futuro, longe da violência e da loucura.",


},

8:{
        "id" : 8,
        "capa" : "https://mojo.org.br/wp-content/uploads/2021/02/0006-ilha-do-tesouro-ebook.jpg",
        "Título": "A Ilha do Tesouro",
"Autor": "Robert Louis Stevenson",
"Instituição": "Mojo (.org)",
"Ano": "2020 – 1ª Edição",
"Nº de Páginas": "627",
"ISBN": "978-65-990752-6-1",
"Tipo": "Livro Digital",
"Formato": ".pdf",
"Licença": "Gratuito",

"Descrição":
"Uma história de piratas, com um mapa, um tesouro, um motim e um cozinheiro de bordo com uma perna só, A ilha do tesouro permanece uma das histórias de aventuras mais amadas da literatura."
},

9:{
        "id" : 9,
        "capa" : "https://a-static.mlcdn.com.br/618x463/livro-a-revolucao-dos-bichos/magazineluiza/228071400/4a0e23a20fcb0c8b5309fbba4d04c330.jpg",
        "Título": "A Revolução dos Bichos",
        "Autor": "George Orwell",
        "Instituição": "UENP",
        "Ano": "2015 – 1ª Edição",
        "Nº de Páginas": "087",
       "Tipo": "Livro Digital",
       "Formato": ".pdf",
        "Licença": "Domínio Público",

       "Descrição" :
       "Revolução dos Bichos é uma distopia, um livro alegórico de George Orwell, publicado em 17 de agosto de 1945, há setenta anos, na Inglaterra. De acordo com Orwell, o livro reflete os acontecimentos que se seguiram à Revolução Comunista de 1917"

},

10:{
        "id" : 10,
        "capa" : "https://m.media-amazon.com/images/I/51pD1JSlpQL.jpg",
        "Título": "Dom Casmurro",
"Autor": "Machado de Assis",
"Editora": "Edições Câmara",
"Ano": "2019 – 2ª Edição",
"Nº de Páginas": "128",
"Tipo":"Livro Digital",
"Formato": ".pdf",
"Licença":" Gratuito",

"Descrição":
"Dom Casmurro, um dos romances mais conhecidos do autor, foi publicado pela primeira vez em 1900. Bentinho, Capitu e Escobar são os protagonistas do enigmático triângulo amoroso criado por Machado de Assis e já fazem parte de nosso imaginário."

}

}



def response_History():
    return {"Destaque" : list(livros_data.values())}


@app.route("/Destaque")
def list_history():
      return response_History()


@app.route("/" )
def Home():
     return "<h1>estou funcionando</h1"

      
@app.route('/Destaque', methods =['POST']) 
def create_Destque():
    body = request.json 
   

    addNovoId = list(livros_data.keys())

    if addNovoId :
       
       NovoId = addNovoId[-1] +1

    else :
       NovoId = 1 

    livros_data[NovoId] = {
          
          "id" : NovoId,
          "titulo" : body ['titulo'],
           
        
          
    }   
    return response_History() 

@app.route('/Destaque/<int:Destaque_id>', methods=['DELETE'])
def delete_destaque(Destaque_id : int):
        Destaque = livros_data.get(Destaque_id)

        if Destaque:
            
            del livros_data [Destaque_id]

        return response_History()  

@app.route('/Destaque/<int:Destaque_id>', methods =['PUT'])

def update_destaque(Destaque_id : int):
    body =  request.json
    capa = body.get('capa')
   

    if Destaque_id in livros_data:
        livros_data[Destaque_id]['capa'] = capa 
        
          
        return response_History()  
     


Romance_livros = {

    1:{
         "id" : 1,
         "Título": "A Garota do Penhasco",
         "capa": "https://images-na.ssl-images-amazon.com/images/I/7178TJKzm2L.jpg",
"Autor": "Lucinda Riley",
"Editora": "Arqueiro",
"Ano": "2019 – 1ª Edição",
"Nº de Páginas": "020",
"ISBN": "9788580419955",
"Tipo": "Livro Digital",
"Formato": ".pdf",
"Licença": "Amostra Grátis",

"Descrição":
"Tentando superar um coração partido, Grania Ryan deixa Nova York e volta para a casa dos pais, na costa da Irlanda. Lá, na beira de um penhasco, em meio a uma tempestade, ela conhece Aurora Lisle, uma garotinha de 8 anos que mudará sua vida para sempre."


     },
    2:{
         "id" : 2,
         "capa": "https://images-na.ssl-images-amazon.com/images/I/717Mp0Qq8uL.jpg",
         'Título': 'A Cruz de Fogo',
'Autor': 'Diana G.',
'Editora': 'Arqueiro',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas': '047',
'ISBN': '9788580418248',
'Tipo': 'Livro Digital',
'Formato': '.pdf ',
'Licença': 'Amostra Grátis',

'Descrição' :
'A guerra se aproxima, garantiu-lhe sua esposa, Claire Randall. E, mesmo não querendo acreditar nesse triste futuro, Jamie Fraser está ciente de que não pode ignorar o conhecimento que só uma viajante do tempo poderia ter.'

     },
    3:{
         "id" : 3,
         'Título': 'Como Eu Era',
         'capa': 'https://images-na.ssl-images-amazon.com/images/I/61io1vJIWFL.jpg ',
'Autor': 'Jojo Moyes',
'Editora': 'Intrínseca' ,
'Ano': '2016 – 1ª Edição',
'Nº de Páginas': '022',
'ISBN': '978-85-8057-326-8',
'Tipo': 'Livro Digital',
'Formato': '.pdf ',
'Licença': 'Amostra Grátis',

'Descrição' :
'Em Como eu era antes de você, Lou Clark é uma jovem cheia de vida e espontaneidade, que sabe uma porção de coisas. Ela sabe quantos passos separam sua casa do ponto de ônibus.'

     },
    4:{
         "id" : 4,
         'Título': 'No Campo de Golfe',
         'capa': 'https://http2.mlstatic.com/D_NQ_NP_788173-MLB44154209640_112020-O.jpg',
'Autor': 'Agatha C. ',
'Instituição': 'L.B.',
'Ano': '1923 – 1ª Edição',
'Nº de Páginas': '252',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' :
'Em seu terceiro livro, Agatha Christie, a escritora dos romances policiais, aborda também o tema do amor. Claro que o assassinato envolto em muito mistério e suspense ainda é o prato principal da Rainha do Crime, mas seu Assassinato no campo de golfe.',

     },
    5:{ 
         "id" : 5,
         'Título': 'Para Todos os Garotos',
'Autor': 'Jenny Han',
'capa': 'https://lojasaraiva.vteximg.com.br/arquivos/ids/13662576/Imagem1.jpg?v=637175632170330000',
'Editora': 'Intrínseca',
'Ano': '2019 – 1ª Edição',
'Nº de Páginas': '018',
'ISBN': '978-85-8057-726-6',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Amostra Grátis',

'Descrição' :
'Lara Jean guarda suas cartas de amor em uma caixa azul-petróleo que ganhou da mãe. Não são cartas que ela recebeu de alguém, mas que ela mesma escreveu. Uma para cada garoto que amou – cinco ao todo.'



    },

     6:{ 
         "id" : 6,
         'Título': 'Eternamente Você',
'Autor': 'Sophie Jackson',
'Editora': 'Arqueiro',
'capa': 'https://www.baixelivros.com.br/media/2019/03/eternamente-voce.jpg ',
'Ano': '2015 – 1ª Edição',
'Nº de Páginas': '080',
'ISBN': '9788580414820',
'Tipo': 'Livro Digital',
'Formato': '.pdf ',
'Licença': 'Gratuito',


'Descrição' :

'Eternamente você é um conto gratuito que se passa entre os livros 1 e 2 da trilogia que se iniciou com Desejo proibido, Quando conheceu o arrogante presidiário Wesley Carter em Desejo proibido, a professora Kat Lane sentiu um misto de atração e ódio. Mas, à medida que o relacionamento entre eles se intensificou, ela descobriu um novo lado de seu aluno e se apaixonou por ele. '

    },

     7:{ 
         "id" : 7,
         'Título': 'A Carta Secreta',
         'capa': 'https://images-na.ssl-images-amazon.com/images/I/61Cn99OWkfL.jpg',
'Autor': 'Lucinda Riley',
'Editora': 'Arqueiro',
'Ano': '2019 – 1ª Edição',
'Nº de Páginas': '022',
'ISBN': '9788580419405' ,
'Tipo': 'Livro Digital',
'Formato':' .pdf',
'Licença':' Amostra Grátis',

'Descrição' :
'Quando sir James Harrison, um dos maiores atores de sua geração, morre aos 95 anos, deixa para trás não apenas uma família arrasada, mas também um segredo que seria capaz de abalar o governo britânico.',

     },

     8:{ 
         "id" : 8,
         'Título':' O Desejo',
         'capa': 'https://images-na.ssl-images-amazon.com/images/I/51eoI44yl0L._SX331_BO1,204,203,200_.jpg',
'Autor ': 'Nicholas Sparks',
'Editora':'' 'Arqueiro',
'Ano': '2021 – 1ª Edição',
'Nº de Páginas': '036',
'ISBN': '978-655-565-222-2',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Amostra Grátis',

'Descrição' :
'Em 1996, aos 16 anos, Maggie Dawes vai morar com uma tia que mal conhece em um vilarejo remoto na Carolina do Norte. Solitária e infeliz, ela só recupera o apetite pela vida quando conhece Bryce Trickett, um dos poucos adolescentes do lugar.'

     },
     
       9:{ 
         "id" : 9,
         'Título': 'Destino Terras Altas',
         'capa': 'https://images-na.ssl-images-amazon.com/images/I/71IrVV+AqNL.jpg',
'Autor ': 'Hannah Howell',
'Editora': 'Arqueiro',
'Ano': '2019 – 1ª Edição',
'Nº de Páginas': '023',
'ISBN': '9788580419368' ,
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Amostra Grátis',

'Descrição' :
'Em O destino das Terras Altas, primeiro livro da série Os Murrays, Hannah Howell nos apresenta o esplendor da Escócia medieval com uma saga de guerra entre clãs, lealdades divididas e amor proibido.'

     }, 
     
      10:{ 
         "id" : 10,
         'Título': 'Um Amor para Recordar',
'Autor': 'Nicholas Sparks',
'Editora': 'Intrínseca',
'Ano': '2019 – 1ª Edição',
'Nº de Páginas': ' 018',
'ISBN': '9788580419818 ',
'Tipo': 'Livro Digital',
'Formato':'  .pdf',
'Licença':' Amostra Grátis',

'Descrição':
'Aos 17 anos, a vida de Landon Carter muda para sempre. Largado pela namorada e sem companhia para o baile da escola, ele está desesperado para dar a volta por cima. As garotas que lhe interessam já têm par, sua única opção é alguém impensável: Jamie Sullivan, a filha do pastor.'



     },


 }      

def response_Romance():
    return {"Romance":list(Romance_livros.values())}

@app.route("/Romance")    
def list_Romance():
    return response_Romance()

Religiao_livros={
       
       1:{
           "id":1,
           'Título': 'Um Mestre da Espiritualidade',
           'capa': 'https://www.baixelivros.com.br/media/2022/01/um-mestre-da-espiritualidade.jpg',
'Autor': 'Joseph Aubry',
'Instituição':'Editora Dom Bosco',
'Ano': '2021 – 1ª Edição',
'Nº de Páginas': '060',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'A ação espiritual de São Francisco de Sales não quer atingir somente uma elite de cristãos e cristãs. Quer chegar a todos. Embora saiba que não pode esperar os mesmos frutos de todos, ele aceita que alguns de seus fiéis tenham necessidades especiais e a estes dirige de modo mais.'

       },

       2:{
           "id":2,
           'Título': 'Meditações para Quaresma',
           'capa': 'https://www.baixelivros.com.br/media/2021/02/meditacoes-quaresma.jpg',
'Autor': 'Santo Tomás de Aquino',
'Instituição': 'Permanência',
'Ano':' 2015 – 1ª Edição',
'Nº de Páginas': '091',
'Tipo': 'Livro Digital',
'Formato':  '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'O verdadeiro guia para o exercício quaresmal, este compilado de pérolas de Santo Tomás disponibilizado pelo Instituto Permanência é certamente capaz de enriquecer a experiência espiritual tanto dos principiantes quanto dos mais avançados na vida de oração.'

       },

       3:{
           "id":3,
           'Título': 'Novena de Natal',
           'capa' : 'https://www.baixelivros.com.br/media/2020/11/novena-de-natal.jpg',
'Autor': 'Dom Gil Antônio Moreira',
'Instituição': 'Arquidiocese Juiz de Fora',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas': '078',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Tenho máxima satisfação de apresentar o texto para os nossos encontros natalinos da Novena 2020, em nossa Província Eclesiástica, constituída das dioceses, de São João del Rei e Leopoldina, levando aos lares as bênçãos do Senhor que vem até nós.'

       },

       4:{
           "id":4,
           'Título': 'Bíblia Católica',
'Autor': 'Vários Autores',
'capa': 'https://www.baixelivros.com.br/media/2020/02/biblia-catolica.jpg',
'Instituição': 'Salve Rainha',
'Ano': '2019 – 1ª Edição',
'Nº de Páginas': '1166',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'A Bíblia Sagrada permanece como o livro de maior sucesso em todo o mundo com mais de 6 bilhões de cópias, mais de sete vezes o segundo colocado. Nós, da Salve Rainha, gradecemos o seu interesse pelos nossos e-books e nos colocamos a sua inteira disposição. '

       },

       5:{
           "id":5,
           'Título': 'Semana Santa',
'Autor':   ' Vários Autores',
'capa': 'https://www.baixelivros.com.br/media/2020/04/semana-santa.jpg',
'Instituição': 'Igreja Católica',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas': '010',
'Tipo': 'Livro Digital',
'Formato':'.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Neste pequeno livro você verá como viver bem sua Semana Santa em casa com sua família. Conselhos para todos os dias da semana: Domingo de Ramos, Segunda-feira, Terça-feira, Quarta-feira e Quinta-feira Santa, Sexta-feira da Paixão, Sábado de Aleluia e Domingo de Páscoa.'



       },
         6:{
           'Título': 'Sínodo do Apocalipse',
'Autor': 'Lucas Henrique',
'capa' : 'https://www.baixelivros.com.br/media/2019/09/sinodo.jpg',
'Instituição': 'CDB',
'Ano': '2019 – 1ª Edição',
'Nº de Páginas':' 064',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',


'Descrição':

'Desde a revolução protestante, que recentemente completou quinhentos anos, nunca o sacerdócio católico esteve sob tanto ataque inimigo quanto no presente momento com o Sínodo da Amazônia.'
       },

       7:{
           "id":7,

           'Título':'A Boa Vontade',
'Autor':' Pe. José Schrijvers',
'Editora': 'Formação da Donzela',
'Ano': '2019',
'Nº de Páginas': '049',
'Tipo': 'Livro Digital',
'Formato':'.pdf',
'Licença': 'Gratuito',

'Descrição':

'Para se santificar, a alma só tem necessidade de boa vontade. Guardá-la intacta e desenvolvê-la sem cessar, tal deve ser o fim constante e único de sua vida. “ A boa vontade, dizia santo Alberto Magno, supre tudo, está acima de tudo’’.'

       },

       8:{
           "id":8,
           'Título': 'Orações Católicas',
'Autor': 'Opus Dei',
'Autor': 'https://s3-eu-west-1.amazonaws.com/images-opus-dei/image/oracoes_capa.jpg',
'Editora': 'Independente',
'Ano': '2019',
'Nº de Páginas': '108',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' : 

'Orações Comuns Sinal da Cruz7 Glória , 7 Pai Nosso, 7 Ave Maria , 7 Salve rainha, 8 Ato de contrição, 8 Credo, 9 Credo Apostólico, 10 Ao Anjo da Guarda, 11, Orações à Santíssima TrindadeSímbolo Atanasiano, 12 Te Deum, 15 Te Deum (Latim), 16 Ato de fé, 18 Ato de esperança, 18 Ato de caridade, 18.'

       },

       9:{
           "id":9,
           'Título': 'A Humildade Cristã',
'Autor': 'Viktor Cathrein S.J.',
'capa':'https://www.baixelivros.com.br/media/2019/10/humildade-crista.jpg',
'Instituição': 'Alexandria Católica',
'Ano': '1925 – 1ª Edição',
'Nº de Páginas': '225',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Embora sobre a humildade já se tenham escrito muitas e belas coisas, e eu não possa apresentar nada de novo acerca de tão preclara virtude, julgo, não obstante que o presente livrinho será de alguma utilidade, não aos sábios, mas aos cristãos suficientemente instruídos.'


            
       },

       10:{
           "id":10,
           'capa':'',
           'Título': 'Contemplar o Natal',
'Autor':' Pe. Francisco Faus',
'Instituição': 'Padre Faus',
'Ano': '2017 – 1ª Edição',
'Nº de Páginas': '036',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',


'Descrição' :

'O primeiro anúncio do Natal foi uma luz resplandecente no meio da escuridão do mundo. Naquela noite santa, havia nos arredores de Belém uns pastores, que vigiavam e guardavam seus rebanhos durante as vigílias da noite.'

       },

}    

def response_Religiao():
    return{"Religiao": list(Religiao_livros.values())}

@app.route("/Religiao")
def list_Religiao():
    return response_Religiao()    

Aventura_livros = {
     
     1:{
         
         "id" : 1,
         'Título': 'A Volta ao Mundo',
         'capa' : 'https://www.lpm.com.br/livros/imagens/volta_ao_mundo_em_80_dias_9788525424525_hd.jpg',
'Autor': 'Júlio Verne',
'Instituição': 'EBC',
'Ano': '1873 – 1ª Edição',
'Nº de Páginas': '234',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' :
'Clássico da literatura juvenil, esta reedição comemora os 100 anos do autor Júlio Verne e conta a história de um inglês, Phileas Fogg, que tinha uma vida regrada e solitária, mas com muito dinheiro e, devido a uma aposta com seus amigos de jogo, resolve dar a volta ao mundo em oitenta dias.'

     },
     2:{
                 
        "id" : 2,

        'Título': 'Viagem Centro Terra',
        'capa' : 'https://images-na.ssl-images-amazon.com/images/I/A1s+6nCSdmL.jpg',
'Autor': 'Júlio Verne',
'Instituição': 'EBC',
'Ano': '1864 – 1ª Edição',
'Nº de Páginas': '169',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' :
'Um pergaminho escrito a mão com letras rúnicas escorrega de um livro de 700 anos. Traz a mensagem que motiva o professor Lidenbrock e seu sobrinho Axel a partirem de Hamburgo, na Alemanha, para a mais estranha e arriscada expedição científica do século XIX!'





     },
     3:{
        
          "id" : 3,
          'capa' : 'https://images-na.ssl-images-amazon.com/images/I/81Ew4DyQP2L.jpg',
          'Título': 'Da Terra à Lua',
'Autor': 'Júlio Verne',
'Instituição': 'EBC',
'Ano': '1877 – 1ª Edição',
'Nº de Páginas':' 265',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' : 
'O Clube do Canhão quer construir a maior arma de guerra já vista. O objetivo: mandar um projétil à Lua! Nessa homenagem em formato de história em quadrinhos, o escritor e quadrinista Estevão Ribeiro reúnem em uma única narrativa os clássicos de Júlio Verne (Da Terra à Lua).'



     },
     4:{
        
         "id" : 4,
         'capa' : 'https://www.baixelivros.com.br/media/2019/03/vinte-mil-leguas-submarinas.jpg',
         'Título': 'Léguas Submarinas',
'Autor': 'Júlio Verne',
'Instituição': 'V.B',
'Ano': '2000 – 1ª Edição',
'Nº de Páginas': '219',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' :
'Um misterioso monstro vem assombrando os oceanos. Destruindo navios e matando seua tripulantes. Publicado originalmente em 1870, 20.000 léguas submarinas é um exemplo clássico da visão e da imaginação de Júlio Verne. O pioneirismo de sua escrita fez com que fosse reconhecido como o pai da ficção científica.'

     },
     5:{
         "id" : 5,
         'capa' : 'https://www.baixelivros.com.br/media/2019/03/deligencia-alem.jpg',
         'Título':' A Diligência do Além',
'Autor': 'Davis',
'Instituição': 'D.B.',
'Ano': '1943 – 1ª Edição',
'Nº de Páginas': '129',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',


'Descrição' :
'Contratado para proteger a herdeira da companhia de diligências, o pistoleiro profissional Clint Jordan precisava encontrar provas contra o autor dos ataques freqüentes que a companhia de Leslie sofria. Com a ajuda de um amigo.'
     },

     6:{
         "id" : 6,
         'capa' : 'https://www.baixelivros.com.br/media/2019/03/mulheres-atiram.jpg',
         'Título': 'Quando as Mulheres Atiram',
'Autor': 'Estefania',
'Instituição': 'Rio Bravo',
'Ano': '1955 – 1ª Edição',
'Nº de Páginas': '123',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' :
'O amor de Nanny por rob era inabalavel, mas silencioso, o seu mundo acabou, quando descubriu que Rob, mandara vir do leste a sua futura esposa, Naany não conseguia entender como poderia Rob querer casar justo com a amada de seu irmão Joe.'

     },

     7:{
         "id" : 7,
         'capa' : 'https://www.baixelivros.com.br/media/2019/03/gosto-de-povora.jpg',
          'Título': 'Gosto de Pólvora',
'Autor': 'Herman',
'Instituição': 'BB',
'Ano': '1965 – 1ª Edição',
'Nº de Páginas': '190',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' :
'Ben era um garoto de 16 anos que estava apaixonado por uma garota da vizinhança. Ao se deparar com a cena em que ela estava sendo atacada por malfeitores a salva. Após o ataque ela morre a caminho do médico. Após isso ele e a família são atacados a noite por mais malfeitores e ele os enfrenta e mata todos.'

     },

     8:{
         "id" : 8,
         'capa' : 'https://www.baixelivros.com.br/media/2019/03/paco-morte.jpg',
'Título':' No Paço da Morte',
'Autor': 'Alf Regaldie',
'Instituição': 'db',
'Ano': '1974 – 1ª Edição',
'Nº de Páginas': '149',
'Tipo': 'Livro Digital',
'Formato': 'pdf',
'Licença': 'Domínio Público',

'Descrição' :
'Levando uma vida simples em Monterrey cuidando de sua granja, Irish não imaginava a mudança que teria em sua vida. Um faroeste onde os bandidos são implacáveis e cada dia nasce com um novo desafio para Irish e Clark. Será que conseguirão chegar com vida até o seu destino?.'



     },

     9:{
         "id" : 9,
         'capa' : 'https://www.baixelivros.com.br/media/2019/03/templo-misterioso.jpg',
         'Título': 'O Templo Misterioso',
'Autor': 'Glenn',
'Instituição': 'db',
'Ano': '1945 – 1ª Edção',
'Nº de Páginas': '051',
'Tipo': 'Livro Digital',
'Formato': 'pdf',
'Licença': 'Domínio Público',

'Descrição' :
'O Tenente Sagnier estava lutando na guerra. Treinar os legionários, ensiná-los a atirar e a sobreviver na selva era um trabalho árduo. Os vietnamitas também não eram adversários fáceis… Mas, e uma bela mulher… seria um adversário fácil de vencer?'

     },

      10:{
         "id" : 10,
         'capa' : 'https://www.baixelivros.com.br/media/2019/03/morte-companheira.jpg',
         'Título': 'A morte é Sua Companheira',
'Autor':' Adam',
'Instituição': 'DB',
'Ano': '1975 – 1ª Edição',
'Nº de Páginas':' 114',
'Tipo': 'Livro Digital',
'Formato': 'pdf',
'Licença': 'Domínio Público',

'Descrição' :
'Clint Garret, o Pistoleiro dos Olhos Azuis, pacificador de cidades; exterminados de bandidos. Justiceiro! A maldição de uma mulher morta sob o fogo do seu revólver o transforma num cavalheiro solitário em busca da paz. Mas o destino quer que ele seja sempre um matador!'



     }

}        

def response_Aventura():
    return {"Aventura": list(Aventura_livros.values())}

@app.route("/Aventura")
def list_Aventura():
    return response_Aventura()    


Infantis_livros = {

         1:{
             'id' : 1,
             'capa':'https://www.baixelivros.com.br/media/2022/03/pele-sol.jpg',
'Título': 'A Pele e o Sol',
'Autor': 'Maurício de Souza',
'Instituição': 'Sociedade Brasileira Dermatologia',
'Ano': '2012 – 1ª Edição',
'Nº de Páginas': '019',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Mônica e Magali tomam banho de piscina. Cebolinha vê a cena e comenta que a piscina é tão grande que cabe até uma baleia. Até aí, mais uma pirraça de Cebolinha, que não aguenta ver a Mônica sem soltar uma piadinha. Mas essa história que começa com brincadeira fala de cuidados ao sol.'

         },         
         2:{
             'id' : 2,
             'capa':'https://images-na.ssl-images-amazon.com/images/I/911o1h5gIzL.jpg',
             'Título': 'O Menino Maluquinho',
'Autor': 'Ziraldo',
'Instituição': 'ziraldo.com',
'Ano': '2018 – 1ª Edição',
'Nº de Páginas': '019',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Nessa versão disponibilizada, gratuitamente, pelo grande Ziraldo, verso e desenho contam a história de um menino traquinas que aprontava muita confusão. Alegria da casa, liderava a garotada, era sabido e um amigão. Fazia versinhos, canções, inventava brincadeiras.'

         },        
         3:{
             'id' : 3,
             'capa':'https://a-static.mlcdn.com.br/618x463/livro-o-pequeno-principe/magazineluiza/228782900/159d6918b41a93af36fe6727aab9b701.jpg',
             'Título': 'O Pequeno Príncipe',
'Autor': 'Antoine de Saint',
'Instituição': 'Virtual Books',
'Ano': '1943 – 1ª Edição',
'Nº de Páginas': '070',
'Tipo': 'Livro Digital',
'Formato': 'pdf',
'Licença': 'Domínio Público',


'Descrição' :
'Publicado pela primeira vez em 1942 nos Estados Unidos e, três anos mais tarde, na França, O pequeno príncipe tornou-se obra de apelo universal, um clássico moderno traduzido para mais de oitenta idiomas.'

         },         
         4:{
             'id' : 4,
             'capa':'https://www.baixelivros.com.br/media/2022/04/o-supermotociclista.jpg',
             'Título': 'O Supermotociclista',
'Autor': 'Maurício de Souza',
'Instituição': 'Honda',
'Ano': '2010 – 1ª Edição',
'Nº de Páginas': '036',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição':
'Transmite, de forma bem humorada, os conceitos de pilotagem defensiva e respeito aos protagonistas do trânsito. Entre os temas abordados estão a importância do uso de equipamentos de segurança e da obediência às leis de trânsito, além da postura ideal a ser adotada pelo motociclista.'
         },         
         5:{
             'id' : 5,                                     
             'capa':'https://images-na.ssl-images-amazon.com/images/I/51HQzMZNXVL._SY445_SX342_QL70_ML2_.jpg',
             'Título': 'O Relógio',
'Autor': 'Flávio Colombini',
'Instituição': '@flaviocolombini',
'Ano': '2018 – 1ª Edição',
'Nº de Páginas': '027',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'O Relógio Que Perdeu a Hora é um livro muito divertido! Tem uma linda história escrita em poesia narrativa, cheia de rimas, que as crianças vão adorar! Quando o relógio despertou, ele reparou que tinha perdido a hora. Então, ele saiu procurando a hora pelo mundo afora.'


         },    

             6:{
             'id' : 6,                                     
             'capa':'https://www.baixelivros.com.br/media/2022/01/bia-perguntadeira.jpg',
             'Título': 'Bia, a Menina Perguntadeira',
'Autor': 'Bianca Maria',
'Instituição': 'ITEVA (.org.br)',
'Ano': '2021 – 1ª Edição',
'Nº de Páginas': '024',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Uma história que tem como objetivo central estimular nas crianças a curiosidade para aprender, associada ao respeito, empatia e tolerância à frustração. Escrito e ilustrado para crianças, este livro é um dos materiais desenvolvidos no Projeto CDF – Cidadão Do Futuro.'


         },

            7:{
             'id' : 7,                                     
             'capa':'https://www.baixelivros.com.br/media/2021/04/historias-infantis.jpg',
             'Título': '100 Histórias Infantis',
'Autor': 'Vários Autores',
'Instituição': 'Colégio Lívia Alencar',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas': '303',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'O objetivo desta coletânea é facilitar para que em um mesmo local nossos alunos possam encontrar um repertório de histórias de qualidade. As histórias a seguir foram escolhidas pois apresentam uma releitura especial, ou seja, são histórias contadas na versão de seus contadores.'


         }, 

            8:{
             'id' : 8,                                     
             'capa':'https://www.baixelivros.com.br/media/2019/05/voa-joao.jpg',
              'Título': 'Voa, João',
'Autor': 'Cleide Ramos',
'Instituição': 'MultiRio',
'Ano': '2015 – 1ª Edição',
'Nº de Páginas': '030',
'ISBN': '978-85-60354-10-8',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',


'Descrição' :
'Conheça João, a pequena ave que tem medo de ir à escola. Vamos acompanhar esta historinha animada que busca fomentar a imaginação e a produtividade das crianças.'

         },    

            9:{
             'id' : 9,                                     
             'capa':'https://www.baixelivros.com.br/media/2022/04/elefante-em-apuros.jpg',
             'Título': 'O Elefante em Apuros',
'Autor': 'Flávio Colombini',
'Ilustração': 'Edde Wagner',
'Instituição': 'flaviocolombini (.com)',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas': '029',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Quando o elefante pisa na areia movediça, fica com os pés presos e começa a afundar. Então vários animais tentam ajudá-lo a sair dessa enrascada.'


         }, 

            10:{
             'id' : 10,                                     
             'capa':'https://www.baixelivros.com.br/media/2020/05/os-porquinhos.jpg',
             'Título': 'Os Três Porquinhos',
'Autor': 'Alfredo Oliveira',
'Instituição': 'LpC',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas': '016',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Os três porquinhos resolveram sair de casa e construir cada um a sua moradia. Mas aí veio o Lobo Mau e com seu forte assopro destruiu tudo! Descubra o que vai acontecer com os irmãos e o Lobo… Viaje para um mundo dos contos com este clássico, recontado pelo Alfredo Oliveira.'


         },         

   }





def response_Infantis():
    return {'Infantis' : list(Infantis_livros.values())}

@app.route('/Infantis')

def list_Infantis():
    return response_Infantis()


Cursos_livros = {
      
      1:{
          'id' : 1,
          'capa' : 'https://www.baixelivros.com.br/media/2019/07/curso-java-basico.jpg',
          'Título': 'Java Básico',
'Autor': 'Fábio Mengue',
'Instituição': 'UNICAMP',
'Ano': '2018 – 1ª Edição',
'Nº de Páginas': '035',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',


'Descrição' :

'Em 1991, um grupo de engenheiros da Sun Microsystems foi encarregado de criar uma nova linguagem que pudesse ser utilizada em pequenos equipamentos como controles de TV, telefones, fornos, geladeiras, etc.'
      },
      2:{
           'id' : 2,
          'capa' : 'https://www.baixelivros.com.br/media/2022/04/introducao-a-criptografia.jpg',
          'Título': 'Introdução à Criptografia',
'Autor': 'Luiz Manoel Figueiredo',
'Instituição': 'CEP/EB',
'Ano': '2010 – 1ª Edição',
'Nº de Páginas': '172',
'ISBN': '85-7648-331-9',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição':
'Aritmética dos inteiros: números primos, algoritmo da divisão, mdc e mmc, algoritmo de Euclides. Aritmética modular: congruência módulo, soma e produto de classes, inversa de uma classe módulo n.'
      },
      3:{
           'id' : 3,
          'capa' : 'https://www.baixelivros.com.br/media/2022/04/microeconomia.jpg',
          'Título': 'Microeconomia',
'Autor': ' Paulo Mattos',
'Instituição': 'ENAP',
'Ano': '2015 – 1ª Edição',
'Nº de Páginas': '067',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'A Microeconomia, em sua formulação padrão, com base nos desenvolvimentos do utilitarismo da economia neoclássica, constitui um corpo teórico o qual parte do entendimento do comportamento econômico individualizado dos agentes, tomados como racionais.'
      },
      4:{
           'id' : 4,
          'capa' : 'https://www.baixelivros.com.br/media/2022/02/ingles-aplicado-eventos.jpg',
          'Título': 'Inglês aplicado',
'Autor': 'Eva Maurice Dionísio',
'Instituição': 'IFS',
'Ano': '2013 – 1ª Edição',
'Nº de Páginas': '140',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Este curso de Inglês para Eventos possui características específicas. A proposta apresentada é simples, pois não tem a pretensão de se tornar um curso completo de Inglês. Nesta obra, são abordados apenas temas considerados relevantes para você.'


      },
      5:{
           'id' : 5,
          'cursos' : 'https://cdn.slidesharecdn.com/ss_thumbnails/marketingvendasifpr-150930142217-lva1-app6891-thumbnail-4.jpg?cb=1443623202',
          'Título': 'Marketing e Vendas',
'Autor': 'Vários Autores',
'Instituição': 'e-Tec',
'Ano': '2012 – 1ª Edição',
'Nº de Páginas': '128',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'O presente livro tem como objetivo enriquecer o estudo acerca das atividades e práticas docentes relativas à disciplina de Marketing e Vendas, na modalidade de Educação a Distância. Cada aula foi estruturada pensando em retomar conceitos institucionais e práticos da cadeia de marketing dentro da vida pessoal e coorporativa.'
      },

       6:{
           'id' : 6,
          'cursos' : 'https://www.baixelivros.com.br/media/2022/01/ingles-iniciantes.jpg',
          'Título': 'Inglês para Iniciantes',
'Autor': 'Vários Autores',
'Instituição': 'CCA',
'Ano': '2019 – 1ª Edição',
'Nº de Páginas': '048',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Este curso tem o objetivo de ensinar as bases necessárias para que o(a) aluno(a) possa aprender uma nova língua, de forma simples e objetiva, motivando(a) a aprofundar seu interesse pelo inglês e se aperfeiçoar, para que possa utilizá-lo como meio de comunicação.'
      },
       7:{
           'id' : 7,
           'cursos' : 'https://www.baixelivros.com.br/media/2021/02/tecnico-em-agropecuaria.jpg',
           'Título': 'Técnico em Agropecuária',
'Autor': 'Leandro Yamashita',
'Instituição': 'e-Tec/MEC',
'Ano': '2012 – 1ª Edição',
'Nº de Páginas': 116,
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Caro aluno, esse material foi desenvolvido com o objetivo de trazer informações sobre a importância de se mecanizar a produção. No entanto, deixamos claro que nem sempre a utilização de máquinas será viável, já que o custo-benefício às vezes não trará vantagens para o produtor.'



      },
       8:{
           'id' : 8,
          'cursos' : 'https://livrariapublica.com.br/wp-content/uploads/curso-eletricista.jpg',
          'Título': 'Eletricista',
'Autor': 'Lucas Puntel',
'Editora': 'ViaRápida',
'Ano': '2012 – 1ª Edição',
'Nº de Páginas': '161',
'ISBN': '978-85-65278-36-2',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'O conhecimento sobre eletricidade foi construído ao longo dos anos. Partindo do levantamento de suas experiências, você aprenderá mais sobre os conhecimentos necessários para o exercício da atividade de eletricista. As ferramentas e os materiais básicos para o exercício do trabalho.'
      },
       9:{
           'id' : 9,
          'cursos' : 'https://www.baixelivros.com.br/media/2019/09/curso-desenhos.jpg',

          'Título':'Desenho Realista',
'Autor': 'Carlos Damasceno',
'Instituição': 'Sesc',
'Ano': '2011 – 1ª Edição',
'Nº de Páginas': '031',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Abordaremos algumas questões e preocupações comuns como: composição, luz e sombra e material utilizado em desenho. Entraremos em contato com diversos aspectos de preparação para o processo de aprender a desenhar. É recomendado que você siga todos os tópicos apresentados.'



      },
       10:{
           'id' : 10,
          'cursos' : 'https://www.baixelivros.com.br/media/2019/07/desenho-artistico.jpg',
          'Título': 'Desenho Artístico',
'Autor': 'Ivan Querino',
'Instituição': 'ADS',
'Ano': '2019 – 1ª Edição',
'Nº de Páginas': '130',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição':
'O objetivo deste ebook é apresentar a arte do desenho artístico, mostrando os princípios básicos do desenho para que você adquira um conhecimento global que o auxiliará na criação de um estilo próprio e na escolha da carreira, servindo de alicerce para outros cursos e o mercado de trabalho.'
      },

        11:{
           'id' : 11,
          'cursos' : 'https://www.baixelivros.com.br/media/2019/02/curso-cabeleireiro.jpg',

          'Título': 'Cabeleireiro',
'Autor': 'Vários Autores',
'Instituição': 'ViaRápida',
'Ano': '2012 – 1ª Edição',
'Nº de Páginas': '~300',
'ISBN': '978-85-61143-92-3',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Porque no mundo de hoje não é suficiente conhecer apenas as técnicas para fazer um bom penteado ou corte de cabelo. Também é preciso saber como você pode melhorar sua busca por um novo emprego. No nosso curso, vai conhecer as várias facetas da ocupação de cabeleireiro.'

    },

}




def response_cursos():
    return {'Cursos' : list(Cursos_livros.values())}

@app.route('/Cursos')
def list_cursos():
    return response_cursos()   

Historias_livros={
       
       1:{
           "id" :1,
           'capa' : 'https://www.baixelivros.com.br/media/2022/02/historias-antigas.jpg',
           'Título': 'Histórias Antigas',
'Autor': 'Vários Autores',
'Instituição': 'Fi Editora',
'Ano': '2021 – 1ª Edição',
'Nº de Páginas': '235',
'ISBN': '978-65-5917-278-8',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Esperamos que a leitura deste livro seja do proveito de todos e que algumas das pesquisas e experiências aqui narradas possam ser inspiradoras de futuros trabalhos em pesquisa, ensino e divulgação de História da Antiguidade. '

       },
       2:{
           "id" :2,
           'capa' : 'https://m.media-amazon.com/images/I/41AfAIRiT6L.jpg',
           'Título': 'A Abolição',
'Autor': 'Osório Duque Estrada',
'Instituição': 'Senado Federal',
'Ano': '2005 – 1ª Edição',
'Nº de Páginas':'235',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'A Abolição é obra de cunho didático que reúne documentos e descreve os passos da criação de uma consciência antiescravagista no Brasil. Osório parte dos antecedentes históricos do fenômeno, passa pelo período de 1830 a 1850 e envereda pelas repercussões da abolição do tráfico negreiro.'   
    },
       3:{
           "id" :3,
           'capa' : 'https://www.baixelivros.com.br/media/2020/08/escritos-sobre-escravidao.jpg',
           'Título': 'Textos sobre Escravidão',
'Autor': 'Vários Autores',
'Instituição': 'Editora Fi',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas': '203',
'ISBN': '978-65-87340-11-1',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Já não sinto minha ofensa nem a tua; sinto somente a que esta gente adventícia faz a nosso ser antigo e aos costumes que herdamos de nossos pais. Porventura foi outro o patrimônio que nos deixaram senão nossa liberdade.'  
     },
       4:{
           "id" :4,
           'capa' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpaiRYweuZdTJdOfO_Q1wdJF1sXgmrgFEavKu_4-2gsEetM7xL3jwZuvbXwRn5s1FdWIA&usqp=CAU',
           'Título': 'Ciência e Liberdade',
'Autor': 'Vários Autores',
'Instituição': 'UFRJ',
'Ano': '1998 – 1ª Edição',
'Nº de Páginas': '285',
'ISBN': '85.7108.212.X',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Que vale a ciência? Que contribuição nos dá para a compreensão do mundo em que vivemos? Além de gerar tecnologias, é a ciência parte da cultura? Qual foi a sua evolução ao longo da história? Você saberá as respostas neste livro.'  
     },

       5:{
           "id" :5,
           'capa' : 'https://m.media-amazon.com/images/I/51ujPiIEStL.jpg',
           'Título': 'Brasil, País do Futuro',
'Autor': 'Stefan Zweig',
'Instituição': 'eBooksBrasil',
'Ano': '1941 – 1ª Edição',
'Nº de Páginas': '407',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição':
'Stefan Zweig e sua segunda mulher, Lotte, escolheram o Brasil como refúgio às atrocidades que eram cometidas na Europa durante a Segunda Guerra Mundial. A obra foi publicada pela primeira vez em 1941 tornou-se rapidamente um clássico.'       },
       6:{
           "id" :6,
           'capa' : 'https://www.baixelivros.com.br/media/2020/06/falas-do-trono.jpg',
           'Título': 'Falas do Trono',
'Autor': 'Vários Autores',
'Instituição': 'Senado Federal',
'Ano': '2019 – 1ª Edição',
'Nº de Páginas': '720',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'O volume contém as Falas do Trono, discursos proferidos pelos monarcas brasileiros entre 1823 e 1889, que arrolam acontecimentos políticos e atos administrativos em cada uma das legislaturas dos 66 anos do Império brasileiro. Falas de Dom Pedro I, Dom Pedro II e da Princesa Isabel.'

 },

       7:{
           "id" :7,
           'capa' : 'https://d1pkzhm5uq4mnt.cloudfront.net/imagens/capas/_6c4e8746113b573fa46d30d8954f11998a87c172.jpg',
           'Título': 'Mulheres Intelectuais',
'Autor': 'Vários Autores',
'Instituição': 'Fi',
'Ano': '2019 – 1ª Edição',
'Nº de Páginas': '296',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'É corrente afirmar-se que, antes da chamada Modernidade, não há registro de mulheres na construção do pensamento erudito. Mas isso é uma inverdade, verificaremos a atuação das mulheres na medicina, na história, na poesia, na dramaturgia, na filosofia, na teologia e na mística.'
   },

       8:{
           "id" :8,
           'capa' : 'https://www.baixelivros.com.br/media/2019/11/proclamacao-da-republica.jpg',
           'Título': '180 Anos da Proclamação da Rep.',
'Autor': 'Vários Autores',
'Instituição': 'IHGRS',
'Ano': '2017 – 1ª Edição',
'Nº de Páginas': '257',
'ISBN': '978-85-62943-08-9',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',


'Descrição' :

'A ideia deste livro surgiu a partir do convite realizado pelo presidente do Instituto Histórico e Geográfico do Rio Grande do Sul, dr. Miguel Frederico do Espírito Santo.' 
   },

       9:{
           "id" :9,
           'capa' : 'http://www.ebooksbrasil.org/eLibris/imagens/peixoto1.jpg',
           'Título': 'História do Brasil',
'Autor': 'Afrânio Peixoto',
'Instituição': 'eBooksBrasil',
'Ano': '2008 – 2ª Edição',
'Nº de Páginas': '267',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'A história não é um arquivo, ou relicário de memórias evocadas: seria de pouco préstimo. Ao contrário. A história é uma criação contínua da vida. Além do documento, que aparece todos os dias, alterando o juízo, esse juízo, com o mesmo documento, muda com as gerações…'  
     },
       10:{
           "id" :10,
           'capa' : 'https://www.baixelivros.com.br/media/2019/06/civilizacao-brasileira.jpg',
           'Título': 'Civilização Brasileira',
'Autor': 'Pedro Calmon',
'Instituição': 'Senado Federal',
'Ano': '2002 – 2ª Edição',
'Nº de Páginas': '329',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :

'Este livro não é um compêndio, nem é um tratado. É uma nova síntese da história do Brasil: história social, econômica, administrativa e política. A História da Civilização Brasileira. Destina-se aos estudantes dos cursos superiores.'     
  },
}     

def response_Historia():
    return {'Historia': list(Historias_livros.values())}

@app.route('/Historia')
def list_historia():
    return response_Historia()  

Lieratura_livros={
            
            1:{
                'id' : 1,
                'capa' : 'https://www.baixelivros.com.br/media/2020/02/iracema.jpg',
                'Título': 'Iracema',
'Autor': 'José de Alencar',
'Instituição': 'Biblioteca Nacional',
'Ano': '2012 – 1ª Edição',
'Nº de Páginas': '084',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' :
'Esta obra, tida como uma das mais belas da literatura brasileira, conta a história de amor entre uma índia tabajara e um guerreiro português. O enredo é uma alegoria da colonização do país, e a protagonista simboliza a união entre o homem e a natureza.'          
  },
            2:{
                'id' : 2,
                'capa' : 'https://www.baixelivros.com.br/media/2020/01/machado-completo.jpg',
                'Título': 'Obras Completas',
'Autor': 'Machado de Assis',
'Instituição': 'Machado de Assis',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas': '2730',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Todos os contos e romances de Machado de Assis organizados em um só volume. O leitor encontrará as seguintes obras: “Ressurreição” (1872), “A Mão e a Luva” (1874), “Helena” (1876), “Iaiá Garcia” (1878), “Memórias Póstumas de Brás Cubas” (1881), “Casa Velha” (1885) e muito mais!'
            },
            3:{
                'id' : 3,
                'capa' : 'https://m.media-amazon.com/images/I/41jfBhIY6jL.jpg',
                'Título': 'Contos Fluminenses',
'Autor': 'Machado de Assis',
'Instituição': 'MEC',
'Ano': '1870 – 1ª Edição',
'Nº de Páginas': '164',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' :
'Contos fluminenses é composto de sete histórias e representa a estreia do escritor como contista. As narrativas revelam algumas das marcas registradas do autor, com personagens complexos e passagens recheadas de ironias e críticas à sociedade fluminense.'
            },
            4:{
                'id' : 4,
                'capa' : 'https://www.baixelivros.com.br/media/2021/01/casa-velha.jpg',
                'Título': 'Relíquias Casa Velha',
'Autor': 'Machado de Assis',
'Instituição': 'MEC',
'Ano': '1906 – 1ª Edição',
'Nº de Páginas': '055',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Relíquias da Casa Velha reúne alguns contos de Machado de Assis, todos eles relacionados a passagens que aconteceram em uma residência. “Uma casa tem muita vez as suas relíquias, lembranças de um dia ou de outro, da tristeza que passou, da felicidade que se perdeu”, escreve o autor.'
            },
            5:{
                'id' : 5,
                'capa' : 'https://www.baixelivros.com.br/media/2019/01/o-banquete.jpg',
                'Título': 'O Banquete',
'Autor': 'Platão',
'Editora': 'VirtualBooks',
'Ano': '2003 – 1ª Edição',
'Nº de Páginas':' 060',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição':
'O Banquete é um dos diálogos mais célebres de Platão (428-347 a.C.). Ambientado durante um jantar oferecido pelo poeta Agatão em Atenas, põe em cena Sócrates, Aristófanes e outros convivas enfrentando-se em uma competição: cada um deve fazer um discurso de elogio à figura de Eros, o deus do amor.'
            },      
            6:{
                'id' : 6,
                'capa' : 'https://m.media-amazon.com/images/I/51821aE9qHL.jpg',
                'Título': 'Fédon',
'Autor': 'Platão',
'Instituto': 'Portal Conservador',
'Ano': '387 a.C – 1ª Edição',
'Nº de Páginas': '059',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição':
'Sócrates é imortalizado pela lucidez e coragem com que enfrenta a morte. Condenado pela democracia ateniense, o filósofo compartilha sua meditação sobre o sentido da filosofia. Neste diálogo, a filosofia é considerada reconhecimento e exercício da verdadeira natureza da alma, que sobrevive à morte do corpo.'
            },
            7:{
                'id' : 7,
                'capa' : 'https://m.media-amazon.com/images/I/41m6ZMGMA2L.jpg',
               ' Título': 'A Escrava Isaura',
'Autor': 'Bernardo Guimarães',
'Instituição': 'Biblioteca Nacional',
'Ano': '1875 – 1ª Edição',
'Nº de Páginas':' 087',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Isaura, uma escrava branca dotada dos melhores sentimentos, pura de coração e com uma educação como não tiveram muitas ricas e ilustres damas. No entanto, sofre as terríveis perseguições de Leôncio, seu senhor e homem tocado pelos piores vícios.'
            },
            8:{
                'id' : 8,
                'capa' : 'https://www.baixelivros.com.br/media/2020/08/ensaios-gracilianicos.jpg',
               ' Título': 'Ensaios Graciliânicos',
'Autor': 'Vera Lúcia Lopes Dias',
'Instituição': 'Fi Editora',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas': '210',
'ISBN': '978-65-81512-30-9',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Nos sete ensaios a autora, analisando o alter ego de Graciliano, reflete sobre a fantástica terra dos meninos, por meio de Raimundo; aborda o uso da fantasia no combate ao preconceito e ao bullying, valorizando as diferenças.'
            },
            9:{
                'id' : 9,
                'capa' : 'https://www.baixelivros.com.br/media/2020/02/obras-castro-alves.jpg',
                'Título': 'Obras Completas',
'Autor': 'Castro Alves',
'Instituição':' BBM/USP',
'Ano': '1921 – 1ª Edição',
'Nº de Páginas':'470' ,
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' :
'A publicação das obras completas de Castro Alves, coordenada por Afrânio Peixoto, colocou à disposição do público, com anotações e correção de gralhas tipográficas das primeiras edições, o conjunto conhecido da produção do poeta'
            },
            10:{
                'id' : 10,
                'capa' : 'https://www.baixelivros.com.br/media/2020/04/maravilhoso-sitio.jpg',
              '  Título':' Monteiro Lobato',
'Autor': 'Pâmela Machado',
'Instituição':' SEBPM',
'Ano': '2015 – 1ª Edição',
'Nº de Páginas': '021',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Através de sua literatura infantil, Lobato permanece vivo no imaginário e nos corações de seus leitores de todas as épocas. Sua obra infantil, ainda que tenha sido escrita há quase cem anos, propicia discussões e reflexões fundamentais para a formação, informação e prazer das crianças e também dos adultos.'
            },


}      

def response_Literatura():
    return {'Literatura': list(Lieratura_livros.values())}

@app.route('/Literatura')
def list_Literatura():
    return response_Literatura()    

Medicina_livros={

       1:{
           'id' : 1,
           'capa' : 'https://www.baixelivros.com.br/media/2022/03/embriologia-humana.jpg',
'Título': 'Embriologia Humana',
'Autor': 'Vários Autores',
'Instituição': 'UFSC',
'Ano': '2011 – 1ª Edição',
'Nº de Páginas':' 199',
'ISBN': '978-85-61485-42-9',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'A Embriologia é a ciência que estuda o desenvolvimento de uma nova vida desde a fecundação até o nascimento. É importante lembrar, porém, que o desenvolvimento não cessa com o nascimento.'
       },
       2:{
           'id' : 2,
           'capa' : 'https://libros.buap.mx/1419-home_default/nociones-de-embriologia-basica.jpg',
          ' Título': 'Embriologia',
'Autor': 'Tatiana Montanari',
'Instituição': 'UFRGS',
'Ano': '2019 – 2ª Edição',
'Nº de Páginas':' 079',
'ISBN': '978-85-915646-1-3',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Embriologia significa a ciência que estuda os embriões, isto é, o estudo descritivo ou experimental das mudanças na forma do embrião. A Embriologia não se restringe ao período embrionário. A Embriologia aborda desde a produção dos gametas até o nascimento.'
       },
       3:{
           'id' : 3,
           'capa' : 'https://www.baixelivros.com.br/media/2021/08/cinesiologia.jpg',
           'Título': 'Cinesiologia',
'Autor': 'Joana Paula Portela',
'Instituição': 'INTA',
'Ano': '2016 – 1ª Edição',
'Nº de Páginas': '087',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'A Cinesiologia é uma ciência que tem como enfoque a análise do movimento humano, na Educação Física tem um olhar especial nas ações musculares sobre o aspecto anatômico funcional. Os conteúdos aqui abordados foram sistematizados de modo a poder processualmente.'
       },
       4:{
           'id' : 4,
           'capa' : 'https://www.baixelivros.com.br/media/2021/03/gestacao-alto-risco.jpg',
           'Título': 'Gestação de Alto Risco',
'Autor': 'Vários Autores',
'Instituição': 'Ministério da Saúde',
'Ano': '2010 – 5ª Edição',
'Nº de Páginas': '304',
'ISBN':' 978-85-334-1767-0',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'O material foi elaborado para orientar a equipe assistencial no diagnóstico e tratamento das doenças e/ou problemas que afligem a mulher durante a gravidez. Objetiva também uniformizar as condutas, contribuindo para uma atuação mais coesa da equipe.'
       },
       5:{
           'id' : 5,
           'capa' : 'https://static.docsity.com/documents_first_pages/notas/2009/09/27/29ebec76be5e31983873c957d4e88298.png',
          ' Título': 'Saúde da Mulher',
'Autor': 'Vários Autores',
'Instituição': 'Ministério da Saúde',
'Ano': '2011 – 1ª Edição',
'Nº de Páginas': '044',
'ISBN': '978-85-334-0781-7',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'O livro reflete o compromisso com a implementação de ações de saúde que contribuam para a garantia dos direitos humanos das mulheres e reduzam a morbimortalidade por causas preveníeis e evitáveis.'


       },
       6:{
           'id' : 6,
           'capa' : 'https://a-static.mlcdn.com.br/618x463/bulario-medico-veterinario-para-caes-e-gatos/zambonibooks/67301/93464e5e42eeaf77ba50d14e834e5b73.jpg',
           'Título': 'Bulário Veterinário',
'Autor': 'Emanuele Mosna',
'Coleção': 'Manuais Veterinários',
'Instituição': 'USP',
'Ano': '2007 – 1ª Edição',
'Nº de Páginas': '228',
'Tipo': 'Livro Digital',
'Formato':' .pdf',
'Licença': 'Gratuito',

'Descrição' :
'Ótimo material para os profissionais da área que buscam o conhecimento na aplicação de medicamentos para cães e gatos. Este manual utilizou como base as doses utilizadas no HOVET.'
       },
       7:{
           'id' : 7,
           'capa' : 'https://www.baixelivros.com.br/media/2020/03/saude-e-doencas.jpg',
          ' Título': 'Saúde e Doenças no Brasil',
'Autor': 'Vários Autores',
'Instituição':' Fi Editora',
'Ano': '2012 – 1ª Edição',
'Nº de Páginas':' 260',
'ISBN': '978-85-5696-415-1',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Esta obra teve seu nascedouro em Vitória (ES), no ano passado (2017), numa conversa informal entre as organizadoras, quando participávamos do 7º. Colóquio História das Doenças. '
       },
       8:{
           'id' : 8,
           'capa' : 'https://images-na.ssl-images-amazon.com/images/I/31kNKhJPUvL._BO1,204,203,200_.jpg',
           'Título': 'Uma Introdução à Medicina',
'Autor': 'Luiz Salvador',
'Instituição': 'CFM',
'Ano': '2013 – Vol. 1',
'Nº de Páginas': '434',
'ISBN': '978-85-87077-31-8',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :

'Este livro começou a ser concebido em 1993, quando os alunos do primeiro ano médico do Centro de Ciências Biológicas da Saúde (CCBS) da Universidade Federal de Mato Grosso do Sul reivindicaram a inclusão.'
       },
       9:{
           'id' : 9,
           'capa' : 'https://www.baixelivros.com.br/media/2020/02/conceitos-genetica.jpg',
          ' Título': 'Conceitos de Genética',
'Autor': 'Benedito Neto',
'Instituição': 'Atena',
'Ano': '2019 – 1ª Edição',
'ISBN': '978-85-7247-421-4',
'Nº de Páginas': '250',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'A genética como sabemos possui um campo vasto de aplicabilidades que podem colaborar e cooperar grandemente com os avanços científicos e tecnológicos. Esperamos que seja apenas o primeiro de muitos outros livros na área.'
       },
       10:{
           'id' : 10,
           'capa' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnLOxMIk7Tpb1EphIHXq3ea4A_-tVJNXOAug&usqp=CAU',
         '  Título': 'Artigos COVID-19',
'Autor': 'Nelson Teich',
'Instituição': 'Linkedin',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas':' 014',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Neste pequeno compilado transformado em livro digital, você terá acesso aos artigos publicados pelo Ministro da Saúde, Dr. Nelson Teich, sobre o COVID-19 (novo coronavírus). Os artigos se encontram em domínio público e foram extraídos da rede social Likedin.'
       },
}    

def response_Medicina():
    return {'Medicina': list(Medicina_livros.values())}

@app.route('/Medicina')
def list_Medicina():
    return response_Medicina()  

Cordel_livros={
      
      1:{
          'id': 1,
          'capa' : 'https://www.baixelivros.com.br/media/2022/01/coronavirus.jpg',
          'Título': 'O Coronavírus',
'Autor': 'Cícero Duarte',
'Ilustração': 'Júlio Souza',
'Instituição':' SESC/CE',
'Ano': '2020 – 1ª Edição',
'Nº de Páginas': '016',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'O projeto é realizado com edições poéticas cujo objetivo principal é publicar a produção de cordelistas para estimular e promover a literatura de cordel na região do Cariri e no Brasil.'
      },
      2:{
          'id': 2,
          'capa' : 'https://www.baixelivros.com.br/media/2022/01/sus-cidadao.jpg',
          'Título': 'O Dia que o SUS',
'Autor': 'Lincoln Macário',
'Instituição':' Ministério da Saúde',
'Ano': '2021 – 1ª Edição',
'Nº de Páginas':' 007',
'Tipo':' Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Esta é uma boa história, digna de um cordel.Trata de quando o SUS e um usuário fiel.Resolveram discutir: cada um o seu papel.No atendimento do SUS, vale a solidariedade.E quem estiver mais doente, tem a prioridade.'
      },
      3:{
          'id': 3,
          'capa' : 'https://www.baixelivros.com.br/media/2021/03/nossos-cordeis.jpg',
         ' Título': 'Nossos Cordéis',
'Autor': 'Teones Suzano',
'Instituição':' FIDA',
'Ano': '2017 – 1ª Edição',
'Nº de Páginas':' 016',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Esta publicação é parte de uma série de ações que visam oportunizar aos jovens, homens e mulheres, a continuidade da permanência na sua região, em diversas atividades, não só agrícolas. O jovem Teones Almeida, é filho de agricultor e agricultora da região atendida pelo projeto e, por meio dos seus cordéis, resgata e valoriza a região semiárida.'
      },
      4:{
          'id': 4,
          'capa' : 'https://www.baixelivros.com.br/media/2020/04/coxinha-de-macaxeira.jpg',
           'Título': 'Coxinha de Macaxeira',
'Autor': 'Pedro da Fonseca',
'Instituição':' IFRN',
'Ano': '2015 – 1ª Edição',
'Nº de Páginas': '018',
'ISBN': '978-85-8333-216-9',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'O Coxinha de Macaxeira, intencionalmente, não é um cordel convencional, pois foi concebido sem perder de vista o mundo dos jovens alunos do ensino médio. Essa foi uma das premissas do projeto: criar algo que fosse atraente para um leitor jovem, com linguagem visual leve'

      },
      5:{
          'id': 5,
          'capa' : 'https://www.baixelivros.com.br/media/2019/03/uma-forca.jpg',
          'Título': 'Uma Forca á Sua Espera',
'Autor': 'Logan',
'Instituição': 'Valentes',
'Ano': '1945 – 1ª Edição',
'Nº de Páginas': '198',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição ' :
'O gerente do banco é assassinado. Encontrado no local do crime, Pat Morrisson é o principal suspeito. Ele tinha dividas a saldar, e discutira com o morto, mais cedo, no mesmo dia. Julgado, Pat é condenado à forca. Porém, sua noiva Mona e o ajudante Ciryl vão sair à caça do verdadeiro assassino para libertar.'
      },
      6:{
          'id': 6,
          'capa' : 'https://www.baixelivros.com.br/media/2019/03/lei-pistoleiros.jpg',
          'Título': 'A Lei dos Pistoleiros',
'Autor': 'Estefânia',
'Instituição':' Marcial',
'Ano': '1980 – 1ª Edição',
'Nº de Páginas':' 126',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição ' :
'O jovem juiz Jeff Brocks despertava sempre uma desconfiança inicial onde era nomeado, e logo depois, o ódio, pois aplicava a lei rigorosamente e sem piedade. Quando se encarregou da violenta e sem lei, Silver City, passou a punir uma horda de malfeitores, encarregados de saloons irregulares.'
      },
      7:{
          'id': 7,
          'capa' : 'https://www.baixelivros.com.br/media/2019/04/protecao-testemunha.jpg',
          'Título': 'Proteção à Testemunha',
'Autor': 'Dayla Assuky',
'Instituição':' D.A.',
'Ano': '2015 – 1ª Edição',
'Nº de Páginas':' 091  ',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',

'Descrição' :
'Mari é uma jovem que esta vivendo nesta situação difícil. Testemunha de um assassinato frio e cruel ela pode tornar-se a próxima vitima. Não existe crime perfeito, mas existe dinheiro e falta de caráter! Se por um lado a vida nos derruba, por outro nos mostra como levantar e seguir em frente.'

      },
      8:{
          'id': 8,
          'capa' : 'https://www.baixelivros.com.br/media/2020/02/colarinho-branco.jpg',
         ' Título':' Horas de Terror',
'Autor': 'Luger',
'Instituição': 'db',
'Ano': '1955 – 1ª Edição',
'Nº de Páginas': '064',
'Tipo': 'Livro Digital',
'Formato':' .pdf',
'Licença':' Domínio Público',


'Descrição' :
'Raymond Duc, agente do Deuxíème Bureau, acabou de dar o laço em sua gravata borboleta, na frente do espelho. Estava contente com o tom bronzeado obtido depois de cinco dias consecutivos de praia. Aquela vidinha boa sem fazer nada…'


      },
      9:{
          'id': 9,
          'capa' : 'https://www.baixelivros.com.br/media/2019/03/lua-comance.jpg',
          'Título': 'Lua Comanche',
'Autor': 'Sagan',
'Instituição': 'Oregon',
'Ano': '1940 – 1ª Edição',
'Nº de Páginas': '132',
'Tipo': 'Livro Digital',
'Formato': '.pdf',
'Licença': 'Domínio Público',

'Descrição' :
'Clifford Marshand, caçador de peles, era atormentado por sonhos recorrentes onde um assassino que ele não conseguia identificar, matava jovens índias. Capturado pelo chefe dos comanches, já não tinha mais esperança de salvação. Seu destino seria escalpo e morte terrível.'
      },
      10:{
          'id': 10,
          'capa' : 'https://www.baixelivros.com.br/media/2020/02/o-salario-terrivel.jpg',
          'Título': 'O Salário Terrível',
'Autor':' L. Carry',
'Instituição': 'Monterrey',
'Ano': '1969 – 1ª Edição',
'Nº de Páginas': '115',
'Tipo':'Livro Digital',
'Formato': '.pdf',
'Licença': 'Gratuito',


'Descrição' :
'Uma rememoração da primeira missão da agente Baby para a CIA: Contrabando de esmeraldas da Colômbia para financiar a compra de armas pesadas em Cuba para uma revolução armada no Caribe.'
      },
}   

def response_Cordel():
    return {'Cordel' : list(Cordel_livros.values())}

@app.route('/Cordel')
def list_Cordel():
    return response_Cordel() 

# 



        
if __name__ == "__main__" :

 app.run(debug=True)



