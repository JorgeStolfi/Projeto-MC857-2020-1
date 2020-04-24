import html_input_IMP

def gera(rotulo, tipo, nome, val_ini, editavel, dica, cmd):
  """Gera o HTML para um campo de dados "<input ... />" com atributos dados.
  Este fragmento geralmente é incluído em um formulário "<form>...</form>".
  
  O parâmetro {rotulo} é um rótulo opcional. Se não for {None}, será inserido na frente
  do elemento "<input.../>" na meio de um elemento "<label>{rotulo}</label>".
  
  O parâmetro {tipo} é o tipo de campo, por exemplo "text", "email", 
  "hidden", "password", "number", etc. (resulta em "<input type='{tipo}'.../>").
  
  O parâmetro {nome} é o nome do campo, que será usado para enviar 
  o valor do mesmo ao servidor (resulta em "<input ... name='{nome}' id='{nome}'.../>"). 
  Quando o comando POST do formulário for emitido, este campo
  será enviado como um par {nome}: {val_fin} nos argumentos do POST,
  onde {val_fin} é o valor fornecido pelo usuário.
  
  O parâmetro {val_ini} é o valor inicial do campo (resulta em 
  "<input ... value='{val_ini}'.../>"). Se for {None}, esse atributo é omitido e o
  valor do campo será inicialmente nulo. Senão, {val_ini} deve ser
  uma string.  Se o usuário não editar o campo, {val_ini}
  será devolvido ao servidor no POST do formulário, como valor desse campo.
  
  O valor do campo poderá ser editado pelo usuário apenas se {editavel} for {True}.
  Se for {False}, {val_ini} não pode ser {None}.
  
  O parâmetro {dica} é um texto que será mostrado no campo, se {val_ini} for {None},
  para orientar o preenchimento (resulta em "<input ... placeholder='{dica}' .../>").
  Este campo NÃO será devolvido ao servidor Se for {None}, o campo estará inicialmente em branco.
  
  O parâmetro {cmd}, se não for {None}, é o comando que será enviado ao 
  servidor via POST, quando o usuário alterar este campo, em vez do
  "action" default do formulário."""  
  return html_input_IMP.gera(rotulo, tipo, nome, val_ini, editavel, dica, cmd)
