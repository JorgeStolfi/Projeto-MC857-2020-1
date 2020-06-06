import roteiro
import html_resumo_de_roteiro
import html_lista_de_trechos
import html_pag_generica
import html_botao_simples

def gera(ses, rot, erros):
  ver_roteiro = False # Já estamos vendo o roteiro.
  campos_resumo = html_resumo_de_roteiro.gera(rot, ver_roteiro)
  ht_resumo = " ".join(str(campos_resumo))
  
  alterar_trechos = False # Não deve ter botões de "Alterar".
  ht_trechos = html_lista_de_trechos.gera(rot, alterar_trechos)
  
  ht_conteudo = ht_resumo + "<br/>" + ht_trechos

  ids_trechos = roteiro.obtem_identificadores_de_trechos(rot)
  ids_trechos_txt = ",".join(ids_trechos)
  ht_comprar = html_botao_simples("Comprar", "comprar_roteiro", {'ids_trechos': ids_trechos_txt}, "#22ff22")
  ht_conteudo.append(ht_comprar)

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
