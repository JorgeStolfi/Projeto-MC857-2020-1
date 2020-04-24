import html_span

def gera(texto, disp, fam_fonte, tam_fonte, peso_fonte, pad, halign, cor_texto, cor_fundo):
  estilo = \
    ( " display: " + disp + ";" if disp != None else "") + \
    ( " font-family:" + fam_fonte + ";" if fam_fonte != None else "") + \
    ( " font-weight:" + peso_fonte + ";" if peso_fonte != None else "") + \
    ( " font-size:" + tam_fonte + ";" if tam_fonte != None else "") + \
    ( " padding:" + pad + ";" if pad != None else "") + \
    ( " background-color:" + cor_fundo + ";" if cor_fundo != None else "") + \
    ( " color:" + cor_texto + ";" if cor_texto != None else "") + \
    ( " text-align:" + halign + ";" if halign != None else "")
  return html_span.gera(estilo, texto)
