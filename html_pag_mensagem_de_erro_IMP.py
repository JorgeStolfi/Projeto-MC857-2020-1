import html_pag_generica
import html_botao_simples

def gera(ses, erros):
  ht_botao = html_botao_simples.gera("OK", 'principal', None, '#55ee55')
  pagina = html_pag_generica.gera(ses, ht_botao, erros)
  return pagina
