import comando_trocar_poltrona_IMP

def processa(ses, args):
    """Esta função é chamada quando um usuário aperta o botão "Trocar"
    na página Meu carrinho. 
  
    A sessão corrente {ses} não pode ser {None}.

    A função libera a poltrona e retorna uma página HTML {pag} 
    contendo a lista de poltronas disponíveis. """
    id_poltrona = args['id_poltrona']
    id_trecho = args['id_trecho']
    id_compra = args['id_compra']
    return comando_trocar_poltrona_IMP.processa(ses, id_poltrona, id_trecho, id_compra)