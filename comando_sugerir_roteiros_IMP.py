# Implementação do comando criar roteiro
import roteiro
import html_lista_de_roteiros
import html_pag_generica
import html_pag_sugerir_roteiros

from valida_campo import ErroAtrib

def processa(ses, args):
  try:
    if not args:
      raise ErroAtrib("Todos campos devem estar preenchidos")

    if 'origem' in args:
      origem = args['origem']
    else:
      raise ErroAtrib("O campo origem deve ser preenchidos")

    if 'destino' in args:
      destino = args['destino']
    else:
      raise ErroAtrib("O campo destino deve ser preenchidos")

    if 'dia_min' in args:
      dia_min = args['dia_min']
    else:
      raise ErroAtrib("O campo dia mínimo deve estar preenchidos")

    if 'dia_max' in args:
      dia_max = args['dia_max']
    else:
      raise ErroAtrib("O campo dia máximo deve estar preenchidos")

    #Verificar se recebemos origem e destino não vazio
    if (origem is not None and destino is not None and dia_min is not None and dia_max is not None):
      
      #chamando a função que decobre esses trechos
      roteiros = roteiro.descobre_todos(origem, destino, dia_min, dia_max)

      #chamo modulo 
      roteiros_html = html_lista_de_roteiros.gera(roteiros)
      pag = html_pag_generica.gera(ses, roteiros_html, None)
      return pag
    else:
      raise ErroAtrib("Todos campos devem estar preenchidos")
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página com mensagem de erro:
    pag = html_pag_sugerir_roteiros.gera(ses, erros)
    return pag
