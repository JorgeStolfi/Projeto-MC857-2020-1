import html_form_acrescentar_trecho
import html_pag_generica

from utils_testes import erro_prog

def gera(ses, atrs, erros):
  # Constrói formulário com dados:
  conteudo = html_form_acrescentar_trecho.gera(atrs)
  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
