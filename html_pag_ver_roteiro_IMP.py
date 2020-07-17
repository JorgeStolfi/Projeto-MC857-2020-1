import roteiro
import html_resumo_de_roteiro
import html_lista_de_trechos
import html_pag_generica
import html_botao_simples
import trecho 

def gera(ses, rot, erros):
  ver_roteiro = False # Já estamos vendo o roteiro.
  campos_resumo = html_resumo_de_roteiro.gera(rot, ver_roteiro)
  ht_resumo = " ".join(str(campos_resumo))
  
  # ??? EXPANDIR COMO {html_pag_ver_compra}
  
  alterar_trcs = False # Não deve ter botões de "Alterar".
  ht_trechos = html_lista_de_trechos.gera(rot, alterar_trcs)
  
  ht_conteudo = ht_resumo + "<br/>" + ht_trechos

  ids_trechos = roteiro.obtem_identificadores_de_trechos(rot)
  ids_trechos_txt = ",".join(ids_trechos)

  # verifica se todos os trechos estao abertos
  roteiro_aberto = True
  for id in ids_trechos:
    roteiro_aberto = roteiro_aberto and (trecho.busca_por_identificador(id))["Aberto"]

  if roteiro_aberto:
    ht_comprar = html_botao_simples.gera("Comprar", "comprar_roteiro", {'ids_trechos': ids_trechos_txt}, "#22ff22")
    ht_conteudo += "<br/>" + ht_comprar

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
