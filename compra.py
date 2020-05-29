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
  feito por um cliente, consistindo de uma lista de bilhetes.
  Os atributos deste objeto, por enquanto, são:
    
    'cliente'  {Objeto_Usuario} o cliente que fez ou está fazendo o pedido de compra.
    'status'   {str}            o estado do pedido.
    'itens'    {list}           os itens (bilhetes individuais) do pedido de compra.

  O atributo 'status' por enquanto, pode ser:

   'aberto': O cliente ainda está montando o pedido, escolhendo forma de pagamento, etc.
   'pagando':  O cliente finalizou o pedido de compra, e a loja está aguardando o pagamento.
   'pago': A loja já recebeu o pagamento e está finalizando as reservas.
   'finalizado': A loja já finalizou as reservas.

  Mais campos e/ou estados poderão ser acrescentados no futuro.
   
  Note que os itens do pedido de compra não são armazenados na 
  tabela "compras", mas numa tabela separada "itens_de_compras".
  
  Além desses atributos, cada pedido de compra também tem um identificador de
  compra, uma string da forma "C-{NNNNNNNN}" onde {NNNNNNNN} é o índice
  na tabela (vide abaixo) formatado em 8 algarismos.
  
  Cada pedido de compra pertence a um unico usuário, mas cada usuário
  pode ter vários pedidos ainda não finalizados ao mesmo tempo. Por
  exemplo, o cliente da loja virtual pode ser uma agência de turismo,
  que teria um pedido de compra separada para cada um de seus clientes.

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
 
def cria(cliente):
  """Cria um novo objeto da classe {Objeto_Compra}, associada ao {cliente} (um
  objeto da classe {Objeto_Usuario}), acrescentando-o à tabela de compras da
  base de dados. inicialmente aberta, com o cookie inicial {cookie} e
  carrinho de pedidos de compra {carrinho}. O status será inicialmente
  'aberto'. Atribui um identificador único à compra, derivado do seu
  índice na tabela.

  Em caso de sucesso, retorna o objeto.  Se os parâmetros 
  forem inválidos ou incompletos, retorna uma ou mais mensagens
  de erro, na forma de uma lista de strings. """
  return compra_IMP.cria(cliente)

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
  """Retorna o estado do pedido de compra {cpr} ('aberto', 'pagando', etc.).
  Equivale a {compra.obtem_atributos(cpr,'status')}."""
  return compra_IMP.obtem_status(cpr)

def obtem_poltronas(cpr):
  """Devolve as poltronas (bilhetes) no pedido de compra {cpr},
  na forma de uma lista cujos elementos são itentificadores de poltronas
  ("A-{NNNNNNNN}")."""
  return compra_IMP.obtem_poltronas(cpr)

def busca_por_identificador(id):
  """Localiza um pedido de compra com identificador {id} (uma string da forma
  "C-{NNNNNNNN}"), e devolve a mesma na forma de um objeto da classe {Objeto_Compra}.
  Se tal compra não existe, devolve {None}."""
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

def muda_atributos(cpr, mods_mem):
  """Recebe um dicionário Python {mods_mem} cujas chaves são um subconjunto
  dos nomes de atributos do pedido de compra (exceto o identificador e a lista 
  de itens). Troca os valores desses atributos no objeto {cpr} da classe {Objeto_Compra}
  pelos valores correspondentes em {mods_mem}.  Também altera esses 
  campos na base de dados. Os valores devem estar no formato de
  atributos na memória."""
  compra_IMP.muda_atributos(cpr, mods_mem)

def fecha(cpr):
  """Muda o status do pedido de compra {cpr} de 'aberto' para 'pagando' e salva o novo
  status da compra no banco de dados."""
  compra_IMP.fecha(cpr)

# DEPURAÇÂO

def verifica(cpr, id, atrs):
  """Faz testes de consistência básicos de um objeto {cpr} de classe {Objeto_Compra}, 
  dados o identificador esperado {id}, e os atributos esperados {atrs}.
  
  Especificamente, verifica as funções {obtem_identificador(cpr)},
  {obtem_atributos(cpr)} e {busca_por_identificador(id)}.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return compra_IMP.verifica(cpr, id, atrs)

def cria_testes():
  """Limpa a tabela de pedidos de compras com {inicializa(True)}, e cria alguns 
  pedidos para fins de teste, incluindo-as na tabela.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {base_sql.conecta}.Supõe que a tabela de usuários 
  já foi inicializada e tem pelo menos três entradas.""" 
  compra_IMP.cria_testes()

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  compra_IMP.diagnosticos(val)
