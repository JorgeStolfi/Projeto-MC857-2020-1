from datetime import datetime, timezone

def gera():
  nowraw = datetime.now(timezone.utc)
  nowfmt = nowraw.strftime("%Y-%m-%d %H:%M:%S %z")
  return \
    "  <div>\n" + \
    "    <small><p>Página criada em " + nowfmt + "</p></small>\n" + \
    "  </div>\n" + \
    "  </body>\n" + \
    "</html>\n"
