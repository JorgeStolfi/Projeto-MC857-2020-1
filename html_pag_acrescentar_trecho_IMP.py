import html_form_acrescentar_trecho
import html_pag_generica

from utils_testes import erro_prog

def gera(ses, args, erros):
  if ses == None:
    # Não deveria acontecer:
    erro_prog("usuário deveria estar logado")

  # Constrói formulário com dados:
  conteudo = html_form_acrescentar_trecho.gera(args)
  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
