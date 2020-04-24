# Implementação do módulo {tabelas}.

import sys

# Os principais objetos:
import usuario
import compra
import sessao
from utils_testes import erro_prog, mostra

def inicializa_todas(limpa):
  usuario.inicializa(limpa)
  compra.inicializa(limpa)
  sessao.inicializa(limpa)
  
def id_para_objeto(id):
  letra = id[0];
  if letra == "U":
    obj = usuario.busca_por_identificador(id)
  elif letra == "C":
    obj = compra.busca_por_identificador(id)
  elif letra == "S":
    obj = sessao.busca_por_identificador(id)
  else:
    erro_prog("identificador '" + id + " inválido")
  return obj

def cria_todos_os_testes():
  # A ordem é importante:
  usuario.cria_testes() # Não tem atributos de tipo objeto.
  compra.cria_testes()  # Tem atributos de tipo {ObjUsuario}.
  sessao.cria_testes()  # Tem atributos de tipo {ObjUsuario}.
  


