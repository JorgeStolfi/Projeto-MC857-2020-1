import html_textarea
import utils_testes

def testa(rotulo, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = html_textarea
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, modulo.gera, rotulo, frag, pretty, *args)
   
for vin in ( False, True ):
  for edt in  ( False, True ):
    for obr in ( False, True ):
      for dic in ( False, True ):
        if (not (vin and dic)) and (edt or not (obr or dic)):
          vini = "Lorem ipsum" if vin else None
          dica = "Máximo 50 kg" if dic else None
          rot = "test"
          rot += "-vin" + str(vin)[0]
          rot += "-edt" + str(edt)[0]
          rot += "-obr" + str(obr)[0]
          rot += "-dic" + str(dic)[0]
          testa(rot, "Peso", 'peso', vini, edt, obr, dica, "vade_retro")
