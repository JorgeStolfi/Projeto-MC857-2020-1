# Implementação do comando criar roteiro
import roteiro
import html_lista_de_roteiros
import html_pag_generica

from valida_campo import ErroAtrib

def processa(ses, args):

  #recebo args com origem e destino
  origem = args['origem']
  destino = args['destino']
  dia_min = args['dia_min']
  dia_max = args['dia_max']

  #Verificar se recebemos origem e destino não vazio
  if (origem and destino and dia_min and dia_max):
    
    #chamando a função que decobre esses trechos
    roteiros = roteiro.descobre_todos(origem, destino, dia_min, dia_max)

    #chamo modulo 
    roteiros_html = html_lista_de_roteiros.gera(roteiros)
    pag = html_pag_generica.gera(ses, roteiros_html, None)
  else:
    raise ErroAtrib("campos 'origem', 'destino', 'dia_min' e 'dia_max' devem ser preenchidos")
  return pag
