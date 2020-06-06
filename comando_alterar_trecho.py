import comando_alterar_trecho_IMP


def processa(ses, args):
    """Esta função é chamada quando o usuário aperta o botão "Alterar"
    em um formulário para alterar um trecho, após ter preenchido
    os campos do mesmo.

    Os dados do trecho devem estar definidos no dicionário {args}.
    Deve haver um campo 'id_trc' com valor não nulo;

    Se os dados forem aceitáveis, a função altera o trecho {trc},
    na base de dado; e retorna um formulário"""
    
    return comando_alterar_trecho_IMP.processa(ses, args)
