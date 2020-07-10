import comando_sugerir_roteiros_IMP

def processa(ses, args):
    """Esta funcao é chamada quando não existe um trecho direto entre a origem e o destino do 
    usuario, entao ele pede para o sistema encontrar um roteiro que atenda as necessidade de
    origem e destino. Essa função recebe 4 argumentos são eles:
    ['origem']
    ['destino']
    ['dia_min']
    ['dia_max']
    Ela devolve um pagina html para mostrar os roteiros encontrados.
    """
    return comando_sugerir_roteiros_IMP.processa(ses,args)
