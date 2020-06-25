import comando_trocar_poltrona_IMP

def processa(ses, id_poltrona, trc, id_compra):
    """Esta função é chamada quando um usuário aperta o botão "Trocar"
    na página Meu carrinho. 
  
    A sessão corrente {ses} não pode ser {None}.

    A função libera a poltrona e retorna uma página HTML {pag} 
    contendo a lista de poltronas disponíveis. """

    return comando_trocar_poltrona_IMP.processa(ses, id_poltrona, trc, id_compra)