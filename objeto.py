# Este módulo define a classe geral de objetos {Objeto}, 
# superclasse de objetos como {ObjUsuario}, {ObjPassagem}, etc.

# Implementação deste módulo e da classe {Objeto}:
import objeto_IMP; from objeto_IMP import Objeto_IMP

class Objeto(Objeto_IMP):
  """Um objeto genérico. Possui os seguintes campos privados:
  
    {identificador}   uma string da forma "{X}-{NNNNNNNN}" onde
                      {X} é uma letra que identifica o tipo do objeto
                      ('U' para ObjUsuario, 'S' para ObjSessao, etc)
                      e {NNNNNNNN} é o índice na tabela correspondente
                      da base de dados, formatado em 8 algarismos
                      
    {atrs}            um dicionário Python que contém os atributos 
                      do objeto, específicos para cada classe.
  """
  pass


def cria(atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  """Cria um novo objeto da classe {Objeto} com atributos {atrs}
  e acrescenta-o à tabela {nome_tb}, que deve ter as {colunas} especificadas.
  O identificador será "{L}-{NNNNNNNN}" onde {L} é {letra_tb}
  e {NNNNNNNN} é o índice da linha na tabela, formatada em 8 dígitos decimais.
  Também acrescenta o objeto no {cache} na memória.
  
  Em caso de sucesso, retorna o objeto criado.  Caso contrário, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro."""
  return objeto_IMP.cria(atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def muda_atributos(obj, mods, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  """Modifica alguns atributos do objeto {obj} da classe {Objeto},
  registrando as alterações na tabela especificada da base de dados.

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do objeto (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {mods}.
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  objeto_IMP.muda_atributos(obj, mods, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def obtem_identificador(obj):
  """Devolve o identificador '{L}-{NNNNNNNN}' do objeto."""
  return objeto_IMP.obtem_identificador(obj)

def obtem_atributos(obj):
  """Retorna um dicionário Python que é uma cópia dos atributos do objeto,
  exceto identificador."""
  return objeto_IMP.obtem_atributos(obj)

def obtem_atributo(obj, chave):
  """Retorna o valor do atributo de {obj} com a chave {chave}.
  Não serve para obter o identificador."""
  return objeto_IMP.obtem_atributo(obj, chave)

def busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  """Localiza um objeto com identificador {id} (uma string da forma
  "{X}-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {Objeto}.
  Se tal objeto não existe, devolve {None}."""
  return objeto_IMP.busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def busca_por_campo_unico(chave, val, cache, nome_tb, letra_tb, colunas):
  """Procura objeto cujo atributo {chave}
  tem valor {val}, supondo que ele é único. Se
  encontrar, devolve o identificador desse objeto (NÃO o objeto),
  senão devolve {None}"""
  
# FUNÇÕES PARA DEPURAÇÃO

def verifica(obj, tipo, id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  """Faz testes de consistência básicos de um objeto {obj} de classe {tipo}, 
  que deve ser uma sublcasse de {Objeto}, dados o identificador esperado 
  {id}, e os atributos esperados {atrs}.
  
  Especificamente, verifica as funções {obtem_identificador(obj)},
  {obtem_atributos(obj)} e {busca_por_identificador(id)}
  do {modulo} dado.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return objeto_IMP.verifica(obj, tipo, id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  objeto_IMP.diagnosticos(val)
