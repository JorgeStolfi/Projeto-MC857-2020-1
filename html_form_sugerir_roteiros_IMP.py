import html_label
import html_input
import html_table
import html_botao_submit
import html_form


def gera():
  linhas = [].copy()

  ht_rotulo = html_label.gera("Origem", ": ")
  ht_campo = html_input.gera(None, "text", "origem", None, None, True, True, "VCP", None)
  linhas.append((ht_rotulo, ht_campo,))

  ht_rotulo = html_label.gera("Data mínima de partida", ": ")
  ht_campo = html_input.gera(None, "text", "dia_min", None, None, True, True, "aaaa-mm-dd", None)
  ht_campo2 = html_input.gera(None, "text", "hora_min", None, None, True, True, "HH:MM", None)
  ht_rotulo2 = html_label.gera("UTC", "")
  linhas.append((ht_rotulo, ht_campo, ht_campo2, ht_rotulo2))

  ht_rotulo = html_label.gera("Destino", ": ")
  ht_campo = html_input.gera(None, "text", "destino", None, None, True, True, "SDU", None)
  linhas.append((ht_rotulo, ht_campo,))

  ht_rotulo = html_label.gera("Data máxima de chegada", ": ")
  ht_campo = html_input.gera(None, "text", "dia_max", None, None, True, True, "aaaa-mm-dd", None) 
  ht_campo2 = html_input.gera(None, "text", "hora_max", None, None, True, True, "HH:MM", None)
  ht_rotulo2 = html_label.gera("UTC", "")
  linhas.append((ht_rotulo, ht_campo, ht_campo2, ht_rotulo2))

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_table.gera(linhas, None)

  ht_bt_buscar = html_botao_submit.gera("Buscar", 'sugerir_roteiros', None, '#55ee55')

  ht_campos = \
    ht_table + \
    ht_bt_buscar

  ht = html_form.gera(ht_campos)
  return ht
