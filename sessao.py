# Este módulo define a classe de objetos {ObjSessao}, que
# representa uma sessão de 'login' de um cliente da loja virtual.
# 
# Nas funções abaixo, {usr} é um objeto da classe {ObjUsuario}
# que representa o cliente.

# Implementaçao deste módulo:
import sessao_IMP; from sessao_IMP import ObjSessao_IMP

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela "sessoes" na base de dados.
  Deve ser chamada apenas uma vez no ínicio da execução do servidor, 
  depois de chamar {base_sql.conecta}. Não retorna nenhum valor.  
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  sessao_IMP.inicializa(limpa)

class ObjSessao(ObjSessao_IMP):
  """Um objeto desta classe representa uma sessao de acesso ao
  servidor.  Os atributos deste objeto, por enquanto, são:
    
    'usr'      {ObjUsuario} o usuário que fez login na sessão.
    'abrt'     {bool}       estado da sessao.
    'cookie'   {str}        cookie da sessao.
    'carrinho' {ObjCompra}  o carrinho de compras associado à sessao.
    
  Outros atributos (data, IP, etc.) poderão ser acrescentados no futuro.
  
  Além desses atributos, cada sessão também tem um identificador de
  sessão, uma string da forma "S-{NNNNNNNN}" onde {NNNNNNNN} é o índice
  na tabela (vide abaixo) formatado em 8 algarismos.
  
  Cada sessao pertence a um unico usuário, mas cada usuário 
  pode ter várias sessoes abertas ao mesmo tempo. A sessao é criada
  e "aberta" quando o usuario faz login, e e "fechada" no logout.

  REPRESENTAÇÃO NA BASE DE DADOS

  Cada sessão do sistema -- aberta ou fechada -- é representada por uma
  linha na tabela "sessoes" da base SQL em disco. Apenas algumas dessas
  linhas são representadas também na memória por objetos da classe
  {ObjSessao}.
  
  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos da sessão
  (menos o identificador)."""
  pass
 
def cria(usr, cookie, carrinho):
  """Cria um novo objeto da classe {ObjSessao}, associada ao usuário {usr},
  inicialmente aberta, com o cookie inicial {cookie} e carrinho de compras {carrinho}.
  Também acrescenta a sessão à base de dados.  Em caso de sucesso, retorna o objeto.
  Atribui um identificador único à sessão, derivado do seu índice na tabela.
  Retorna o objeto criado."""
  return sessao_IMP.cria(usr, cookie, carrinho)

def obtem_identificador(ses):
  """Devolve o identificador 'S-{NNNNNNNN}' da sessão {ses}."""
  return sessao_IMP.obtem_identificador(ses)

def obtem_atributos(ses):
  """Retorna um dicionário Python que é uma cópia dos atributos da sessão {ses},
  exceto identificador."""
  return sessao_IMP.obtem_atributos(ses)

def obtem_usuario(ses):
  """Retorna o objeto da classe {ObjUsuario} correspondente ao usuario que
  fez login na sessao {ses}.  Equivale a {sessao.obtem_atributos(ses)['usr']}. """
  return sessao_IMP.obtem_usuario(ses)

def aberta(ses):
  """Retorna o estado da sessão {ses}: {True} se a sessao ainda esta aberta, 
  {False} se o usuário deu logout.  Equivale a {sessao.obtem_atributos(ses)['abrt']}."""
  return sessao_IMP.aberta(ses)

def obtem_cookie(ses):
  """Devolve o cookie da sessão {ses} """
  return sessao_IMP.obtem_cookie(ses)

def obtem_carrinho(ses):
  return sessao_IMP.obtem_carrinho(ses)

def busca_por_identificador(id):
  """Localiza uma sessao com identificador {id} (uma string da forma
  "S-{NNNNNNNN}"), e devolve a mesma na forma de um objeto da classe {ObjSessao}.
  Se tal sessão não existe, devolve {None}."""
  return sessao_IMP.busca_por_identificador(id)

def muda_atributos(ses, mods_mem):
  """Recebe um dicionário Python {mods_mem} cujas chaves são um subconjunto
  dos nomes de atributos da sessão (exceto o identificador). Troca os 
  valores desses atributos no objeto {ses} da classe {ObjSessao}
  pelos valores correspondentes em {mods_mem}.  Também altera esses 
  campos na base de dados. Os valores devem estar no formato de
  atributos na memória."""
  sessao_IMP.muda_atributos(ses, mods_mem)

def fecha(ses):
  """Registra o logout do usuário na sessão {ses}, mudando o atributo 'abrt'
  permanentemente para {False}. Também altera esse campo na base de dados.
  A sessão não pode ser {None} e deve estar aberta.  Não retorna nenum resultado."""
  sessao_IMP.fecha(ses)

# DEPURAÇÂO

def cria_testes():
  """Limpa a tabela de sessoes com {inicializa(True)}, e cria três sessões
  para fins de teste, incluindo-as na tabela.  As sessões estarão
  inicialmente abertas.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {base_sql.conecta}.Supõe que a tabela de usuários 
  já foi inicializada e tem pelo menos três entradas.""" 
  sessao_IMP.cria_testes()

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  sessao_IMP.diagnosticos(val)
