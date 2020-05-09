# Implementação do módulo {comando_alterar_usuario}.

import html_pag_login
import html_pag_alterar_usuario
import usuario
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

    id_usuario = args["id_usuario"]
    assert id_usuario is not None, "id_usuario obrigatório para atualizar"

    # Tenta editar o usuário:
    try:
        usuario.confere_e_elimina_conf_senha(args)
        usr_antigo = usuario.busca_por_identificador(id_usuario)

        campos_para_atualizar = args.copy()
        campos_para_atualizar.pop("id_usuario")

        usuario.muda_atributos(usr_antigo, campos_para_atualizar)

        pag = html_pag_login.gera(ses, None)
    except ErroAtrib as ex:
        erros = ex.args[0]
        # Repete a página de cadastrar com os mesmos argumentos e mens de erro:
        pag = html_pag_alterar_usuario.gera(ses, id_usuario, args, erros)
    return pag
