# Este módulo define a classe de objetos {Objeto_Compra}, que
# representa uma lista de bilhetes comprados por um cliente
# da loja virtual.
#

# Interfaces importadas por esta interface:
import usuario

# Implementaçao deste módulo:
import compra_IMP; from compra_IMP import Objeto_Compra_IMP

class Objeto_Compra(Objeto_Compra_IMP):
  """Um objeto desta classe representa um pedido de compra
  feito por um cliente, consistindo de uma viagem por um único passageiro
  Os atributos deste objeto, por enquanto, são:

    'cliente'   {Objeto_Usuario} o cliente que fez ou está fazendo o pedido de compra.
    'status'    {str}            o estado do pedido.
    'nome_pass' {str}            o nome do passageiro que fará a viagem.
    'doc_pass'  {str}            documento do passageiro que fará a viagem.
    'itens'     {list}           os itens (bilhetes individuais) do pedido de compra.

  O atributo 'status' por enquanto, pode ser:

   'comprando': O cliente ainda está montando o pedido, escolhendo forma de pagamento, etc.
   'pagando':  O cliente finalizou o pedido de compra, e a loja está aguardando o pagamento.
   'pago': A loja já recebeu o pagamento e está finalizando as reservas.
   'finalizado': A loja já finalizou as reservas.

  Mais campos e/ou estados poderão ser acrescentados no futuro.

  Além desses atributos, cada pedido de compra também tem um identificador de
  compra, uma string da forma "C-{NNNNNNNN}" onde {NNNNNNNN} é o índice
  na tabela (vide abaixo) formatado em 8 algarismos.

  Os itens são uma lsta de bilhetes individuais.  Cada
  bihete é representado por um objeto de tipo {Objeto_Poltrona}
  (vide {poltrona.py}).

  Cada bilhete (poltrona) deve pertencer a um trecho
  ({Objeto_Trecho}) distinto.

  Os bilhetes devem estar em ordem cronológica;
  ou seja, a data+hora da chegada do trecho de cada bilhete
  deve ser menor que a data+hora de partida do trecho
  do bilhete seguinte.

  Note que os itens do pedido de compra não são armazenados na
  tabela "compras", mas numa tabela separada "itens_de_compras".

  Cada pedido de compra pertence a um unico usuário da loja, mas cada
  pode ter vários pedidos ainda não finalizados ao mesmo tempo. Por
  exemplo, o cliente da loja virtual pode ser uma agência de turismo,
  que teria um pedido de compra separada para cada um de seus clientes.

  Note que o pasageiro (atributo 'nome_pass') não é necessariamete
  o usuário da loja virtual que está montando o pedido (atributo 'cliente'),
  e não precisa estar cadastrado na loja virtual.

  REPRESENTAÇÃO NA BASE DE DADOS

  Cada pedido de compra do sistema é representada por uma
  linha na tabela "compras" da base SQL em disco. Apenas algumas dessas
  linhas são representadas também na memória por objetos da classe
  {Objeto_Compra}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos do pedido de compra
  (menos o identificador). """

# Nas funções abaixo, {cliente} é um objeto da classe {Objeto_Usuario}
# que representa o cliente.

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela "compras" na base de dados.
  Deve ser chamada apenas uma vez no ínicio da execução do servidor,
  depois de chamar {base_sql.conecta} e {poltrona.inicializa}.  Não retorna nenhum valor.
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  compra_IMP.inicializa(limpa)

def cria(cliente, nome_pass="", doc_pass=""):
  """Cria um novo objeto da classe {Objeto_Compra}, associada ao {cliente} (um
  objeto da classe {Objeto_Usuario}), acrescentando-o à tabela de compras da
  base de dados. inicialmente aberta, com o cookie inicial {cookie} e
  carrinho de pedidos de compra {carrinho}. O status será inicialmente
  'comprando'. Atribui um identificador único à compra, derivado do seu
  índice na tabela.

  Em caso de sucesso, retorna o objeto.  Se os parâmetros
  forem inválidos ou incompletos, retorna uma ou mais mensagens
  de erro, na forma de uma lista de strings. """
  return compra_IMP.cria(cliente, nome_pass, doc_pass)

def obtem_identificador(cpr):
  """Devolve o identificador 'C-{NNNNNNNN}' do pedido de compra {cpr}."""
  return compra_IMP.obtem_identificador(cpr)

def obtem_atributos(cpr):
  """Retorna um dicionário Python que é uma cópia dos atributos do pedido de compra {cpr},
  exceto identificador e a lista de itens."""
  return compra_IMP.obtem_atributos(cpr)

def obtem_atributo(cpr, chave):
  """Retorna o atributo da compra {cpr} com a {chave} dada.
  Equivale a {obtem_atributos(cpr)[chave]}"""
  return compra_IMP.obtem_atributo(cpr, chave)

def obtem_cliente(cpr):
  """Retorna o objeto da classe {Objeto_Usuario} correspondente ao usuario que
  montou ou está montando o pedido de compra {cpr}.  Equivale a
  {compra.obtem_atributo(cpr,'cliente')}. """
  return compra_IMP.obtem_cliente(cpr)

def obtem_status(cpr):
  """Retorna o estado do pedido de compra {cpr} ('comprando', 'pagando', etc.).
  Equivale a {compra.obtem_atributos(cpr,'status')}."""
  return compra_IMP.obtem_status(cpr)

def obtem_poltronas(cpr):
  """Devolve as poltronas (bilhetes) no pedido de compra {cpr},
  na forma de uma lista cujos elementos são itentificadores de poltronas
  ("A-{NNNNNNNN}").  A lista eatará em ordem cronológica da data e hora
  de partida dos trechos correspondentes. """
  return compra_IMP.obtem_poltronas(cpr)

def busca_por_campos(args):
  """O parâmetro {args} é um dicionário que contém um subconjunto dos
  atributos de um {Objeto_Compra}, pelo menos um dos atributos deve estar definido e todos os atributos definitos
  devem ser diferentes de None.
  Localiza trechos pelos atributos definidos em {args}.
  Devolve uma lista dos identificadores desses trechos (NÃO os trechos),
  por exemplo ['C-00000001', 'C-00000025'].
  Devolve uma lista vazia se não existir nenhum trecho nessas condições."""
  return compra_IMP.busca_por_campos(args)

def busca_por_identificador(id):
  """Localiza um pedido de compra com identificador {id} (uma string da forma
  "C-{NNNNNNNN}"), e devolve a mesma na forma de um objeto da classe {Objeto_Compra}.
  Se {id} é {None} ou tal compra não existe, devolve {None}."""
  return compra_IMP.busca_por_identificador(id)

def busca_por_cliente(id_cliente):
  """Localiza os pedidos de compra feitas pelo usuário com identificado {id_cliente}
  e devolve a lista dos identificadores dos pedidos de compras (NÃO uma lista de objetos),
  em qualquer status, associadas a esse cliente. Se não existirem tais compras,
  devolve uma lista vazia."""
  return compra_IMP.busca_por_cliente(id_cliente)

def calcula_preco(cpr):
  """Devolve o preço total da compra, que é a soma dos
  preços de todos os bilhetes (poltronas) atualmente na mesma."""
  return compra_IMP.calcula_preco(cpr)
  
def trecho_eh_compativel(cpr, trc):
  """Devolve {True} se os horários e aeroportos do trecho {trc} são 
  compatíveis com os dos trechos atualmente em {cpr}."""
  return compra_IMP.trecho_eh_compativel(cpr, trc)

def muda_atributos(cpr, mods_mem):
  """Recebe um dicionário Python {mods_mem} cujas chaves são um subconjunto
  dos nomes de atributos do pedido de compra (exceto o identificador e a lista
  de itens). Troca os valores desses atributos no objeto {cpr} da classe {Objeto_Compra}
  pelos valores correspondentes em {mods_mem}.  Também altera esses
  campos na base de dados. Os valores devem estar no formato de
  atributos na memória."""
  compra_IMP.muda_atributos(cpr, mods_mem)

def fecha(cpr):
  """Muda o status do pedido de compra {cpr} de 'comprando' para 'pagando' e salva o novo
  status da compra no banco de dados."""
  compra_IMP.fecha(cpr)

def verificar_baldeacao(cpr):
  """Devolve uma lista de identificadores de {cpr} que não têm tempo suficiente de
  baldeação."""
  return compra_IMP.verificar_baldeacao(cpr)

# DEPURAÇÂO

def verifica(cpr, id, atrs):
  """Faz testes de consistência básicos de um objeto {cpr} de classe {Objeto_Compra},
  dados o identificador esperado {id}, e os atributos esperados {atrs}.

  Especificamente, verifica as funções {obtem_identificador(cpr)},
  {obtem_atributos(cpr)} e {busca_por_identificador(id)}.

  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return compra_IMP.verifica(cpr, id, atrs)

def cria_testes(verb):
  """Limpa a tabela de pedidos de compras com {inicializa(True)}, e cria alguns
  pedidos para fins de teste, incluindo-as na tabela.  Não devolve nenhum resultado.

  Deve ser chamada apenas uma vez no ínicio da execução do programa,
  depois de chamar {base_sql.conecta}.Supõe que a tabela de usuários
  já foi inicializada e tem pelo menos três entradas.
  
  Se {verb} for {True}, escreve uma linha em {sys.stderr}
  para cada objeto criado."""
  compra_IMP.cria_testes(verb)

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas
  funções deste módulo."""
  compra_IMP.diagnosticos(val)
