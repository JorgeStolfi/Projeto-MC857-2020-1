import html_form_ver_objeto
import html_pag_generica

from utils_testes import erro_prog

def gera(ses, atrs, erros):
  # Constrói formulário com dados:
  conteudo = html_form_dados_de_trecho.gera(None, atrs, "Checar objeto", 'ver_objeto')
  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
