import trecho
import html_relatorio_de_trafego

def processa(ses, args):
  assert ses != None   # Deveria acontecer.
  lista_aeroportos = ["VCP", "SDU", "POA", "MAO", "GIG", "CGH", "CFN", "BSB"]

  trechos_por_aeroporto = {}
  for aeroporto in lista_aeroportos:
    origem = trecho.busca_por_origem(aeroporto)
    destino = trecho.busca_por_destino(aeroporto)

    trechos_por_aeroporto[aeroporto] = {'origem': origem, 'destino': destino}

  print(trechos_por_aeroporto)


  # resumo = trecho.resumo_de_trafego

  pag = None 
  
  # print(resumo)
  # ht_resumo = html_resumo_de_trafego.gera(ses, trc, comprar_pols, alterar_trc, id_cpr)

  return pag
