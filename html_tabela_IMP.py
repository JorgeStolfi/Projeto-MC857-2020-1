def gera(linhas):
  html_tab = "<table>\n"
  for lin in linhas:
    html_lin = "<tr>\n"
    for el in lin:
      html_el = "<td>" + el + "</td>\n"
      html_lin += html_el
    html_lin += "</tr>\n"
    html_tab += html_lin
  html_tab += "</table>"
  return html_tab
