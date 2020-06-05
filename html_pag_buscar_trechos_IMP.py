import sessao
import usuario
import html_form_buscar_trechos
import html_pag_generica

def gera(ses, atrs, admin, erros):
  # Constrói formulário com dados:
  ht_dados = html_form_buscar_trechos.gera(atrs, admin)
  conteudo = ht_dados
  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
