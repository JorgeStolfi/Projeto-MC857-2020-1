# Implementação do módulo {comando_alterar_trecho}.

import html_pag_login
import html_pag_alterar_usuario
import usuario
import trecho
import sessao
from valida_campo import ErroAtrib


def msg_campo_obrigatorio(nome_do_campo):
    return "O campo %s é obrigatório." % nome_do_campo


def processa(ses, args):
    # Determina se o usuário corrente {usr_ses} é administrador:
    if ses is None:
        admin = False
    else:
        usr_ses = sessao.obtem_usuario(ses)
        assert usr_ses is not None
        admin = usuario.obtem_atributos(usr_ses)['administrador']

    id_trc = args["id_trc"]
    assert id_trc is not None, "id_trc obrigatório para atualizar"

    # Tenta editar o trecho:
    try:
        usuario.confere_e_elimina_conf_senha(args)
        trc_antigo = trecho.busca_por_identificador(id_trc)

        campos_para_atualizar = args.copy()
        campos_para_atualizar.pop("id_trc")

        trecho.muda_atributos(trc_antigo, campos_para_atualizar)

        pag = html_pag_login.gera(ses, None)
    except ErroAtrib as ex:
        erros = ex.args[0]
        # Repete a página de cadastrar com os mesmos argumentos e mens de erro:
        pag = html_pag_alterar_trecho.gera(ses, id_trc, args, erros)
    return pag
