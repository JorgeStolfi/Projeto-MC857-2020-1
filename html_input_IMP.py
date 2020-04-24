
import html_label
from utils_testes import erro_prog

def gera(rotulo, tipo, nome, val_ini, editavel, dica, cmd):
  html_rotulo = html_label.gera(rotulo, ": ")
  html_tipo = " type =\"" + tipo + "\""
  html_nome = " name=\"" + nome + "\" id=\"" + nome + "\""
  if tipo == "number": html_nome += " min=\"1\""
    
  if val_ini != None and dica != None:
    erro_prog("{val_ini} e {dica} são mutuamente exclusivos")
  if val_ini == None and not editavel:
    erro_prog("{val_ini} não pode ser {None} se o campo não é editável")
  
  html_val_ini = ( " value =\"" + val_ini + "\"" if val_ini != None else "" )
  if val_ini == 'on' and tipo == 'checkbox':
    html_val_ini += ' checked '
  html_readonly = ( " readonly" if not editavel else "" )
  html_dica = ( " placeholder=\"" + dica + "\"" if dica != None else "" )
  html_cmd = ( " onchange=\"window.location.href=" + cmd + "\"" if cmd != None else "" )
  html = html_rotulo + "<input" + html_tipo + html_nome + html_val_ini + html_readonly + html_dica + "/>"
  return html
