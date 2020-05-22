#! /usr/bin/python3

import os,sys,inspect
import base_sql 
import tabela_generica
import tabelas
import compra
import usuario
import identificador
import utils_testes
from utils_testes import erro_prog, mostra


# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {usuario}, limpando tabela, criando usuários para teste:\n")
usuario.cria_testes()

sys.stderr.write("Inicializando módulo {compra}, limpando tabela, criando compras para teste:\n")
compra.cria_testes()

sys.stderr.write("Inicializando módulo {compra}, limpando tabela:\n")
compra.inicializa(True)

# ----------------------------------------------------------------------
sys.stderr.write("Obtendo dois usuários para teste:\n")

usr1 = usuario.busca_por_identificador("U-00000001")
usr2 = usuario.busca_por_identificador("U-00000002")

cmp1 = compra.busca_por_identificador("C-00000001")
cmp2 = compra.busca_por_identificador("C-00000003")

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_compra(rotulo, cpr, ident, cliente, status):
  """Testes básicos de consistência do objeto {cpr} da classe {Objeto_Compra}, dados
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando compra %s\n" % rotulo)
  atrs = { 'cliente': cliente, 'status': status }
  ok = compra.verifica(cpr, ident, atrs)
  
  if cpr != None and type(cpr) is compra.Objeto_Compra:
    
    sys.stderr.write("testando {obtem_cliente()}:\n")
    usr1 = compra.obtem_cliente(cpr)
    if usr1 != cliente:
      aviso_prog("retornou " + str(usr1) + ", deveria ter retornado " + str(cliente),True)
      ok = False

    sys.stderr.write("testando {obtem_status()}:\n")
    status1 = compra.obtem_status(cpr)
    if status1 != status:
      aviso_prog("retornou " + str(status1) + ", deveria ter retornado " + str(status),True)
      ok = False
    
    # erro na implementação de poltrona
    # sys.stderr.write("testando {obtem_itens()}:\n")
    # itens1 = compra.obtem_itens(cpr)
    # if itens1 != usr:
    #   aviso_prog("retornou " + str(itens1) + ", deveria ter retornado " + str(usr),True)
    #   ok = False
      
  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("%s\n" % ("-" * 70))
  return

# ----------------------------------------------------------------------
sys.stderr.write("testando {compra.cria}:\n")
compra1 = compra.cria(usr1)
compraIndice1 = 1
compraId1 = "C-00000001"
verifica_compra("c1", compra1, compraId1, usr1, 'aberto')

compra2 = compra.cria(usr2)
compraIndice2 = 2
compraId2 = "C-00000002"
verifica_compra("c2", compra2, compraId2, usr2, 'aberto')

compra3 = compra.cria(usr1)
compraIndice3 = 3
compraId3 = "C-00000003"
verifica_compra("c3", compra3, compraId3, usr1, 'aberto')

sys.stderr.write("testando {compra.fecha}:\n")
compra.fecha(compra1)
verifica_compra("fecha_c1", compra1, compraId1, usr1, 'pagando')

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
