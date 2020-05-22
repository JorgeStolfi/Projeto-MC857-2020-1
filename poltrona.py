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
    'numero'       número da poltrona no veículo
    'bagagens'     quantidade de bagagens relacionadas a compra, ou {None} se livre.
    
  Outros atributos (como preço, limite de bagagem, classe, etc.) poderão 
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
  Se tal poltrona não existe, devolve {None}."""
  return poltrona_IMP.busca_por_identificador(id_poltrona)

def busca_por_trecho(trc):
  """Devolve uma lista de identificadores (NÃO objetos) das poltronas
  no trecho {trc}."""
  return poltrona_IMP.busca_por_trecho(trc)

def busca_por_compra(cpr):
  """Devolve uma lista de identificadores (NÃO objetos) de todos  as poltronas
  reservados pelo pedido de compra {cpr}."""
  return poltrona_IMP.busca_por_compra(cpr)

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
