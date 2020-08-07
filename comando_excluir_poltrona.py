# Este módulo processa o acionamento do botão "Excluir" da página "Meu carrinho" do Usuário.
import comando_excluir_poltrona_IMP


def processa(ses, args):
  """Esta função é chamada quando o usuário pede para excluir uma poltrona de 
  uma de suas compras.

  O parâmetro {args} é um dicionário que contém um campo com chave 'id_poltrona' 
  cujo valor é o identificador {id_pol} da poltrona a excluir; p. ex.
  {{'id_poltrona': "A-00000001"}}. Essa poltrona deve estar reservada para 
  alguma compra.  A função cancela essa reseva, liberando a poltrona.
  
  A sessão {ses} não pode ser {None}. Se dono da sessão {ses} não for
  administrador, deve ser o dono da compra a alterar;
  se essa compra não for o carrinho desse usuário, ela passa a ser.

  O resultado será uma página que mostra essa compra. {html_ver_compra.gera}."""
  return comando_excluir_poltrona_IMP.processa(ses, args)
