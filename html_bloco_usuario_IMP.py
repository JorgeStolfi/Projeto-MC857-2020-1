import usuario
import html_paragrafo
import html_span
import html_bloco_texto

def gera(usr):
  atrs = usuario.obtem_atributos(usr)

  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"

  nome = atrs['nome']
  ht_nome = html_paragrafo.gera(estilo_parag, html_bloco_texto.gera(nome, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  email = atrs['email']
  ht_email = html_paragrafo.gera(estilo_parag, html_bloco_texto.gera(email, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  CPF = atrs['CPF']
  ht_CPF = html_paragrafo.gera(estilo_parag, html_bloco_texto.gera(CPF, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  telefone = atrs['telefone']
  ht_telefone = html_paragrafo.gera(estilo_parag, html_bloco_texto.gera(telefone, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  documento = atrs['documento']
  ht_documento = html_paragrafo.gera(estilo_parag, html_bloco_texto.gera(documento, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  ht_final = ht_nome + ht_email + ht_CPF + ht_telefone + ht_documento
  bloco_final = html_span.gera("\n display: inline-block;", ht_final)
  
  width_pct = ("33%")
  estilo_final = f"width: {width_pct}; padding: 15px; border-radius: 15px 50px 20px; display: flex; align-items: center;"
  bloco_final = html_span.gera(estilo_final, bloco_final)
  return bloco_final
