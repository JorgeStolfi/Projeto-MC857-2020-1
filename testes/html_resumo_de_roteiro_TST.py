import html_resumo_de_roteiro
import utils_testes

def testa(rotulo, *args):
  """ Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = html_resumo_de_roteiro
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidade (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


# Testa a geração de um fragmento html correspondente ao resumo de roteiro
roteiro = None # Usando {None} pois objeto roteiro ainda não foi definido, como consta em roteiro_IMP.py
testa('resumo_roteiro', roteiro)
