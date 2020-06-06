#! /usr/bin/python3
 
import html_pag_ver_poltrona
import base_sql
import tabelas
import poltrona
import sessao
import utils_testes
import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_pag_ver_poltrona
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

pol1_id = "A-00000001"

ses = sessao.busca_por_identificador("S-00000001")
pol = poltrona.busca_por_identificador(pol1_id)

testa("xF-e0", ses, pol, None, False, None)
testa("xF-e1", ses, pol, None, False, "É o fim da picada")
testa("xF-e2", ses, pol, None, False, ["Não tem café", "Cadê meu grampeador?"])

testa("xT-e0", ses, pol, 'C-00000001', True, [])

