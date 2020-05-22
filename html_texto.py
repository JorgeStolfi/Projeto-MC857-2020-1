import html_texto_IMP

def gera(texto, disp, fam_fonte, tam_fonte, peso_fonte, pad, halign, cor_texto, cor_fundo):
  """Retorna un string que é um fragmento HTML consistindo do {texto}
  dado, que pode conter tags de HTML (como '<b>', '<i>') e quebras de
  linha ('<br/>'). O fragmento todo é um domínio  {span(estilo,texto)}
  com o {estilo} apropriado.
  
  O parâmetro {disp} é o valor do atributo 'display' do estilo, por exemplo 
  'block' ou 'inline-block'. 

  Os parâmetros {fam_fonte}, {tam_fonte} e {peso_fonte} especificam a família e o
  tamanho do fonte a usar (por exemplo 'Helvetica','18px','bold').

  O parâmetro {pad}, especifica a largura do espaço extra ('padding') em
  volta do texto como um todo.

  O parâmetro {halign} especifica o alinhamento das linhas do texto;
  pode ser 'left', 'center', ou 'right'.

  Os parâmetros {cor_texto} e {cor_fundo} devem ser cores aceitáveis no
  CSS (por exemplo, '#ff8800').

  Cada parâmetro de estilo pode ser {None} para indicar a omissão
  do atributo no estilo. O atributo então herda o defô
  do contexto ou de especificações de estilo CSS globais."""
  return html_texto_IMP.gera(texto, disp, fam_fonte, tam_fonte, peso_fonte, pad, halign, cor_texto, cor_fundo)
