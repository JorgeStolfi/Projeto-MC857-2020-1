import html_form_dados_de_trecho_IMP

def gera(id_trc, atrs, admin, ht_submit):
  """Retorna um <form>...</form> com os dados do {trecho} cujo
  identificador é {id_trc}, que pode ser {None} no caso de um trecho que
  está sendo criado.

  O formulário vai conter um elemento <table>..</table> onde cada linha
  mostra um dos atributos de um {Objeto_Trecho}. Os valores desses
  campos são inicializados conforme o dicionário {atrs} (e NÃO com os
  atributos correntes do trecho).
  
  O parãmetro {admin} diz se o usuário que pediu este formulário é
  administrador.

    Se {id_trc} é {None}, retorna um formulário apropriado para
    cadastrar novo trecho. Neste caso {admin} deve ser {True}. Não
    haverá um campo para o identificador, e todos os campos serão
    editáveis.

    Se {id_trc} não é {None}, retorma um formulário apropriado para
    visualizar ou alterar os dados do trecho {trc} cujo identificador é
    {id_trc}, que supostamente já existe. Se {admin} for {True}, o
    identificador será visível, e todos os campos serão editáveis,
    exceto 'identificador', o código do voo, os aeroportos de 'origem' e
    'destino', e 'poltronas'. Senão, o identificador será "hidden" e
    todos os campos serão "readonly".

  O parãmetro {ht_submit}, se não for {None}, deve ser um fragmento HTML
  que será incluído no <form>...</form> após todos os campos. Seve
  conter pelo menos um botão "submit". Quando acionado, esse botãovai
  causar a emissão de um comando HTTP "POST" com os dados do formulário.

  """
  return html_form_dados_de_trecho_IMP.gera(id_trc, atrs, admin, ht_submit)
