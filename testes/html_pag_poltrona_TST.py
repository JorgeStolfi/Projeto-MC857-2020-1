#! /usr/bin/python3
 
import html_pag_poltrona
import base_sql
import tabelas
import poltrona
import compra
import usuario
import sessao
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
  
  modulo = html_pag_poltrona
  funcao = html_pag_poltrona.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# ----------------------------------------------------------------------
# Dados para testes:

# Um cliente comum:
usrC_id = "U-00000001"
usrC = usuario.busca_por_identificador(usrC_id)
assert not usuario.obtem_atributo(usrC, 'administrador')

# Um administrador:
usrA_id = "U-00000003"
usrA = usuario.busca_por_identificador(usrA_id)
assert usuario.obtem_atributo(usrA, 'administrador')

# Uma compra em aberto do cliente 1:
cprC_id = "C-00000001"
cprC = compra.busca_por_identificador(cprC_id)
assert compra.obtem_status(cprC) == 'comprando'
assert compra.obtem_cliente(cprC) == usrC

# Uma compra fechada:
cprF_id = "C-00000004"
cprF = compra.busca_por_identificador(cprF_id)
assert compra.obtem_status(cprF) != 'comprando'

# Sessão do cliente 1:
sesC = sessao.busca_por_identificador("S-00000001")
assert sessao.obtem_usuario(sesC) == usrC

# Sessão de outro cliente comum:
sesO = sessao.busca_por_identificador("S-00000003")
assert sessao.obtem_usuario(sesO) != None
assert sessao.obtem_usuario(sesO) != usrC

# Sessão de administrador:
sesA = sessao.busca_por_identificador("S-00000004")
assert sessao.eh_administrador(sesA)

# Poltrona reservada pelo usuario 1:
polR_id = "A-00000001"
polR = poltrona.busca_por_identificador(polR_id)
assert poltrona.obtem_atributo(polR, 'id_compra') == "C-00000001"

# Poltrona livre:
polL_id = "A-00000005"
polL = poltrona.busca_por_identificador(polL_id)
assert poltrona.obtem_atributo(polL, 'id_compra') == None

# Atributos a alterar:
atrs_m = {}.copy();

for ses_tag, ses in (("sesN", None), ("sesC", sesC), ("sesO", sesO), ("sesA", sesA)):
  for pol_tag, pol in (("polL", polL), ("polR", polR)):
    for err_tag, err in (("err0", None), ("err1", "Das schibunga is kaput")):
      atrs_pol = poltrona.obtem_atributos(pol)
      rot = "test-" + ses_tag + "-" + pol_tag + "-" + err_tag
      # Teste com atributos originais:
      testa(rot + "-O", ses, pol, atrs_pol, err)
      # Teste com atributos alterados:
      atrs_pol['preco'] = 999.99
      atrs_pol['oferta'] = not atrs_pol['oferta']
      testa(rot + "-M", ses, pol, atrs_pol, err)
