# Este módulo define funções para verificar a validade de dados digitados
# pelo usuário em diversos formulários.

# Cada função abaixo verifica se o parâmetro {val}
# satisfaz certas condições. Em caso afirmativo,
# a função devolve uma lista vazia.  Senão devolve uma lista de 
# uma ou mais mensagens de erro (strings).  O parâmetro 
# {rotulo} é usado para montar as mensagens de erro.

# O parâmetro booleano {nulo_ok} diz se {None} deve ser considerado
# um valor válido de {val} (se {True}) ou não (se {False}).

import valida_campo_IMP

class ErroAtrib(Exception):
  pass

def nome_de_usuario(rotulo, val, nulo_ok):
  """Exige que o parâmetro {val} seja um string com aparência de
  nome de usuário, com no mínimo 10 e no máximo 60 caracteres.
  São permitidas letras acentuadas, brancos, hífen, ponto, e apóstrofe."""
  return valida_campo_IMP.nome_de_usuario(rotulo, val, nulo_ok)
  
def CPF(rotulo, val, nulo_ok):
  """Exige que {val} seja um string com aparência de
  CPF: "{NNN}.{NNN}.{NNN}-{NN}" onde cada {N} é um algarismo.
  Deveria verificar os dígitos de controle também."""
  return valida_campo_IMP.CPF(rotulo, val, nulo_ok)
  
# def linha_de_endereco(rotulo, val, nulo_ok):
#   """Exige que {val} seja uma linha de endereço, 
#   com mínimo 3 e máximo 60 caracteres, incluindo..."""
#   # !!! Completar !!!
#   return valida_campo_IMP.linha_de_endereco(rotulo, val, nulo_ok)
  
def cidade_UF(rotulo, val, nulo_ok):
  """ !!! documentar !!! """
  return valida_campo_IMP.cidade_UF(rotulo, val, nulo_ok)
  
def senha(rotulo, val, nulo_ok):
  """ !!! documentar !!! """
  return valida_campo_IMP.senha(rotulo, val, nulo_ok)

def email(rotulo, val, nulo_ok):
  """ !!! documentar !!! """
  return valida_campo_IMP.email(rotulo, val, nulo_ok)

# def endereco(rotulo, val, nulo_ok):
#   """ !!! documentar !!! """
#   return valida_campo_IMP.endereco(rotulo, val, nulo_ok)

def CEP(rotulo, val, nulo_ok):
  """ !!! documentar !!! """
  return valida_campo_IMP.CEP(rotulo, val, nulo_ok)

def telefone(rotulo, val, nulo_ok):
  """ !!! documentar !!! """
  return valida_campo_IMP.telefone(rotulo, val, nulo_ok)

def documento(rotulo, val, nulo_ok):
  """ !!! documentar !!! """
  return valida_campo_IMP.documento(rotulo, val, nulo_ok)

def booleano(rotulo, val, nulo_ok):
  """Exige que o parâmetro {val} seja um booleano."""
  return valida_campo_IMP.booleano(rotulo, val, nulo_ok)

def identificador(rotulo, val, letra, nulo_ok):
  """Exige que o parâmetro {val} seja um string com aparência de
  identificador, no formato "{L}-{NNNNNNNN} onde {L} é a {letra}
  dada e {NNNNNNNN} são 8 dígitos decimais.  Se {letra} for {None},
  aceita qualquer letra maiúscula."""
  return valida_campo_IMP.identificador(rotulo, val, letra, nulo_ok) 

def id_trecho(rotulo, val, nulo_ok):
  """Exige que o parâmetro {val} seja um string com aparência de
  identificador de trecho, ou seja "T-{NNNNNNNN}". """
  return valida_campo_IMP.id_trecho(rotulo, val, nulo_ok) 

def id_compra(rotulo, val, nulo_ok):
  """Exige que o parâmetro {val} seja um string com aparência de
  idetificador de compra, ou seja "C-{NNNNNNNN}"."""
  return valida_campo_IMP.id_compra(rotulo, val, nulo_ok) 

def numero_de_poltrona(rotulo, val, nulo_ok):
  """Exige que o parâmetro {val} seja uma string, com aparência de
  numero de poltrona, ou seja um inteiro positivo opcionalmente seguido
  de uma letra maiúscula."""
  return valida_campo_IMP.numero_de_poltrona(rotulo, val, nulo_ok) 

def num_de_bagagens(rotulo, val, nulo_ok):
  """Exige que o parâmetro {val} seja uma contagem de bagagens,
  ou seja um inteiro não negativo."""
  return valida_campo_IMP.num_de_bagagens(rotulo, val, nulo_ok) 

def preco(rotulo, val, nulo_ok):
  """Exige que o parâmetro {val} seja um preço, ou seja um float 
  não-negativo que é múltiplo de 0.01 (a menos de erros de 
  arredondamento do formato float)."""
  return valida_campo_IMP.preco(rotulo, val, nulo_ok) 

# !!! Completar !!!

