# Implementação do módulo {comando_solicitar_pag_acrescentar_trecho}.

import html_pag_acrescentar_trecho
import sys

def processa(ses, args):
  # !!! Deveria verificar se a sessão {ses} está aberta e o dono é administrador !!!
  pag = html_pag_acrescentar_trecho.gera(ses, args, None)
  return pag

def verifica_usuario(usr):
  sys.stderr.write("\n%s\n" % usr)
  assert ses["administrador"]
  return
