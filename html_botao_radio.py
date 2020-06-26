import html_botao_radio_IMP

def gera(nome, valor, rotulo):
  """Devolve um fragmento HTML5 que implementa um <input> de tipo "radio
  button" (uma alternativa de um item de múltipla escolha).
   
  O parâmetro {nome} é o nome da variável cujo valor é definido por este
  botão; por exemplo, 'cor'. Quando um botão rádio é selecionado, todos
  os outros botões rádio com mesmo {nome} dentro do mesmo
  <form>...</form> são des-selecionados.
   
  O {valor} é um string que é atribuído à variável de nome {nome} quando 
  o botão é selecionado.  Por exemplo, 'rosa' ou 'azul'.

  O parâmetro {rotulo} é o texto visível ao usuário. Por exemplo, "Cor de rosa"
  ou "Azul marinho".  
  
  Quando um botão "submit" é ativado dentro do <form>, o comando POST emitido
  vai incluir a atribuição "{nome}={valor}"."""
  return html_botao_radio_IMP.gera(nome, valor, rotulo) 
