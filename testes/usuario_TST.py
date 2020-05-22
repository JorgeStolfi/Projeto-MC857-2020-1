#! /usr/bin/python3
import usuario  
import tabela_generica
import base_sql
import identificador
import utils_testes
import sys
from utils_testes import erro_prog, aviso_prog, mostra

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {usuario}, limpando tabela:\n")
usuario.inicializa(True)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_usuario(rotulo, usr, ident, atrs):
  """Testes básicos de consistência do objeto {usr} da classe {Objeto_Usuario}, dados 
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando usuário %s\n" % rotulo)
  ok = usuario.verifica(usr, ident, atrs)

  if usr != None and type(usr) is usuario.Objeto_Usuario:   
    # ----------------------------------------------------------------------
    sys.stderr.write("testando {busca_por_email()}:\n")
    em1 = atrs['email']
    ident1 = usuario.busca_por_email(em1)
    if ident1 != ident:
      aviso_prog("retornou " + str(ident1) + ", deveria ter retornado " + str(ident),True)
      ok = False 

    # ----------------------------------------------------------------------
    sys.stderr.write("testando {busca_por_CPF()}:\n")
    CPF1 = atrs['CPF']
    ident1 = usuario.busca_por_CPF(CPF1)
    if ident1 != ident:
      aviso_prog("retornou " + str(ident1) + ", deveria ter retornado " + str(ident),True)
      ok = False 
  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("%s\n" % ("-" * 70))
  return
 
def testa_cria_usuario(rotulo, ident, atrs):
  """Testa criação de usuário com atributos com {atrs}. Retorna o usuário."""
  usr = usuario.cria(atrs)
  verifica_usuario(rotulo, usr, ident, atrs)
  return usr
 
# ----------------------------------------------------------------------
sys.stderr.write("testando {usuario.cria}:\n")
usr1_atrs = {
  'nome': "José Primeiro", 
  'senha': "123456789", 
  'email': "primeiro@gmail.com", 
  'CPF': "123.456.789-00", 
  'telefone': "+55(19)9 9876-5432",
  'documento': "1.234.567-9 SSP-SP",
  'administrador': False
}
uindice1 = 1
uident1 = "U-00000001"
usr1 = testa_cria_usuario("usr1", uident1, usr1_atrs)

usr2_atrs = {
  'nome': "João Segundo", 
  'senha': "987654321", 
  'email': "segundo@ic.unicamp.br", 
  'CPF': "987.654.321-99", 
  'telefone': "+55(19)9 9898-1212",
  'documento': 'CD98765-43 PF',
  'administrador': False
}
uindice2 = 2
uident2 = "U-00000002"
usr2 = testa_cria_usuario("usr2", uident2, usr2_atrs)

# Sem documento:
usr3_atrs = {
  'nome': "Juca Terceiro", 
  'senha': "4321002134", 
  'email': "muda@gmail.com", 
  'CPF': "111.111.111-11", \
  'telefone': "+55(19)9 9999-9999",
  'documento': None,
  'administrador': True
}
uindice3 = 3
uident3 = "U-00000003"
usr3 = testa_cria_usuario("usr3", uident3, usr3_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {usuario.muda_atributos}:\n")

usr1_mods = {
  'nome': "Josegrosso de Souza",
  'email': "grosso@hotmail.com"
}
usuario.muda_atributos(usr1, usr1_mods)
usr1_d_atrs = usr1_atrs
for k, v in usr1_mods.items():
  usr1_d_atrs[k] = v
verifica_usuario("usr1_d", usr1, uident1, usr1_d_atrs) 


if type(usr2) is usuario.Objeto_Usuario:
  usuario.muda_atributos(usr2, usr2_atrs) # Não deveria mudar os atributos
  verifica_usuario("usr2", usr2, uident2, usr2_atrs)

if type(usr2) is usuario.Objeto_Usuario:
  usr2_m_atrs = usr3_atrs.copy()
  usr2_m_atrs['CPF'] = usr2_atrs['CPF'] # Não pode alterar CPF.
  usr2_m_atrs['email'] = usr2_atrs['email'] # Vamos manter email.
  usuario.muda_atributos(usr2, usr2_m_atrs) # Deveria assumir os valores do usr3
  verifica_usuario("usr2_m", usr2, uident2, usr2_m_atrs)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
