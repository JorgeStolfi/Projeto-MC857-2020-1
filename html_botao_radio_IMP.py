import html_input

def gera(nome, valor, rotulo):
  id_bot = nome + "." + valor;
  ht_input = \
    "<input" + \
      " type=\"radio\"" + \
      " name=\"" + nome + "\"" + \
      " value=\"" + valor + "\"" + \
      " id=\"" + id_bot + "\"" + \
    "/>"
  ht_label = "<label for=\"" + id_bot + "\">\"" + rotulo + "\"</label>"
  ht_bot = ht_input + ht_label
  return ht_bot
