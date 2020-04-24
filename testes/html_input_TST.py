#! /usr/bin/python3

import html_input; from html_input import gera
import utils_testes; from utils_testes import testa_gera_html as testa

def testa_inp(rot_arq, rotulo, tipo, nome, val_ini, editavel, dica):
  """ Testa {html_input.gera}.  O parâmetro {rot_arq} é 
  usado para formar o nome do arquivo de saída.  Os demais
  parâmetros são passados a {html_input.gera}."""
  testa(html_input, gera, rot_arq, True, False, rotulo, tipo, nome, val_ini, editavel, dica, "def_valor")
   
testa_inp("text_dica",   "Peso", "text", "peso", None,    True,  "Máximo 50 kg")
testa_inp("text_vini",   "Peso", "text", "peso", "30 kg", True,  None)
testa_inp("text_rdonly", "Peso", "text", "peso", "30 kg", False, None)

testa_inp("num_dica",   "Peso (kg)", "number", "peso", None, True, "Máximo 50")
testa_inp("num_vini",   "Peso (kg)", "number", "peso", "30", True, None)
testa_inp("num_rdonly", "Peso (kg)", "number", "peso", "30", False,None)

testa_inp("email_dica",  "Email", "email", "email", None,               True, "{user}@{host}")
testa_inp("email_vini",  "Email", "email", "email", "jose@tatu.gov.br", True, None)

testa_inp("senha_dica",  "Senha", "password", "senha", None, True, "Máximo 2 letras")
testa_inp("senha_vini",  "Senha", "password", "senha", "99", True, None)

testa_inp("hidden_vini",  None, "hidden", "user", "U-12345678", False, None)
