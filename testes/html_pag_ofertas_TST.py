#! /usr/bin/python3
 
import utils_testes
import html_pag_ofertas
import tabelas
import usuario
import sessao
import trecho
import base_sql
import utils_testes
import objeto

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

#sessao de teste
ses = sessao.busca_por_identificador("S-00000001")

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_pag_ofertas
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidade (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


#teste no caso de pagina de ofertas buscar por trechos
trc1_id = "T-00000001"
trc2_id = "T-00000002"
trc3_id = "T-00000003"

trecho1 = trecho.busca_por_identificador(trc1_id)
trecho2 = trecho.busca_por_identificador(trc2_id)
trecho3 = trecho.busca_por_identificador(trc3_id)

trechos = [trecho1, trecho2, trecho3]

testa("E0", ses, trechos, None)
testa("E1", ses, trechos, "Tsk, tsk!")


