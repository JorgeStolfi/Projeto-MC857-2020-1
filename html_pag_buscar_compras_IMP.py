import html_pag_generica
import html_div


def gera(ses):
  conteudo = html_div.gera("display:inline-block", "TODO: Implementar página de busca")
  pagina = html_pag_generica.gera(ses, conteudo, None)
  return pagina
