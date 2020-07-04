import comando_ver_poltrona_IMP


def processa(ses, args):
    """
    Esta função é chamada quando um usuário aperta o botão "Ver" referente à uma poltrona
    na página "Meu carrinho". {args} é um dicionário contendo o atributo {'id-poltrona'}
    de uma poltrona.

    A sessão corrente {ses} não pode ser {None} e deve estar aberta.

    A função retorna uma página HTML {pag} contendo as informações da poltrona requisitada.

    Caso a sessão for {None} ou não existir uma poltrona com identificador igual à {'id-poltrona'},
    retornará uma página de erro.
    """
    return comando_ver_poltrona_IMP.processa(ses, args)