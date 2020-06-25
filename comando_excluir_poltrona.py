# Este módulo processa o acionamento do botão "Excluir" da página "Meu carrinho" do Usuário.
import comando_excluir_poltrona_IMP


def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Excluir" no
  formulário que lista as poltronas na página "Meu carrinho".

  O parâmetro {args} é um dicionário que contém os elementos corrrespondente às chaves
  {id_poltrona} e {id_compra} fazendo refêrencia à poltrona que será excluída e a compra  que ela pertence
   - e.g.: {{'id_poltrona': "A-00000001", 'id_compra':"C-00000001"}}. A função será responsável por buscar um
   {Objeto_Poltrona} com esse identificador e definir seu atributo {id_compra} como {None}.

  O resultado deve ser uma página "Meu carrinho" atualizada (com o trecho excluído sem ser
  listado), gerada por {html_ver_compra.gera}."""
  return comando_excluir_poltrona_IMP.processa(ses, args)