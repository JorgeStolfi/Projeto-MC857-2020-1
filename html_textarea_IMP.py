
import html_label
from utils_testes import erro_prog

def gera(rotulo, nome, val_ini, editavel, obrigatorio, dica, cmd):
  ht_rotulo = html_label.gera(rotulo, ": ")
  ht_linhas = " rows=\"" + "10" + "\""
  ht_colunas = " cols=\"" + "60" + "\""
  ht_tamanho = " maxlength=\"" + "6000" + "\""
  ht_nome = " name=\"" + nome + "\""
  ht_id = " id=\"" + nome + "\""

  if val_ini != None and dica != None:
    erro_prog("{val_ini} e {dica} são mutuamente exclusivos")

  ht_obrigatorio = ( " required" if obrigatorio else "" )
  if not editavel:
    ht_readonly = " readonly"
    ht_estilo =  "style=\"background-color:#bcbcbc;\""
  else:
    ht_readonly = ""
    ht_estilo = " style=\"background-color:#ffffff\""

  ht_dica = ( " placeholder=\"" + dica + "\"" if dica != None else "" )
  ht_cmd = ( " onchange=\"window.location.href=" + cmd + "\"" if cmd != None else "" )
  ht_textarea = ht_rotulo + \
    "<textarea" + \
      ht_linhas + \
      ht_colunas + \
      ht_tamanho + \
      ht_nome + \
      ht_id + \
      ht_readonly + \
      ht_dica + \
      ht_cmd + \
      ht_obrigatorio + \
      ht_estilo + \
    ">" + (val_ini if val_ini != None else "") + "</textarea>"
  return ht_textarea
