
import html_label
from utils_testes import erro_prog

def gera(rotulo, tipo, nome, val_ini, val_min, editavel, obrigatorio, dica, cmd):
  assert type(tipo) is str
  assert type(nome) is str
  assert val_ini == None or type(val_ini) is str
  assert val_min == None or type(val_min) is str
  assert type(editavel) is bool
  assert type(obrigatorio) is bool
    
  # Parâmetros ignorados para campos não visíveis ou não editáveis:
  if tipo == "hidden": 
    editavel = False
    rotulo = None
  if not editavel: 
    obrigatorio = False
    dica = None
    val_min = None
  
  ht_tipo = " type =\"" + tipo + "\""
  ht_nome = " name=\"" + nome + "\""
  
  # Inputs de tipo "radio" precisam de "id" diferenciado pelo valor:
  if (tipo == "radio") and (val_ini != None):
    ht_id = " id=\"" + nome + "." + val_ini + "\""
  else:
    ht_id = " id=\"" + nome + "\""
  ht_rotulo = html_label.gera(rotulo, ": ")

  if val_ini != None and dica != None:
    erro_prog("{val_ini} e {dica} são mutuamente exclusivos")

  ht_val_ini = ( " value =\"" + str(val_ini) + "\"" if val_ini != None else "" )
  if val_ini == 'on' and tipo == 'checkbox':
    ht_val_ini += ' checked '

  if tipo == "number" and val_min != None:
    ht_val_min = " min=\"" + val_min + "\""
  else:
    ht_val_min = ""

  ht_obrigatorio = ( " required" if obrigatorio else "" )
  if not editavel:
    ht_readonly = " readonly"
    if tipo == "checkbox":
      # Checkbox precisa de "disabled" também?  Não basta "readonly"?
      ht_readonly += " disabled"
    ht_estilo =  " style=\"border-style:none;background:none;\""
  else:
    ht_readonly = ""
    ht_estilo = " style=\"background-color:#ffffff\""
  ht_dica = ( " placeholder=\"" + dica + "\"" if dica != None else "" )
  ht_cmd = ( " onchange=\"window.location.href=" + cmd + "\"" if cmd != None else "" )
  ht_input = ht_rotulo + \
    "<input" + \
      ht_tipo + \
      ht_nome + \
      ht_id + \
      ht_val_ini + \
      ht_val_min + \
      ht_readonly + \
      ht_dica + \
      ht_cmd + \
      ht_obrigatorio + \
      ht_estilo + \
    "/>"
  return ht_input
