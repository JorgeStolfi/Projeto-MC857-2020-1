#! /usr/bin/python3

import html_label
from html_label import gera

from utils_testes import testa_gera_html as testa
import sys

testa(html_label, gera, "elemento_label_1", True, False, "Banana", " --> ")
