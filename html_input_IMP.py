
import html_label
from utils_testes import erro_prog

def gera(rotulo, tipo, nome, val_ini, editavel, dica, cmd):
  ht_rotulo = html_label.gera(rotulo, ": ")
  ht_tipo = " type =\"" + tipo + "\""
  ht_nome = " name=\"" + nome + "\" id=\"" + nome + "\""
  if tipo == "number": ht_nome += " min=\"1\""
    
  if val_ini != None and dica != None:
    erro_prog("{val_ini} e {dica} são mutuamente exclusivos")
  if val_ini == None and not editavel:
    erro_prog("{val_ini} não pode ser {None} se o campo não é editável")
  
  ht_val_ini = ( " value =\"" + val_ini + "\"" if val_ini != None else "" )
  if val_ini == 'on' and tipo == 'checkbox':
    ht_val_ini += ' checked '
  ht_readonly = ( " readonly" if not editavel else "" )
  ht_dica = ( " placeholder=\"" + dica + "\"" if dica != None else "" )
  ht_cmd = ( " onchange=\"window.location.href=" + cmd + "\"" if cmd != None else "" )
  html = ht_rotulo + "<input" + ht_tipo + ht_nome + ht_val_ini + ht_readonly + ht_dica + "/>"
  return html
