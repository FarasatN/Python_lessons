# import re
# >>> re.search("Sinan","Merhaba ben Sinan, senin adın nedir?")
# <_sre.SRE_Match object; span=(12, 17), match='Sinan'>
#
# >>> metin = "Merhaba ben Sinan, senin adın nedir?"
# >>> metin[12:17]
# 'Sinan'
#
# >>> kontrol = re.search("Sinan","Merhaba ben Sinan, senin adın nedir?")
# >>> kontrol.start()
# 12

# >>> kontrol = re.search("Sinan","Merhaba ben Sinan, senin adın nedir?")
# >>> kontrol.end()
# 17

# >>> metin = "Merhaba ben Sinan, senin adın nedir?"
# >>> kontrol = re.search("Sinan",metin)
# >>> kontrol.endpos
# 36
# >>> metin[:36]
# 'Merhaba ben Sinan, senin adın nedir?'

# >>> print(re.findall("zaman","Tam zamanında geldin, sensiz zaman geçmiyor"))
# ['zaman', 'zaman']

# >>> print(len(re.findall("zaman","Tam zamanında geldin, sensiz zaman geçmiyor")))
# 2

# ....
#
# metakarakterler ve s. ...
