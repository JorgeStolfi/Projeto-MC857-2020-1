#! /usr/bin/env python3

import html_pag_trecho
import tabelas
import usuario
import sessao
import trecho
import base_sql
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_trecho
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# ----------------------------------------------------------------------
# Sessao de teste de usuário comum:
ses_com = sessao.busca_por_identificador("S-00000001")
assert ses_com != None
assert not sessao.eh_administrador(ses_com)

# Usuario comum de teste:
usr_com = sessao.obtem_usuario(ses_com)
assert usr_com != None
usr_com_id = usuario.obtem_identificador(usr_com)
usr_com_atrs = usuario.obtem_atributos(usr_com)

# Sessao de teste de administrador:
ses_adm = sessao.busca_por_identificador("S-00000004")
assert ses_adm != None
assert sessao.eh_administrador(ses_adm)

# Usuario administrador de teste:
usr_adm = sessao.obtem_usuario(ses_adm)
assert usr_adm != None
usr_adm_id = usuario.obtem_identificador(usr_adm)
usr_adm_atrs = usuario.obtem_atributos(usr_adm)

# Trechos de teste (somente id):
trc1_id = "T-00000001" # Não encerrado.
trc1 = trecho.busca_por_identificador(trc1_id)
assert not trecho.obtem_atributo(trc1, 'encerrado')

trc6_id = "T-00000006" # Encerrado.
trc6 = trecho.busca_por_identificador(trc6_id)
assert trecho.obtem_atributo(trc6, 'encerrado')

# ----------------------------------------------------------------------
# Atributos para criação de novo trecho:
atrs_nov = {
  'codigo': 'AZ 3344',
  'origem': 'GRU',
  'destino': 'RAO',
  'dia_partida': '2020-05-02',
  'dia_chegada': '2020-05-02'
}

# Atributos para alteração de trecho:
atrs_alt = {
  'dia_partida': '2020-09-02',
  'dia_chegada': '2020-09-02',
  'hora_chegada': '19:45',
  'encerrado': True,
}

# ----------------------------------------------------------------------

# Testes com erros em vérios formatos:
for trc_tag, id_trc in (("trcN", None), ("trc1", trc1_id), ("trc6", trc6_id)):
  trc = None if id_trc == None else trecho.busca_por_identificador(id_trc)
  for ses_tag, ses in (("sesN", None), ("sesC", ses_com), ("sesA", ses_adm)):
    logado = ses != None
    admin = False if ses == None else sessao.eh_administrador(ses)
    for err_tag, erros in (
      ("err0", None), 
      ("err1", "Não entendi"), 
    ):
      if admin or (trc != None):
        rot = trc_tag + "-" + ses_tag + "-" + err_tag
        sys.stderr.write("--- %s ------------------------\n" % rot)
        atrs = atrs_alt if trc != None else atrs_nov
        testa(rot, ses, trc, atrs, erros)
