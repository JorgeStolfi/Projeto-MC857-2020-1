import comando_alterar_trecho_IMP


def processa(ses, args):
    """Esta função é chamada quando o usuário aperta o botão "Alterar"
    em um formulário para alterar um trecho, após ter preenchido
    os campos do mesmo.

    Os dados do trecho devem estar definidos no dicionário {args}.
    Deve haver um campo 'senha' com valor não nulo, um campo 'conf_senha'
    com o mesmo valor e um campo 'id_trc' não nulo.

    Se os dados forem aceitáveis, a função altera o trecho {trc},
    na base de dado; e retorna um formulário
    para o usuário fazer login (com campos para email e senha,
    e um botão "Entrar").

    Se os dados não forem aceitáveis, a função devolve o
    mesmo formulário de alterar usuário, com os mesmos
    dados nos campos preenchidos, com uma ou mais mensagens de erro
    adequadas."""
    return comando_alterar_trecho_IMP.processa(ses, args)
