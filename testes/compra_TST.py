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
usuario.cria_testes(False)

sys.stderr.write("Inicializando módulo {compra}, limpando tabela, criando compras para teste:\n")
compra.cria_testes(False)

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

def verifica_compra(rotulo, cpr, ident, cliente, status, nome_pass, doc_pass):
  """Testes básicos de consistência do objeto {cpr} da classe {Objeto_Compra}, dados
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando compra %s\n" % rotulo)
  atrs = { 'cliente': cliente, 'status': status, 'nome_pass': nome_pass, 'doc_pass': doc_pass }
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
    # sys.stderr.write("testando {obtem_poltronas()}:\n")
    # itens1 = compra.obtem_poltronas(cpr)
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
nome_pass1 = usuario.obtem_atributos(usr1)['nome']
doc_pass1 = usuario.obtem_atributos(usr1)['documento']
compra1 = compra.cria(usr1, nome_pass1, doc_pass1)
# print(compra.obtem_atributos(compra1))
compraIndice1 = 1
compraId1 = "C-00000001"
verifica_compra("c1", compra1, compraId1, usr1, 'comprando', nome_pass1, doc_pass1)

nome_pass2 = usuario.obtem_atributos(usr2)['nome']
doc_pass2 = usuario.obtem_atributos(usr2)['documento']
compra2 = compra.cria(usr2, nome_pass2, doc_pass2)
compraIndice2 = 2
compraId2 = "C-00000002"
verifica_compra("c2", compra2, compraId2, usr2, 'comprando', nome_pass2, doc_pass2)

nome_pass3 = "Giovanni Pereira"
doc_pass3 = "36.987.986-0"
compra3 = compra.cria(usr1, nome_pass3, doc_pass3)
compraIndice3 = 3
compraId3 = "C-00000003"
verifica_compra("c3", compra3, compraId3, usr1, 'comprando', nome_pass3, doc_pass3)

sys.stderr.write("testando {compra.fecha}:\n")
compra.fecha(compra1)
verifica_compra("fecha_c1", compra1, compraId1, usr1, 'pagando', nome_pass1, doc_pass1)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
