import html_form_dados_de_trecho
import html_pag_generica
import html_botao_simples

from utils_testes import erro_prog

def gera(ses, atrs, erros):
  # Constrói formulário com dados:
  id_trecho = None
  texto_bt = "Acrescentar"
  comando_bt = "acrescentar_trecho"
  conteudo = html_form_dados_de_trecho.gera(id_trecho, atrs, texto_bt, comando_bt)

  ht_cancel = html_botao_simples.gera("Cancelar", 'principal', None, "#ff2200")
  conteudo += "<br/>" + ht_cancel

  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
