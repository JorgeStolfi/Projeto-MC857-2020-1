def gera(linhas):
  ht_tab = "<table>\n"
  for lin in linhas:
    ht_lin = "<tr>\n"
    for el in lin:
      ht_el = "<td>" + el + "</td>\n"
      ht_lin += ht_el
    ht_lin += "</tr>\n"
    ht_tab += ht_lin
  ht_tab += "</table>"
  return ht_tab
