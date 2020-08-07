import html_label
import html_input
import html_table
import html_label
import html_textarea
from utils_testes import erro_prog
import sys

def gera(dados_linhas, atrs):
  # sys.stderr.write("{html_form_table_IMP.gera}: atrs = %s\n" %str(atrs))

  # Converte os dados brutos das linhas para fragmentos HTML:
  ht_linhas_vis = [].copy() # Lista de pares {(ht_rotulo,ht_input)} dos campos visíveis.
  ht_campos_hid = [].copy()  # Lista de {ht_input}s dos campos invisívels.
  for rotulo, tipo, chave, dica, visivel, editavel, obrigatorio in dados_linhas:
    val = (atrs[chave] if chave in atrs else None)
    if visivel:
      # Pega o valor mínimo, se houver:
      chmin = chave + "_min"
      vmin = atrs[chmin] if (tipo == "number") and (chmin in atrs) else None
      # Gera o <input>:
      ht_rotulo = html_label.gera(rotulo, None);
      ht_input = gera_input(tipo, chave, val, vmin, dica, editavel, obrigatorio)
      ht_linhas_vis.append((ht_rotulo, ht_input,))
    else:
      ht_input = gera_input("hidden", chave, val, None, None, False, False)
      ht_campos_hid.append(ht_input)

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_table.gera(ht_linhas_vis, None)
  ht_res = ht_table + ("\n".join(ht_campos_hid))
  return ht_res

def gera_input(tipo, chave, val, vmin, dica, editavel, obrigatorio):
  """Retorna o HTML de um elemento <input> ou <textarea>...</textarea>.

  O elemento terá o dado {tipo} ("text", "password", etc.), nome {chave},
  valor inicial {val}, valor mínimo {vmin}, e a {dica} especificada 
  (se {val} for {None}).  Se {tipo} for "textarea", gera um
  <textarea> em vez de <input>.
  
  O valor inicial {val} é convertido para string de maneira adequada ao
  seu tipo python. Em particular, valor {float} é formatado com 2 casas
  depois do ponto decimal.

  Se a chave for 'senha', não mostra o {val}.  Se {tipo}
  não for "number", ignora {vmin}. """

  if chave == 'senha': val = None
  if chave == 'conf_senha': val = None

  # Converte val para HTML:
  if val == None:
    ht_valor = None
  elif type(val) is str:
    ht_valor = val
  elif type(val) is bool:
    ht_valor = ('on' if val else 'off')
  elif type(val) is float:
    ht_valor = ("%.2f" % val)
  elif type(val) is int:
    ht_valor = ("%d" % val)
  else:
    erro_prog("valor inválido = \"" + str(val) + "\"")
  
  # Converte o valor mínimo para HTML:
  if tipo == 'number': 
    ht_vmin = str(vmin)
  else:
    ht_vmin = None

  # Dica e valor inicial são mutuamente exclusivos:
  if ht_valor == None:
    ht_dica = dica
  else:
    ht_dica = None

  # Cozinhada: tipo "textarea" é um elemento diferente.
  if tipo != "textarea":
    ht_campo = html_input.gera(None, tipo, chave, ht_valor, ht_vmin, editavel, obrigatorio, ht_dica, None)
  else:
    ht_campo = html_textarea.gera(None, chave, ht_valor, editavel, obrigatorio, ht_dica, None)
  
  return ht_campo
