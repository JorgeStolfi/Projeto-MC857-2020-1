#! /usr/bin/python3

import html_input
import utils_testes

def testa(rotulo, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = html_input
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, modulo.gera, rotulo, frag, pretty, *args, "elucubrar")
   
testa("text_dica",   "Peso", "text", "peso", None,    True,  "Máximo 50 kg")
testa("text_vini",   "Peso", "text", "peso", "30 kg", True,  None)
testa("text_rdonly", "Peso", "text", "peso", "30 kg", False, None)

testa("num_dica",   "Peso (kg)", "number", "peso", None, True, "Máximo 50")
testa("num_vini",   "Peso (kg)", "number", "peso", "30", True, None)
testa("num_rdonly", "Peso (kg)", "number", "peso", "30", False,None)

testa("email_dica",  "Email", "email", "email", None,               True, "{user}@{host}")
testa("email_vini",  "Email", "email", "email", "jose@tatu.gov.br", True, None)

testa("senha_dica",  "Senha", "password", "senha", None, True, "Máximo 2 letras")
testa("senha_vini",  "Senha", "password", "senha", "99", True, None)

testa("hidden_vini",  None, "hidden", "user", "U-12345678", False, None)
