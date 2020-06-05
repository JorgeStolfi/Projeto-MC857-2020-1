import html_form_dados_de_trecho
import html_pag_generica

from utils_testes import erro_prog

def gera(ses, atrs, erros):
  # Constrói formulário com dados:
  conteudo = html_form_dados_de_trecho.gera(None, atrs, "Acrescentar", 'acrescentar_trecho')
  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
