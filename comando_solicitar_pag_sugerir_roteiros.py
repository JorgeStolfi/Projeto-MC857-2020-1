import comando_solicitar_pag_sugerir_roteiros_IMP

def processa(ses, args):
    """
        Esta função é chamada quando o usuário precisa adicionar um roteiro novo.

        A função retorna uma página HTML {pag} contendo o formulário para criar um novo
        roteiro e um botão de sumbissão "Criar".

        O dicionário de argumentos {args} é irrelevantes e pode ser {None}.

        O parâmetro {ses} deve estar definido e o usuário dono da sessão precisa ser Administrador.
    """
    return comando_solicitar_pag_sugerir_roteiros_IMP.processa(ses, args)
