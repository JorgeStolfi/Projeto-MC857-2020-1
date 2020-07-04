import html_form_contato
import html_pag_generica
import html_texto

def gera(ses, erros):
  #conteudo = html_form_contato.gera()
  #texto1 = "Entre em contato no telefone (11)99999-9999"
  #cor_texto = "#000488"
  #cor_fundo = "#eeeeee"
  #bloco_texto1 =  html_texto.gera(texto1, None,"Courier","16px","normal","5px","center", cor_texto, cor_fundo)

  # Constrói formulário com dados:
  admin = False
  ht_dados = html_form_contato.gera({}, admin)
  conteudo = ht_dados

  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
