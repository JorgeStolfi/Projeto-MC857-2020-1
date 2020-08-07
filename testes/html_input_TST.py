#! /usr/bin/python3

import html_input
import utils_testes

def testa(rotulo, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = html_input
  funcao = html_input.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, modulo.gera, rotulo, frag, pretty, *args)
  
for typ in ("text", "number", "email", "password", "textarea", "date", "checkbox", "radio", ):
  tag_typ = typ
  for val in ("N", "V", "M", "D"): 
    tag_val = "val" + str(val)[0]

    vmin = None
    dica = None
    if typ == "text":
      nome = "peso"
      vini = "30 kg"
      dica = "NN.N kg"
    elif typ == "number":
      nome = "pernas"
      vini = "30"
      vmin = "3"
      dica = "NNN"
    elif typ == "email":
      nome = "endereco"
      vini = "primeiro@gmail.com"
      dica = "XXX@YYY.ZZZ"
    elif typ == "password":
      nome = "senha"
      vini = "123456789"
      dica = "uma senha segura"
    elif typ == "textarea":
      nome = "mensagem"
      vini = "Lorem ipsum est diviso in partes tres."
      dica = "Escreva sua mensagem aqui"
    elif typ == "date":
      nome = "dia_fatidico"
      vini = "2020-08-07"
      vmin = "2020-08-01"
      dica = "AAAA-MM-DD"
    elif typ == "checkbox":
      nome = "sublime"
      vini = "on"
    elif typ == "radio":
      nome = "flor"
      vini = "rosa"
    else:
      assert False

    if val == "N":
      vini = None; vmin = None; dica = None;
    elif val == "V":
      vmin = None; dica = None;
    elif val == "M":
      if vmin == None: continue
      dica = None
    elif val == "D":
      if dica == None: continue
      vini = None; vmin = None;
    else:
      assert False

    rotulo = nome.title()

    for edt in (False, True):
      tag_edt = "edt" + str(edt)[0]
      for obr in (False, True):
        tag_obr = "obr" + str(obr)[0]
        
        if obr and not edt: continue
        
        tag = tag_typ + "-" + tag_val + "-" + tag_edt + "-" + tag_obr
            
        testa(tag, rotulo, typ, nome, vini, vmin, edt, obr, dica, "carpe_diem")
