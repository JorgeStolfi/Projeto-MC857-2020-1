#! /usr/bin/python3

import html_pag_cadastrar_usuario
import tabelas
import usuario
import sessao
import base_sql
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessao de teste:
ses = sessao.busca_por_identificador("S-00000001")
assert ses != None

# Atributos de usuario para teste:
atrs1 = {
  'nome': "José Primeiro", 
  'senha': "123456789", 
  'email': "primeiro@gmail.com", 
  'CPF': "123.456.789-00", 
  'telefone': "+55(19)9 9876-5432",
  'documento': "1.234.567-9 SSP-SP",
  'administrador': False
}

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_pag_cadastrar_usuario
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for tag, atrs, erros in ( 
    ("NN", None,  None), 
    ("NA", atrs1, None), 
    ("VN", None,  []), 
    ("VA", atrs1, []), 
    ("EN", None,  ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
    ("EA", atrs1, ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",]),
  ):
  rotulo = tag
  testa(rotulo, ses, atrs, erros)
