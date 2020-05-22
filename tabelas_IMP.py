# Implementação do módulo {tabelas}.

import sys

# Os principais objetos:
import poltrona
import usuario
import trecho
import sessao
import compra
from utils_testes import erro_prog, mostra

def inicializa_todas(limpa):
  poltrona.inicializa(limpa)
  usuario.inicializa(limpa)
  compra.inicializa(limpa)
  sessao.inicializa(limpa)
  trecho.inicializa(limpa)
  
def id_para_objeto(id):
  letra = id[0];
  if letra == "U":
    obj = usuario.busca_por_identificador(id)
  elif letra == "C":
    obj = compra.busca_por_identificador(id)
  elif letra == "S":
    obj = sessao.busca_por_identificador(id)
  elif letra == "A":
    obj = poltrona.busca_por_identificador(id)
  elif letra == "T":
    obj = trecho.busca_por_identificador(id)
  else:
    erro_prog("identificador '" + id + " inválido")
  return obj

def cria_todos_os_testes():
  # A ordem é importante:
  poltrona.cria_testes() # Não tem atributos de tipo objeto.
  usuario.cria_testes() # Não tem atributos de tipo objeto.
  trecho.cria_testes()  # Não tem atributos de tipo objeto.
  compra.cria_testes()  # Tem atributos de tipo {Objeto_Usuario}, {Objeto_Poltrona}.
  sessao.cria_testes()  # Tem atributos de tipo {Objeto_Usuario}, {Objeto_Compra}.
  


