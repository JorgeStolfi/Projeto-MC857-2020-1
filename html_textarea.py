import html_textarea_IMP

def gera(rotulo, nome, val_ini, editavel, obrigatorio, dica, cmd):
  """Gera o HTML para um elemento de textarea  "<textarea ... ></textarea>".
  Este fragmento geralmente é incluído em um formulário "<form>...</form>".
  
  O parâmetro {rotulo} é um rótulo opcional. Se não for {None}, será inserido na frente
  do elemento "<textarea>" na forma de um elemento "<label>{rotulo}</label>".
  
  O parâmetro {nome} é o nome do campo, que será usado para enviar o
  valor do mesmo ao servidor, e também o atributo "id".  Resulta em "<textarea ...
  name='{nome}' id='{nome}'.../>". Quando o comando POST do formulário for emitido,
  este campo será enviado como um par {nome}: {val_fin} nos argumentos
  do POST, onde {val_fin} é o texto digitado pelo usuário.
  
  O parâmetro {val_ini} é o conteúdo inicial do campo (resulta em
  "<textarea> {val_ini}</textarea>"). Se for {None} o texto será
  inicialmente nulo. Senão, {val_ini} deve ser uma string. Se o usuário
  não editar o campo, {val_ini} será devolvido ao servidor no POST do
  formulário, como valor desse campo.
  
  O parâmetro {editavel} é um booleano que diz se o conteúdo deste campo
  poderá ser editado pelo usuário. Se for {False}, {val_ini} não pode ser {None}.

  O parâmetro {obrigatorio} indica se o campo deve ser obrigatóriamente preenchido ou não.
  Isso altera visualmente a forma como o campo é exibido para o usuário pelo navegador. O valor
  default deste parâmetro é False, por questões de compatibilidade.
  
  O parâmetro {dica} é um texto que será mostrado no campo, se {val_ini}
  for {None}, para orientar o preenchimento (resulta em "<textarea ...
  placeholder='{dica}' ...>"). Este campo NÃO será devolvido ao
  servidor Se for {None}, o campo estará inicialmente em branco.
  
  O parâmetro {cmd}, se não for {None}, é o comando que será enviado ao 
  servidor via POST, quando o usuário alterar este campo, em vez do
  "action" default do formulário."""  
  return html_textarea_IMP.gera(rotulo, nome, val_ini, editavel, obrigatorio, dica, cmd)
