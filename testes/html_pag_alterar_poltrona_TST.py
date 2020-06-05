#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import html_pag_alterar_poltrona
import usuario
import identificador
import base_sql
import tabelas
import poltrona
import sessao
import compra
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes das funções de {html_form}:

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
   
  modulo = html_pag_alterar_poltrona
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Dados para teste:
ses1 = sessao.busca_por_identificador("S-00000001")
usr1 = usuario.busca_por_identificador("U-00000001")
assert usr1 != None

pol1_id = "A-00000001"
pol1 = poltrona.busca_por_identificador(pol1_id)
pol1_atrs = poltrona.obtem_atributos(pol1)

# Teste com atributos originais:
testa("O-E0", ses1, pol1_id, pol1_atrs, None)
testa("O-E1", ses1, pol1_id, pol1_atrs, "Não gostei")

# Teste com atributos alterados:
pol1_atrs_m = pol1_atrs.copy();
pol1_atrs_m['preco'] = 999.99
pol1_atrs_m['oferta'] = not pol1_atrs['oferta']

testa("M-E1", ses1, pol1_id, pol1_atrs_m, "Das schibunga is kaput")
