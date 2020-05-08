import usuario
import html_paragrafo
import html_span

def gera(usr):
  atrs = usuario.obtem_atributos(usr)

  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"

  nome = atrs['nome']
  html_nome = html_paragrafo.gera(estilo_parag, bloco_texto(nome, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  email = atrs['email']
  html_email = html_paragrafo.gera(estilo_parag, bloco_texto(email, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  CPF = atrs['CPF']
  html_CPF = html_paragrafo.gera(estilo_parag, bloco_texto(CPF, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  telefone = atrs['telefone']
  html_telefone = html_paragrafo.gera(estilo_parag, bloco_texto(telefone, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  documento = atrs['documento']
  html_documento = html_paragrafo.gera(estilo_parag, bloco_texto(documento, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  html_final = html_nome + html_email + html_CPF + html_telefone + html_documento
  bloco_final = html_span.gera("\n display: inline-block;", html_final)
  
  width_pct = ("33%")
  estilo_final = f"width: {width_pct}; padding: 15px; border-radius: 15px 50px 20px; display: flex; align-items: center;"
  bloco_final = html_span.gera(estilo_final, bloco_final)
  return bloco_final
