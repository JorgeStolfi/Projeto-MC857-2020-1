import html_resumo_de_roteiro
import html_lista_de_trechos
import html_pag_generica



def gera(ses, rot):
  ver_roteiro = False # Já estamos vendo o roteiro.
  campos_resumo = html_resumo_de_roteiro.gera(rot, ver_roteiro)
  ht_resumo = " ".join(str(campos_resumo))
  
  alterar_trechos = False # Não deve ter botões de "Alterar".
  ht_trechos = html_lista_de_trechos.gera(ses, rot, alterar_trechos)
  ht_conteudo = ht_resumo + "<br/>" + ht_trechos
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag
