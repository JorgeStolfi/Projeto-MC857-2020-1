import html_input_IMP

def gera(rotulo, tipo, nome, val_ini, val_min, editavel, obrigatorio, dica, cmd):
  """Gera o HTML para um campo de dados "<input ... />" com atributos dados.
  Este fragmento geralmente é incluído em um formulário "<form>...</form>".
  
  O parâmetro {rotulo} é um rótulo opcional. Se não for {None}, e {tipo}
  não for "hidden", será inserido na frente do elemento "<input.../>" na
  forma de um elemento "<label>{rotulo}</label>".
  
  O parâmetro {tipo} é o tipo de campo, por exemplo "text", "email", 
  "hidden", "password", "number", etc. (resulta em "<input type='{tipo}'.../>").
  
  O parâmetro {nome} é o nome do campo, que será usado para enviar o
  valor do mesmo ao servidor. Resulta em "<input ...
  name='{nome}'.../>". Quando o comando POST do formulário for emitido,
  este campo será enviado como um par {nome}: {val_fin} nos argumentos
  do POST, onde {val_fin} é o valor fornecido pelo usuário.
  
  O parâmetro {val_ini} é o valor inicial do campo (resulta em "<input
  ... value='{val_ini}'.../>"). Se for {None}, esse atributo é omitido e
  o valor do campo será inicialmente nulo. Senão, {val_ini} deve ser uma
  string (mesmo quando o campo é numérico). Se o usuário não editar o
  campo, {val_ini} será devolvido ao servidor no POST do formulário,
  como valor desse campo.
  
  O parâmetro {val_min} é relevante apenas se o {tipo} for 'number'. Se
  não for {None}, deve ser um string que define o valor mínimo que o
  usuário pode digitar neste campo ("<input ... min='{val_min}' .../>").
  
  O parâmetro {editavel} é um booleano que diz se o valor deste campo
  poderá ser editado pelo usuário. Se for {False}, {val_ini} não pode ser {None}.
  Este parâmetro é ignorado se {tipo} for "hidden".

  O parâmetro {obrigatorio} indica se o campo deve ser obrigatóriamente preenchido ou não.
  Isso altera visualmente a forma como o campo é exibido para o usuário pelo navegador.
  Este parãmetro é ignorado se o tipo for "hidden", ou {editavel} for {False}.
  
  O parâmetro {dica} é um texto que será mostrado no campo, se {val_ini}
  for {None}, para orientar o preenchimento (resulta em "<input ...
  placeholder='{dica}' .../>"). Este campo NÃO será devolvido ao
  servidor Se for {None}, o campo estará inicialmente em branco.
  
  O parâmetro {cmd}, se não for {None}, é o comando que será enviado ao 
  servidor via POST, quando o usuário alterar este campo, em vez do
  "action" default do formulário.
  
  Em geral, cada campo deve ter um {nome} distinto. Porém, todos os
  elementos de tipo "radio" que são mutuamente exclusivos devem ter o
  mesmo nome, sendo distinguidos pelo {val_ini}. Portanto, o terá também
  um atributo {id} ("<input ... id='{id}' .../>") que é
  "{nome}.{val_ini}" se o tipo for "radio", ou apenas "{nome}" nos
  demais casos. """  
  return html_input_IMP.gera(rotulo, tipo, nome, val_ini, val_min, editavel, obrigatorio, dica, cmd)
