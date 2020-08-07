import html_pag_compra_IMP

def gera(ses, cpr, atrs, erros):
  """Retorna uma página HTML que mostra os dados do pedido de compra {cpr}
  (que deve ser {None} ou um objeto de tipo {Objeto_Compra}), para visualização,
  alteração, ou criação de uma nova compra.
  
  O dicionário {atrs}, se não for {None}, deve ser um dicionário que
  (re)define alguns ou todos os atributos de um {Objeto_Compra}.
  Se um atributo for definido em {atrs}, mesmo como {None},
  esse valor substitui o valor do atributo de {cpr}.
  
  O parâmetro {ses} é a sessão que pediu esta página, e não pode ser
  {None}. O parâmetro {erros} é uma lista de mensagens de erro a mostrar
  no alto da página. Pode ser {None}.
  
  A página terá um <form>...</form> com campos <input> para os atributos
  da compra, Vide detalhes em {html_form_dados_de_compra.gera}.

    Se {cpr} for {None}, entende-se que o propósito da página é a criação
    de um novo pedido de compra no sistema.  Nesse caso {ses} não pode ser {None}
    nem sessão de administrador.  Haverá um botão submit 
    "Acrescentar" para confirmar a criação.

    Se {cpr} não for {None}, entende-se que o pedido de compra {cpr}
    está sendo visualizado e possivelmente alterado. Neste caso, a
    sessão deve pertencer a um administrador ou ao cliente que é dono da
    compra {cpr}. O formulário incluirá um campo visível 'id_compra' com
    o ID de {cpr}, como "readonly". Vários campos serão edtáveis. Haverá
    um botão "Alterar" para confirmar as alterações, e um botão
    "Finalizar" para fechar a compra. Além disso, haverá uma lista das
    poltronas (bilhetes) da compra, em forma resumida. Vide
    {html_lista_de_poltronas_de_compra.gera}. Os campos e botões que
    aparecem na página dependem do caso determinado por {ses} e {cpr}.
    Haverá botões "Ver", "Comprar", "Excluir", "Trocar" etc. em cada poltrona,
    quando cabíveis, permitindo que o usuário faça essas operações. Veja
    {html_resumo_de_poltrona_de_compra.gera}.
  """
  return html_pag_compra_IMP.gera(ses, cpr, atrs, erros)
