import usuario
import html_bloco_usuario
import html_div

def gera(ids):
  res = ""
  for id_usuario in ids:
    usr = usuario.busca_por_identificador(id_usuario)
    bloco_prod = html_bloco_usuario.gera(usr)
    res = res + bloco_prod + "\n"
  lista_html = html_div.gera("display:inline-block", res)
  return lista_html
