import assento_IMP; from assento_IMP import Objeto_Assento_IMP

class Objeto_Assento(Objeto_Assento_IMP):
  """Um objeto desta classe representa um assento em determinado trecho
  (ou seja, em uma determinada viagem de um determinado veículo 
  numa viagem uma entre duas escalas, em uma determinada data e hora). É
  uma subclasse de {Objeto}.
  
  O identificador de um assento é uma string da forma
  "A-{NNNNNNNN}" onde {NNNNNNNN} é o índice na tabela (vide abaixo)
  formatado em 8 algarismos.  Todo assento é parte de um 
  único trecho, e pode estar reservado para no maximo um
  pedido de compra.

  Por enquanto, o dicionário de atributos de um ojeto desta classe
  contém os seguintes campos:

    'id_trecho'    identificador "T-{NNNNNNNN}" do trecho de que este assento é parte.
    'id_compra'    identificador "C-{NNNNNNNN}" da compra, ou {None} se livre.
    'numero'       número da poltrona no veículo
    'bagagens'     quantidade de bagagens relacionadas a compra, ou {None} se livre.
    
  Outros atributos (como preço, limite de bagagem, classe, etc.) poderão 
  ser acrescentados no futuro.
  
  REPRESENTAÇÃO NA BASE DE DADOS

  Cada assento (como definido aqui) é representado por uma linha na
  tabela "assentos" da base SQL em disco. Apenas algumas dessas linhas
  são representadas também na memória por objetos da classe
  {Objeto_Assento}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos do assento."""
  pass

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela de assentos na base de dados.
  Não retorna nenhum valor. Deve ser chamada apenas uma vez no ínicio da
  execução do servidor, depois de chamar {base_sql.conecta} e {assento.inicializa}. 
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  assento_IMP.inicializa(limpa)

def cria(atrs_mem):
  """Cria um novo objeto da classe {Objeto_Assento}, com os atributos especificados
  pelo dicionário Python {atrs}, acrescentando-o à tabéla de assentos da base de dados.
  Atribui um identificador único ao assento, derivado do seu índice na tabela.
  
  Não pode haver outro assento com mesmo 'id_trecho' e 'numero'.
  
  Em caso de sucesso, retorna o objeto criado.  Caso contrário, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro."""
  return assento_IMP.cria(atrs_mem)

def muda_atributos(ass, mods_mem):
  """Modifica alguns atributos do objeto {ass} da classe {Objeto_Assento},
  registrando as alterações na base de dados.

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do assento (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {mods}.

  Se o 'id_trecho' ou 'numero' for alterado, não pode existir nenum outro 
  assento na tabela com esses mesmos dados.
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  assento_IMP.muda_atributos(ass, mods_mem)

def obtem_identificador(ass):
  """Devolve o identificador 'A-{NNNNNNNN}' do assento."""
  return assento_IMP.obtem_identificador(ass)

def obtem_atributos(ass):
  """Retorna um dicionário Python que é uma cópia dos atributos do assento,
  exceto identificador."""
  return assento_IMP.obtem_atributos(ass)

def obtem_atributo(ass, chave):
  """Retorna o atributo do assento {ass} com a {chave} dada. 
  Equivale a {obtem_atributos(ass)[chave]}"""
  return assento_IMP.obtem_atributo(ass, chave)

def busca_por_identificador(id_assento):
  """Localiza um assento com identificador {id_assento} (uma string da forma
  "A-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {Objeto_Assento}.
  Se tal assento não existe, devolve {None}."""
  return assento_IMP.busca_por_identificador(id_assento)

def busca_por_trecho(trc):
  """Devolve uma lista de identificadores (NÃO objetos) dos assentos
  no trecho {trc}."""
  return assento_IMP.busca_por_trecho(trc)

def busca_por_compra(cpr):
  """Devolve uma lista de identificadores (NÃO objetos) de todos  os assentos
  reservados pelo pedido de compra {cpr}."""
  return assento_IMP.busca_por_compra(cpr)

# FUNÇÕES PARA DEPURAÇÃO

def verifica(ass, id, atrs):
  """Faz testes de consistência básicos de um objeto {ass} de classe {Objeto_Assento}, 
  dados o identificador esperado {id}, e os atributos esperados {atrs}.
  
  Especificamente, verifica as funções {obtem_identificador(ass)},
  {obtem_atributos(ass)} e {busca_por_identificador(id)}.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return assento_IMP.verifica(ass, id, atrs)

def cria_testes():
  """Limpa a tabela de assentos com {inicializa(True)}, e cria pelo menos três assentos
  para fins de teste, incluindo-os na tabela.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {base_sql.conecta}.""" 
  assento_IMP.cria_testes()

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  assento_IMP.diagnosticos(val)
