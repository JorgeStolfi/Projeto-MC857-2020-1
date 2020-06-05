import trecho_IMP; from trecho_IMP import Objeto_Trecho_IMP

class Objeto_Trecho(Objeto_Trecho_IMP):
  """Um objeto desta classe representa uma viagem de um veículo entre duas
  escalas, em uma determinada data e hora, armazena seus atributos. É
  uma subclasse de {Objeto}.
  
  O identificador de um trecho é uma string da forma
  "T-{NNNNNNNN}" onde {NNNNNNNN} é o índice na tabela (vide abaixo)
  formatado em 8 algarismos.

  Por enquanto, o dicionário de atributos de um objeto desta classe
  contém os seguintes campos:

    'codigo'       código do trecho na empresa (p. ex. "AZ 4623").
    'origem'       sigla da estação/porto/aeroporto de orígem.
    'destino'      sigla da estação/porto/aeroporto de destino.
    'dia_partida'  data de partida (string "{YYYY}-{MM}-{DD}").
    'hora_partida' horário de partida (string "{hh}:{mm}").
    'dia_chegada'  data de chegada (string "{YYYY}-{MM}-{DD}").
    'hora_chegada' horário de chegada (string "{hh}:{mm}").
    
  As datas e horários são sempre referentes ao fuso horário UTC.  Outros atributos 
  poderão ser acrescentados no futuro.
  
  REPRESENTAÇÃO NA BASE DE DADOS

  Cada trecho (como definido aqui) é representado por uma linha na
  tabela "trechos" da base SQL em disco. Apenas algumas dessas linhas
  são representadas também na memória por objetos da classe
  {Objeto_Trecho}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos do trecho."""
  pass

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela de trechos na base de dados.
  Não retorna nenhum valor. Deve ser chamada apenas uma vez no ínicio da
  execução do servidor, depois de chamar {base_sql.conecta} e {poltrona.inicializa}. 
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  trecho_IMP.inicializa(limpa)

def cria(atrs_mem):
  """Cria um novo objeto da classe {Objeto_Trecho}, com os atributos especificados
  pelo dicionário Python {atrs}, acrescentando-o à tabéla de trechos da base de dados.
  Atribui um identificador único ao trecho, derivado do seu índice na tabela.
  
  Não pode haver outro trecho com mesmo 'codigo', 'data_partida', e 'hora_partida'.
  
  Em caso de sucesso, retorna o objeto criado.  Caso contrário, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro."""
  return trecho_IMP.cria(atrs_mem)

def muda_atributos(trc, mods_mem):
  """Modifica alguns atributos do objeto {trc} da classe {Objeto_Trecho},
  registrando as alterações na base de dados.

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do trecho (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {mods}.

  Se o 'codigo', 'dia_partida', ou 'hora_partida' for alterado, não 
  pode existir nenum outro trecho na tabela com esses mesmos dados.
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  trecho_IMP.muda_atributos(trc, mods_mem)

def obtem_identificador(trc):
  """Devolve o identificador 'T-{NNNNNNNN}' do trecho."""
  return trecho_IMP.obtem_identificador(trc)

def obtem_atributos(trc):
  """Retorna um dicionário Python que é uma cópia dos atributos do trecho,
  exceto identificador."""
  return trecho_IMP.obtem_atributos(trc)

def obtem_atributo(trc, chave):
  """Retorna o atributo do trecho {trc} com a {chave} dada. 
  Equivale a {obtem_atributos(trc)[chave]}"""
  return trecho_IMP.obtem_atributo(trc, chave)

def busca(args):
  """O parâmetro {args} é um dicionário que contém um subconjunto dos
  atributos de um {Objeto_Trecho}, pelo menos um dos atributos deve estar definido e todos os atributos definitos
  devem ser diferentes de None.
  Localiza trechos pelos atributos definidos em {args}.
  Devolve uma lista dos identificadores desses trechos (NÃO os trechos),
  por exemplo ['T-00000001', 'T-00000025'].
  Devolve uma lista vazia se não existir nenhum trecho nessas condições."""
  return trecho_IMP.busca(args)

def busca_por_identificador(id_trecho):
  """Localiza um trecho com identificador {id_trecho} (uma string da forma
  "T-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {Objeto_Trecho}.
  Se tal trecho não existe, devolve {None}."""
  return trecho_IMP.busca_por_identificador(id_trecho)

def obtem_poltronas(trc):
  """Devolve uma lista com os identificadores das poltronas do trecho."""
  return trecho_IMP.obtem_poltronas(trc)

def busca_por_origem(cod):
  """Devolve uma lista de identificadores (NÃO objetos) de todos os trechos
  através de uma string codigo de origem do aeroporto."""
  return trecho_IMP.busca_por_origem(cod)

def busca_por_codigo_e_data(cod, dia, hora):
  """Localiza um trecho cujo 'codigo' é {cod}, 'dia_partida'
  é {dia}, e 'hora_partida' é {hora}, e devolve o identificador 
  do mesmo (não o objeto); ou {None} se não existir tal trecho.
  Não deve existir mais de um trecho nessas condições.
  
  O dia deve estar no formato ISO, "{YYYY}-{MM}-{DD}", e 
  a hora deve estar no formato "{hh}:{mm}", onde
  o mes {MM}, o dia {DD}, as horas {hh} e os minutos {mm}
  devem ter sempre 2 dígitos."""
  return trecho_IMP.busca_por_codigo_e_data(cod, dia, hora)

def busca_por_origem_e_destino(origem, destino):
  """Localiza trechos cujo atributo 'origem' é {origem} e cujo 'destino'
  é {destino}.  Devolve uma lista dos identificadores desses trechos (NÃO os trechos), 
  por exemplo ['T-00000001', 'T-00000025'].
  Devolve uma lista vazia se não existir nenhum trecho nessas condições."""
  return trecho_IMP.busca_por_origem_e_destino(origem, destino)

def busca_por_dias(dia_min, dia_max):
  """Localiza trechos com 'dia_partida' entre {dia_min} e {dia_max},
  e devolve uma lista com os identificadores dos mesmos (não os objetos), 
  por exemplo ['T-00000001', 'T-00000025'].  Devolve uma  lista vazia
  se não existir nenhum trecho nessas condições.
  
  Os dois dias devem estar no formato ISO, "{YYYY}-{MM}-{DD}".
  O mes {MM} e o dia {DD} devem ter sempre 2 dígitos."""
  return trecho_IMP.busca_por_dias(dia_min, dia_max)

# FUNÇÕES PARA DEPURAÇÃO

def verifica(trc, id, atrs):
  """Faz testes de consistência básicos de um objeto {trc} de classe {Objeto_Trecho}, 
  dados o identificador esperado {id}, e os atributos esperados {atrs}.
  
  Especificamente, verifica as funções {obtem_identificador(trc)},
  {obtem_atributos(trc)} e {busca_por_identificador(id)}.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return trecho_IMP.verifica(trc, id, atrs)

def cria_testes():
  """Limpa a tabela de trechos com {inicializa(True)}, e cria pelo menos três trechos
  para fins de teste, incluindo-os na tabela.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {base_sql.conecta}.""" 
  trecho_IMP.cria_testes()

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  trecho_IMP.diagnosticos(val)
