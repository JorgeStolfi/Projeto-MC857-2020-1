import html_pag_trecho_IMP

def gera(ses, trc, atrs, erros):
  """Retorna uma página HTML que mostra os dados do trecho {trc} (que deve
  ser {None} ou um objeto de tipo {Objeto_Trecho}), para visualização,
  alteração, ou criação de novo trecho.

  Caso {atrs} não seja {None}, deve ser um dicionário que (re)define
  valores para alguns ou todos os atributos de um {Objeto_Trecho}. Se um
  atributo tiver valor definido em {atrs}, mesmo que {None}, esse
  valor tem precedência sobre o valor em {trc}.
  
  O parâmetro {ses} é a sessão que pediu esta página. O parâmetro
  {erros} é uma lista de mensagens de erro a mostrar no alto da página.
  Pode ser {None}.
  
  A página conterá um <form>...</form> com campos <input> para os
  atributos do trecho. Vide detalhes em
  {html_form_dados_de_trecho.gera}. Em seguida haverá uma lista das
  poltronas do trecho, em forma resumida. Vide
  {html_lista_de_poltronas_de_trecho.gera}. Os campos e botões que
  aparecem na página dependem do caso determinado por {ses} e {trc}.

    Se {trc} for {None}, entende-se que o propósito da página é a inclusão
    de um novo trecho no sistema.  Nesse caso {ses} não pode ser {None}
    e deve ser sessão de administrador.  Haverá um botão submit 
    "Acrescentar" para confirmar a criação.

    Se {trc} não for {None}, entende-se que o trecho {trc} está sendo
    visualizado e possivelmente alterado. Neste caso: 
    
      Se {ses} for uma sessão de administrador, o formulário incluirá um
      campo visível 'id_trecho' com o ID de {trc}, como "readonly";
      vários campos serão edtáveis; e haverá um botão "Alterar" para
      confirmar as alterações. Haverá também um botão "Clonar" para
      criar um trecho semelhante.
      
      Se {ses} for uma sessão de cliente comum, o campo 'id_trecho' será
      "hidden", todos os campos serão "readonly, e não haverá botão
      "Alterar". Mas haverá botões "Comprar", "Excluir", "Trocar" etc.
      em cada poltrona, quando cabíveis, permitindo que o usuário faça essas
      operações.  Veja {html_resumo_de_poltrona_de_trecho.gera}
      
      Se {ses} for {None}, entende-se que o usuário não fez login.
      Nesse caso todos os campos serão "readonly" e não haverá 
      botões de "Alterar", nem botões "Comprar", etc. em cada
      poltrona.
 
  Em todo caso, cada poltrona terá um botão "Ver", que, quando clicado,
  emite o comando HTTP "ver_poltrona".

  A página também terá um botão simples "Cancelar" ou "Voltar",
  que, quando clicado, emite o comando "principal".

  """
  return html_pag_trecho_IMP.gera(ses, trc, atrs, erros)
