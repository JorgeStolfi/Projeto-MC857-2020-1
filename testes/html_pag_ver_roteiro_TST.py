#! /usr/bin/python3

assert False # !!! IMPLEMENTAR !!!

### # Interfaces usadas por este script:
### 
### import html_roteiro
### import base_sql
### import tabelas
### import roteiro
### import utils_testes
### import sessao
### 
### import sys
### 
### sys.stderr.write("Conectando com base de dados...\n")
### res = base_sql.conecta("DB",None,None)
### assert res == None
### 
### sys.stderr.write("Criando alguns objetos...\n")
### tabelas.cria_todos_os_testes()
### 
### def testa(rotulo, *args):
###   """Testa {funcao(*args)}, grava resultado 
###   em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
###   
###   modulo = html_roteiro
###   funcao = modulo.gera
###   frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
###   pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
###   utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)
### 
### rots = roteiro.descobre_todos("VCP", "MAO", "2020-05-07", "2020-05-10")
### rot = rots[0]
### 
### testa("NF", None, rot, False) # Sem login, sem detalhes.
### testa("NT", None, rot, True) # Sem login, com detalhes.
### 
### ses1 = sessao.busca_por_identificador("S-00000001")
### 
### testa("LF", ses1, rot, False) # Com login, sem detalhes.
### testa("LT", ses1, rot, True) # Com login, com detalhes.
### 
