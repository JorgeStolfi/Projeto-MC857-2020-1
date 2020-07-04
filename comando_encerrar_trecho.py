import comando_encerrar_trecho_IMP


def processa(ses, args):
    """Esta função é chamada quando o usuário aperta o botão "Encerrar"
    na página {ver_objeto} de um trecho.

    Os dados do trecho devem estar definidos no dicionário {args}.
    Deve haver um campo 'id_trecho' com valor não nulo;

    Se os dados forem aceitáveis, a função (por enquanto) apaga todos os campos 'oferta' das poltronas do trecho."""

    return comando_encerrar_trecho_IMP.processa(ses, args)
