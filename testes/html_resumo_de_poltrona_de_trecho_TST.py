import html_resumo_de_poltrona_de_trecho
import base_sql
import poltrona
import tabelas
import utils_testes
import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

modulo = html_resumo_de_poltrona_de_trecho
frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).

def testa_gera(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  funcao = modulo.gera
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

def testa_gera_cabecalho(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  funcao = modulo.gera_cabecalho
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)
 
def testa_gera_legenda(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  funcao = modulo.gera_legenda
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)
 
# A-00000001: ocupada, oferta, fez checkin.
# A-00000002: livre, oferta.
# A-00000003: ocupada, normal, não fez checkin.
# A-00000004: livre, normal.

testes = ( \
  ( False, False,  False,  False, ), 
  ( True,  False,  False,  False, ),
  ( True,  False,  False,  True,  ),
  ( False, True,   False,  False, ),
  ( False, False,  True,   False, ),
)

for id_pol in ( "A-00000001", "A-00000002",  "A-00000003", "A-00000004"):
  for alterar, comprar, excluir, fazer_checkin in testes:
    embarcar = fazer_checkin
    rot = id_pol;
    pol = poltrona.busca_por_identificador(id_pol);
    assert pol != None
    rot += "-alter" + str(alterar)[0];
    rot += "-compr" + str(comprar)[0];
    rot += "-exclu" + str(excluir)[0];
    rot += "-fzchk" + str(fazer_checkin)[0];
    testa_gera_cabecalho(rot, fazer_checkin)
    testa_gera(rot, pol, alterar, comprar, excluir, fazer_checkin, embarcar)
    testa_gera_legenda(rot, fazer_checkin)
    
