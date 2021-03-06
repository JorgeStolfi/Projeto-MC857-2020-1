import html_estilo_de_botao
import html_input

def gera(texto, URL, args, cor_fundo):
  args_html = ""
  if args != None:
    # Acrescenta argumentos ao {args_html}:
    for key, val in args.items():
      kv_html = html_input.gera(None, 'hidden', key, val, None, False, False, None, None)
      args_html += kv_html

  # O botão propriamente dito:
  estilo = html_estilo_de_botao.gera(cor_fundo)
  html = args_html + \
    "<input" + \
    " type=\"submit\"" + \
    " style=\"" + estilo + "\n\"" + \
    " formaction=\"" + URL + "\"" + \
    " value=\"" + texto + "\"" + \
    "/>"
  return html
