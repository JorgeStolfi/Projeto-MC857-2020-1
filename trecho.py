import trecho_IMP; from trecho_IMP import Objeto_Trecho_IMP

class Objeto_Trecho(Objeto_Trecho_IMP):
  """Um objeto desta classe representa uma viagem de um veículo entre duas
  escalas, em uma determinada data e horário, armazena seus atributos. É
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
    'veiculo'      código identificador do onibus/aeronave (formato livre).
    'encerrado'    a atribuição de poltronas não pode mais mudar (booleano).
    
  As datas e horários são sempre referentes ao fuso horário UTC.  O atributo
  'disponive' começa {True} e vira {False} se o voo é cancelado ou quando o embarque 
  é encerrado, e as poltronas não podem mais ser vendidas, canceladas, ou trocadas.
  Outros atributos poderão ser acrescentados no futuro.
  
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
  
def obtem_dia_e_hora_de_partida(trc):
  """Retorna a data e hora de partida do trecho {trc},
  no formato "{YYYY}-{MM}-{DD} {hh}:{mm} UTC"."""
  return trecho_IMP.obtem_dia_e_hora_de_partida(trc)

def obtem_dia_e_hora_de_chegada(trc):
  """Retorna a data e hora de chegada do trecho {trc},
  no formato "{YYYY}-{MM}-{DD} {hh}:{mm} UTC"."""
  return trecho_IMP.obtem_dia_e_hora_de_chegada(trc)

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
  Se {id_trecho} é {None} ou tal trecho não existe, devolve {None}."""
  return trecho_IMP.busca_por_identificador(id_trecho)

def obtem_poltronas(trc):
  """Devolve uma lista com os identificadores das poltronas do trecho."""
  return trecho_IMP.obtem_poltronas(trc)

def obtem_poltronas_livres(trc):
  """Devolve uma lista com os identificadores das poltronas livres do trecho."""
  return trecho_IMP.obtem_poltronas_livres(trc)

def numero_de_poltronas(trc):
  """Devolve o numero {num} de poltronas em um trecho."""
  return trecho_IMP.numero_de_poltronas(trc)

def numero_de_poltronas_livres(trc):
  """Devolve o numero {num} de poltronas livres em um trecho."""
  return trecho_IMP.numero_de_poltronas_livres(trc)

def verificar_disponibilidade(trc):
  """Retorna se o trecho está disponível para compra. Ou seja, se está 
  com atributo 'disponinvel' {True} e tem poltronas livres"""
  return trecho_IMP.verificar_disponibilidade(trc)

def busca_por_origem(cod):
  """Devolve uma lista de identificadores (NÃO objetos) de todos os trechos
  com código de aeroporto de origem {cod}."""
  return trecho_IMP.busca_por_origem(cod)

def busca_por_destino(cod):
  """Devolve uma lista de identificadores (NÃO objetos) de todos os trechos
  com código de aeroporto de destino {cod}."""
  return trecho_IMP.busca_por_destino(cod)

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

def busca_por_origem_e_destino(org, dst, data_min, data_max):
  """Localiza trechos com origem e/ou destino especificados, num intervalo de 
  datas especificado.
  
  Se {org} não for {None}, deve ser um código de porto ("VCP", "SDU", etc.);
  o atributo 'origem' do trecho deve ser {org}.
  
  Se {dst} não for {None}, deve ser um código de porto;
  o atributo 'destino' do trecho deve ser {dst}.
  
  Se {data_min} não for {None}, deve ser uma especificação de data e hora
  no formato "{yyyy}-{mm}-{dd} {HH}-{MM}" (com fuso opcional " UTC");
  o dia e hora de partida do trecho devem ser esses, OU POSTERIORES. 
  
  Se {data_max} não for {None}, deve ser uma especificação de data e hora
  no mesmo formato;
  o dia e hora de chegada do trecho devem ser esses, OU ANTERIORES.
  
  Devolve uma lista dos identificadores dos trechos que satisfazem essas
  condições (NÃO os trechos).  Por exemplo, ['T-00000001', 'T-00000025'].
  Devolve uma lista vazia se não existir nenhum trecho nessas condições."""
  return trecho_IMP.busca_por_origem_e_destino(org, dst, data_min, data_max)

def busca_por_dias(dia_min, dia_max):
  """Localiza trechos com 'dia_partida' entre {dia_min} e {dia_max},
  e devolve uma lista com os identificadores dos mesmos (não os objetos), 
  por exemplo ['T-00000001', 'T-00000025'].  Devolve uma  lista vazia
  se não existir nenhum trecho nessas condições.
  
  Os dois dias devem estar no formato ISO, "{YYYY}-{MM}-{DD}".
  O mes {MM} e o dia {DD} devem ter sempre 2 dígitos."""
  return trecho_IMP.busca_por_dias(dia_min, dia_max)

def resumo_de_trafego(ids_trechos):
  """Data uma lista {ids_trechos} de identificadores de trechos
  (voos), devolve um resumo dessa lista.  
  
  O resultado é uma tupla {(ntr, npol_tot, npol_pag, renda_tot,
  npol_chk)} onde {ntr} é o número de trechos em {L}, {npol_tot} é o
  número total de poltronas desses voos, {npol_pag} é o número de
  poltronas reservadas ou compradas, {renda_tot} é o total dos preços
  dessas poltronas, e {npol_chk} é o número de passageiros desses voos
  que fizeram checkin."""
  return trecho_IMP.resumo_de_trafego(ids_trechos)

def horarios_sao_compativeis(trc1, trc2):
  """Devolve {True} se e somente se os horários e aeroportos 
  dos trechos {trc1} e {trc2} são compatíveis, nessa ordem. Ou seja, 
  a data (dia, hora, e minuto) de chegada do trecho {trc1} 
  é anterior à data de pearida do trecho {trc2}, e
  o intervalo entre eles é suficiente para fazer a baldeação 
  entre os mesmos."""
  return trecho_IMP.horarios_sao_compativeis(trc1, trc2)

def todos_os_aeroportos():
  """Retorna uma lista de todos os códigos de aeroportos de partida ou chegada
  em todos os trechos na base de dados, em ordem alfabética, sem repetições."""
  return trecho_IMP.todos_os_aeroportos()

# FUNÇÕES PARA DEPURAÇÃO

def verifica(trc, id, atrs):

  """Faz testes de consistência básicos de um objeto {trc} de classe {Objeto_Trecho}, 
  dados o identificador esperado {id}, e os atributos esperados {atrs}.
  
  Especificamente, verifica as funções {obtem_identificador(trc)},
  {obtem_atributos(trc)} e {busca_por_identificador(id)}.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return trecho_IMP.verifica(trc, id, atrs)

def cria_testes(verb):
  """Limpa a tabela de trechos com {inicializa(True)}, e cria pelo menos três trechos
  para fins de teste, incluindo-os na tabela.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {base_sql.conecta}.
  
  Se {verb} for {True}, escreve uma linha em {sys.stderr}
  para cada objeto criado.""" 
  trecho_IMP.cria_testes(verb)

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  trecho_IMP.diagnosticos(val)

def mostra(trc):
  """Retorna uma cadeia que descreve sucintamente o trecho {trc},
  para fins de depuração."""
  return trecho_IMP.mostra(trc)
