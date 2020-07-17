import comando_alterar_poltrona_IMP

def processa(ses, args):
    """Esta função é chamada quando o administrador aperta o botão "Alterar" no
    formulário gerado pelo botão "Checar Objeto" do menu principal.

    O propósito da função é alterar os dados de uma poltrona, com exceção de seu id.
    A sessão {ses} deve pertencer à um administrador. Além disso, {args} deve ser
    um dicionário contendo:
    'id_poltrona': o ID (string) da poltrona existente;
    'id_trecho': o novo ID (string) do trecho referente;
    'id_compra': o novo ID (string) de uma compra referente à essa poltrona; # TODO: atualmente esse valor é obrigatorio mas não é utilizado, dar uma olhada!
    'numero': o novo número (string) da poltrona;
    'oferta': o novo valor ('on' ou 'off') identificando se essa poltrona foi comprada na oferta;
    'preco': o novo preço (string representando um float ou um float) da poltrona

    Os valores 'id_trecho' E 'numero' de {args} não podem estar sendo usados AO MESMO TEMPO 
    por outra poltrona no banco de dados (é feito uma busca com AND por esses atributos no banco).

    Se a atualização for bem sucedida a tela "Checar Objeto" irá mostrar a
    poltrona com os novos dados. Em caso de erro, será mostrado a
    página de erro.
    """
    return comando_alterar_poltrona_IMP.processa(ses, args)
