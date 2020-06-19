import poltrona_IMP; from poltrona_IMP import Objeto_Poltrona_IMP

class Objeto_Poltrona(Objeto_Poltrona_IMP):
  """Um objeto desta classe representa uma poltrona em determinado trecho
  (ou seja, em uma determinada viagem de um determinado veículo
  numa viagem uma entre duas escalas, em uma determinada data e hora). É
  uma subclasse de {Objeto}.

  O identificador de uma poltrona é uma string da forma
  "A-{NNNNNNNN}" onde {NNNNNNNN} é o índice na tabela (vide abaixo)
  formatado em 8 algarismos.  Toda poltrona é parte de um
  único trecho, e pode estar reservado para no maximo um
  pedido de compra.

  Por enquanto, o dicionário de atributos de um ojeto desta classe
  contém os seguintes campos:

    'id_trecho'    identificador "T-{NNNNNNNN}" do trecho de que este poltrona é parte.
    'id_compra'    identificador "C-{NNNNNNNN}" da compra, ou {None} se livre.
    'oferta'       booleano que diz se a poltrona está em oferta.
    'numero'       número da poltrona no veículo
    'bagagens'     quantidade de bagagens relacionadas a compra, ou {None} se livre.
    'preco'        preço da passagem nesta poltrona.
    
  Outros atributos (classe, etc.) poderão 
  ser acrescentados no futuro.

  REPRESENTAÇÃO NA BASE DE DADOS

  Cada poltrona (como definido aqui) é representado por uma linha na
  tabela "poltronas" da base SQL em disco. Apenas algumas dessas linhas
  são representadas também na memória por objetos da classe
  {Objeto_Poltrona}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos da poltrona."""
  pass

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela de poltronas na base de dados.
  Não retorna nenhum valor. Deve ser chamada apenas uma vez no ínicio da
  execução do servidor, depois de chamar {base_sql.conecta} e {poltrona.inicializa}.
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  poltrona_IMP.inicializa(limpa)

def cria(atrs_mem):
  """Cria um novo objeto da classe {Objeto_Poltrona}, com os atributos especificados
  pelo dicionário Python {atrs}, acrescentando-o à tabéla de poltronas da base de dados.
  Atribui um identificador único à poltrona, derivado do seu índice na tabela.

  Não pode haver outra poltrona com mesmo 'id_trecho' e 'numero'.

  Em caso de sucesso, retorna o objeto criado.  Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro."""
  return poltrona_IMP.cria(atrs_mem)

def muda_atributos(pol, mods_mem):
  """Modifica alguns atributos do objeto {pol} da classe {Objeto_Poltrona},
  registrando as alterações na base de dados.

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos da poltrona (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {mods}.

  Se o 'id_trecho' ou 'numero' for alterado, não pode existir nenhuma outra
  poltrona na tabela com esses mesmos dados.

  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  poltrona_IMP.muda_atributos(pol, mods_mem)

def obtem_identificador(pol):
  """Devolve o identificador 'A-{NNNNNNNN}' da poltrona."""
  return poltrona_IMP.obtem_identificador(pol)

def obtem_atributos(pol):
  """Retorna um dicionário Python que é uma cópia dos atributos da poltrona,
  exceto identificador."""
  return poltrona_IMP.obtem_atributos(pol)

def obtem_atributo(pol, chave):
  """Retorna o atributo da poltrona {pol} com a {chave} dada.
  Equivale a {obtem_atributos(pol)[chave]}"""
  return poltrona_IMP.obtem_atributo(pol, chave)

def busca_por_identificador(id_poltrona):
  """Localiza uma poltrona com identificador {id_poltrona} (uma string da forma
  "A-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {Objeto_Poltrona}.
  Se {id_poltrona} é {None} ou tal poltrona não existe, devolve {None}."""
  return poltrona_IMP.busca_por_identificador(id_poltrona)

def busca_por_trecho(trc):
  """Devolve uma lista de identificadores (NÃO objetos) das poltronas
  no trecho {trc}."""
  return poltrona_IMP.busca_por_trecho(trc)

def busca_por_compra(cpr):
  """Devolve uma lista de identificadores (NÃO objetos) de todos  as poltronas
  reservados pelo pedido de compra {cpr}."""
  return poltrona_IMP.busca_por_compra(cpr)
  
def busca_ofertas():
  """Devolve uma lista com todas as poltronas livres em oferta."""
  return poltrona_IMP.busca_ofertas()
  
def cria_conjunto(trc, txt):
  """Cria um conjunto de poltronas do trecho {trc} especificadas pela cadeia {txt}.
  As poltronas inicialmente são livres (sem nenhuma compra associada). 
  
  A cadeia {txt} deve consistir de zero ou mais séries separadas por ponto-e-vírgula (';'). Cada série
  tem uma lista de números de poltronas, seguida de dois pontos (':'), seguidos pelo preço
  comum a todas as poltronas dessa série.  
  
  Os elementos de uma lista de poltronas são separados por vírgulas (','). Cada elemento
  é um número de poltrona, ou dois números separados por hífen ('-').
  Cada número é um inteiro positivo, seguido opcionalmente de uma letra maiúscula.
  
  Um intervalo "{x}-{y}" representa todos os inteiros entre os dois inteiros dados,
  combinados com todas as letras entre as duas letras dadas. 
  
  Espaços em branco são ignorados.  Zeros à esquerda nos números são eliminados.
  
  Por exemplo, se {txt} for "001, 05, 5B, 7-10, 12A-15D: 90.50; 04K-6M: 130.00"
  as poltronas são "1", "5", "5B", "7", "8", "9", "10", "12A", "12B", "12C", "12D",
  "13A", "13B", "13C", "13D", "14A", ..., "15C", "15D", todas com preço 90.50;
  e "4K", "4L", "4M", "5K", "5L", "5M", "6K", "6L", "6M", todas com preço 130.00.
  
  O trecho não deve ser {None}, e não pode já possuira nenhuma dessas poltronas.
  
  Em caso de sucesso, devolve uma lista das poltronas criadas, na forma de objetos
  do tipo {Objeto_Poltrona}.
  
  Em caso de erro nos argumentos, levanta a exceção {ErroAtrib} com 
  mensagem explicativa como argumento."""
  return poltrona_IMP.cria_conjunto(trc, txt)
  
# FUNÇÕES AUXILIARES:

def analisa_esp_conjunto(txt):
  """Destrincha a cadeia {txt}, no formato descrito na função
  {cria_conjunto}.
  
  Devolve uma lista de pares. Cada par consiste do número de uma
  poltrona (um string) e seu preço (um float). Em caso de erro de
  sintaxe, levanta a exceção {ErroAtrib} com uma explicação como
  argumento."""

# FUNÇÕES PARA DEPURAÇÃO

def verifica(pol, id, atrs):
  """Faz testes de consistência básicos de um objeto {pol} de classe {Objeto_Poltrona},
  dados o identificador esperado {id}, e os atributos esperados {atrs}.

  Especificamente, verifica as funções {obtem_identificador(pol)},
  {obtem_atributos(pol)} e {busca_por_identificador(id)}.

  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return poltrona_IMP.verifica(pol, id, atrs)

def cria_testes():
  """Limpa a tabela de poltronas com {inicializa(True)}, e cria pelo menos três poltronas
  para fins de teste, incluindo-os na tabela.  Não devolve nenhum resultado.

  Deve ser chamada apenas uma vez no ínicio da execução do programa,
  depois de chamar {base_sql.conecta}."""
  poltrona_IMP.cria_testes()

def lista_livres(trc):
  """Retorna uma lista das poltronas do trecho {trc} que estão livres."""
  poltrona_IMP.lista_livres(trc)

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas
  funções deste módulo."""
  poltrona_IMP.diagnosticos(val)
