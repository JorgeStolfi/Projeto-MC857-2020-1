import html_form_entrar
import html_pag_generica

def gera(ses, erros):
  conteudo = html_form_entrar.gera()
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
