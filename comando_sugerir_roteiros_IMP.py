# Implementação do comando criar roteiro
import roteiro
import html_lista_de_roteiros
import html_pag_generica
import html_pag_sugerir_roteiros

from valida_campo import ErroAtrib

def processa(ses, args):
  try:
    # Por via das dúvidas:
    if args == None: args = {}.copy()
    
    erros = [].copy()
    
    # Verifica e obtem campos obrigatórios:
    for ch in ('origem', 'dia_min', 'destino', 'dia_max'):
      if not ch in args: 
        erros.append("O campo '%s' deve ser preenchido" % ch)
        
    # Obtem parâmetros obrigatórios da busca:
    origem = args['origem'] if 'origem' in args else None;
    dia_min = args['dia_min'] if 'dia_min' in args else None;
    destino = args['destino'] if 'destino' in args else None;
    dia_max = args['dia_max'] if 'dia_max' in args else None;

    # Obtem parãmetros opcionais, com defaults:
    hora_min = args['hora_min'] if 'hora_min' in args else "00:00";
    hora_max = args['hora_max'] if 'hora_max' in args else "23:59";
    
    # Monta as datas para busca:
    data_min = dia_min + " " + hora_min + " UTC"
    data_max = dia_max + " " + hora_max + " UTC"

    # Verifica se intervalo é razoável: !!! Deveria exigir mais que 1 minuto !!!
    if data_min >= data_max:
      erros.append("Intervalo de datas inválido")
    
    if len(erros) > 0: raise ErroAtrib(erros)
      
    # Chamando a busca recursiva:
    soh_disponiveis = True
    roteiros = roteiro.descobre_todos(origem, data_min, destino, data_max, soh_disponiveis)

    # Monta página com resposta:
    roteiros_html = html_lista_de_roteiros.gera(roteiros)
    pag = html_pag_generica.gera(ses, roteiros_html, None)
    return pag

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página com mensagens de erro:
    pag = html_pag_sugerir_roteiros.gera(ses, erros)
    return pag
