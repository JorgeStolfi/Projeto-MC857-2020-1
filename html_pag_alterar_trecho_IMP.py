import sessao
import trecho
import html_form_dados_de_trecho
import html_pag_generica

from utils_testes import erro_prog

def gera(ses, id_trecho, atrs, erros):
  # Constrói formulário com dados:
  texto_botao = "Alterar"
  conteudo = html_form_dados_de_trecho.gera(id_trecho, atrs, texto_botao, comando)
  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
