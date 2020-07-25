
import html_label
from utils_testes import erro_prog

def gera(rotulo, tipo, nome, val_ini, val_min, editavel, dica, cmd, obrigatorio):
  ht_rotulo = html_label.gera(rotulo, ": ")
  ht_linhas = " rows=\"" + "10" + "\""
  ht_maxCarac = " maxlength=\"" + "5000" + "\""
  ht_nome = " name=\"" + nome + "\""
  ht_id = " id=\"" + nome + ("." + val_ini if val_ini != None else "") + "\""

  if val_ini != None and dica != None:
    erro_prog("{val_ini} e {dica} são mutuamente exclusivos")
  if val_ini == None and not editavel:
    erro_prog("{val_ini} não pode ser {None} se o campo não é editável")

  ht_val_ini = ( " value =\"" + str(val_ini) + "\"" if val_ini != None else "" )

  ht_obrigatorio = (" required" if obrigatorio else "")
  ht_readonly = ( " readonly" if not editavel else "" )
  ht_readonlybackground = ( " style=\"background-color:#BCBCBC\"" if not editavel else "" )
  ht_dica = ( " placeholder=\"" + dica + "\"" if dica != None else "" )
  ht_cmd = ( " onchange=\"window.location.href=" + cmd + "\"" if cmd != None else "" )
  ht_estilo = ( " style=\"background-color:#c7c7c7\"" if not editavel else "" )
  ht_input_textarea = ht_rotulo + \
    "<textarea" + \
      ht_linhas + \
      ht_maxCarac + \
      ht_nome + \
      ht_val_ini + \
      ht_readonly + \
      ht_readonlybackground + \
      ht_dica + \
      ht_cmd + \
      ht_obrigatorio + \
      ht_estilo + \
    "></textarea>"
  return ht_input_textarea