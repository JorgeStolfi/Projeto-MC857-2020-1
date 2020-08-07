import utils_testes

import base_sql
import tabelas
import sessao
import poltrona
import comando_executa_checkin

# Conecta no banco e carrega alimenta com as informações para o teste
utils_testes.mostra(0, "Conectando com base de dados...")
res = base_sql.conecta("DB", None, None)
assert res is None

utils_testes.mostra(0, "Conectando com base de dados...")
tabelas.cria_todos_os_testes(False)

# Sessao de teste (administrador)
ses = sessao.busca_por_identificador("S-00000004")

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = comando_executa_checkin
  funcao = modulo.processa
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Poltrona que já está reservada
id_poltrona = "A-00000006"
pol = poltrona.busca_por_identificador(id_poltrona)
assert pol is not None, "Poltrona A-00000006 não encontrada no banco"

testa("check-in", ses, { 'id_poltrona': id_poltrona })