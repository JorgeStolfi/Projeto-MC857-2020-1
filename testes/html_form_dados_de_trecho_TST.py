#! /usr/bin/python3
 

import base_sql
import html_form_dados_de_trecho
import tabelas
import trecho
import utils_testes
from utils_testes import erro_prog, aviso_prog
import sys

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# ----------------------------------------------------------------------
sys.stderr.write("Testando função...\n")
def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_dados_de_trecho
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

trc0_id = "T-00000001"
trc0 = trecho.busca_por_identificador(trc0_id)
trc0_atrs = None
testa("vazio", trc0_id, trc0_atrs, "Cozinhar", "cozinhar_trecho")

trc1_id = "T-00000001"
trc1 = trecho.busca_por_identificador(trc1_id)
trc1_atrs = {"codigo": "AZ 3331"}
testa("um_campo", trc1_id, trc1_atrs, "Pensar", "pensar_sobre_trecho")
  
trc2_id = "T-00000002"
trc2 = trecho.busca_por_identificador(trc2_id)
trc2_atrs = trecho.obtem_atributos(trc2)
testa("atuais", trc2_id, trc2_atrs, "Desintegrar", "desintegrar_trecho")

trc3_id = "T-00000003"
trc3 = trecho.busca_por_identificador(trc3_id)
trc3_atrs = {
  "codigo":"GO 333",
  "origem":"111",
  "destino":"222",
  "dia_partida":"2020-05-29",
  "hora_partida":"15:30",
  "dia_chegada":"2020-05-29",
  "hora_chegada":"16:00",
  "poltronas":"1A-20D",
}
testa("muda_todos", trc3_id, trc3_atrs, "Cavocar", "cavocar_trecho")

trc4_id = "T-00000004"
trc4 = trecho.busca_por_identificador(trc4_id)
trc4_atrs = {
  "codigo":"abcdef",
  "origem":"abcdef",
  "destino":"abcdef",
  "dia_partida":"abcdef",
  "hora_partida":"abcdef",
  "dia_chegada":"abcdef",
  "hora_chegada":"abcdef",
  "poltronas":"abcdef",
}
testa("invalidos", trc4_id, trc4_atrs, "SURFAR", "surfar_trecho")
