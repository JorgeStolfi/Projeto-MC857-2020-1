import trecho
import html_relatorio_de_trafego
import sys

def processa(ses, args):
  assert ses != None   # Deveria acontecer.
  lista_aeroportos = trecho.todos_os_aeroportos()

  resumos = []
  for aeroporto in lista_aeroportos:
    origem = trecho.busca_por_origem(aeroporto)
    destino = trecho.busca_por_destino(aeroporto)

    resumo_origem = trecho.resumo_de_trafego(origem)
    resumo_destino = trecho.resumo_de_trafego(destino)
    resumos.append((aeroporto, resumo_origem, resumo_destino))
  
  # Para fins de teste
  sys.stderr.write("dados: %s" % resumos)
  
  pag = html_relatorio_de_trafego.gera(ses, resumos)
  return pag
