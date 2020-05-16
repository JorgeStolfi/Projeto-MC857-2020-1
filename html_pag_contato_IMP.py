#import html_form_contato
import html_pag_generica
import html_bloco_texto

def gera(ses, erros):
  #conteudo = html_form_contato.gera()
  texto1 = "Entre em contato no telefone (11)99999-9999"
  cor_texto = "#000488"
  cor_fundo = "#eeeeee"
  bloco_texto1 =  html_bloco_texto.gera(texto1, None,"Courier","16px","normal","5px","center", cor_texto, cor_fundo)
  pagina = html_pag_generica.gera(ses, bloco_texto1, erros)
  return pagina
