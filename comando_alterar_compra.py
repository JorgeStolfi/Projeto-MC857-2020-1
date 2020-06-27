import comando_alterar_compra_IMP

def processa(ses, args):
    """Esta função é chamada quando o administrador aperta o botão "Alterar" no
    formulário gerado pelo botão "Checar Objeto" do menu principal.

    O propósito da função é alterar o nome do passageiro de uma compra. O novo
    nome do passageiro esta em {args} com a chave {nome_pass}. Além disso,
    {args} deve conter o id do cliente {id_usr}, o id da compra {id_compra} e o
    status da compra {status}.

    Se a atualização for bem sucedida a tela "Checar Objeto" irá mostrar a
    compra com o nome do novo passageiro. Em caso de erro, será mostrado a
    página de erro.
    """
    return comando_alterar_compra_IMP.processa(ses, args)
