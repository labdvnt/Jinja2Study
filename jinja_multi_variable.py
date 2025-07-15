from jinja2 import Template

sablon_metni = """
Merhaba {{ isim }}!
Senin yaşin {{ yas }}.
Bugün {{ sehir }} şehrindesin.
"""

sablon = Template(sablon_metni)

veri = {
    "isim": "Ömer",
    "yas": 30,
    "sehir": "İstanbul"
}

cikti = sablon.render(veri)
print(cikti)