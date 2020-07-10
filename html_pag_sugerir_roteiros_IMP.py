import html_form_sugerir_roteiros
import html_pag_generica
import sessao
import usuario


def gera(ses, erros):
  conteudo = html_form_sugerir_roteiros.gera()
  pag = html_pag_generica.gera(ses, conteudo, erros)
  return pag
