import locale

with open("msg.txt", "rb") as fp:
    content = fp.readline()
    print(content, type(content))
    print(content.decode("utf-8"))

print("---" * 10)

with open("msg.txt", "r") as fp:
    content = fp.readline()
    print(content, type(content))

print("---" * 10)

print(locale.getpreferredencoding())
print(locale.locale_encoding_alias)

print("---" * 10)

with open("msg.txt", "r", encoding="utf-8") as fp:
    content = fp.readline()
    print(content, type(content))

print("---" * 10)

with open("msg.txt", "r", encoding="gb2312") as fp:
    content = fp.readline()
    print(content, type(content))


"""
$ python 08.py
b'\xe7\x9c\x8b\xe5\x88\xb0\xe8\xbf\x99\xe9\x87\x8c\xe4\xba\x86\xef\xbc\x8c\xe7\x82\xb9\xe4\xb8\xaa\xe5\x85\xb3\xe6\xb3\xa8\xe5\x90\xa7\n' <class 'bytes'>
看到这里了，点个关注吧

------------------------------
看到这里了，点个关注吧
 <class 'str'>
------------------------------
UTF-8
{'437': 'C', 'c': 'C', 'en': 'ISO8859-1', 'jis': 'JIS7', 'jis7': 'JIS7', 'ajec': 'eucJP', 'koi8c': 'KOI8-C', 'microsoftcp1251': 'CP1251', 'microsoftcp1255': 'CP1255', 'microsoftcp1256': 'CP1256', '88591': 'ISO8859-1', '88592': 'ISO8859-2', '88595': 'ISO8859-5', '885915': 'ISO8859-15', 'ascii': 'ISO8859-1', 'latin_1': 'ISO8859-1', 'iso8859_1': 'ISO8859-1', 'iso8859_10': 'ISO8859-10', 'iso8859_11': 'ISO8859-11', 'iso8859_13': 'ISO8859-13', 'iso8859_14': 'ISO8859-14', 'iso8859_15': 'ISO8859-15', 'iso8859_16': 'ISO8859-16', 'iso8859_2': 'ISO8859-2', 'iso8859_3': 'ISO8859-3', 'iso8859_4': 'ISO8859-4', 'iso8859_5': 'ISO8859-5', 'iso8859_6': 'ISO8859-6', 'iso8859_7': 'ISO8859-7', 'iso8859_8': 'ISO8859-8', 'iso8859_9': 'ISO8859-9', 'iso2022_jp': 'JIS7', 'shift_jis': 'SJIS', 'tactis': 'TACTIS', 'euc_jp': 'eucJP', 'euc_kr': 'eucKR', 'utf_8': 'UTF-8', 'koi8_r': 'KOI8-R', 'koi8_t': 'KOI8-T', 'koi8_u': 'KOI8-U', 'kz1048': 'RK1048', 'cp1251': 'CP1251', 'cp1255': 'CP1255', 'cp1256': 'CP1256', 'eucjp': 'eucJP', 'euckr': 'eucKR', 'iso2022jp': 'JIS7', 'iso88591': 'ISO8859-1', 'iso885910': 'ISO8859-10', 'iso885911': 'ISO8859-11', 'iso885913': 'ISO8859-13', 'iso885914': 'ISO8859-14', 'iso885915': 'ISO8859-15', 'iso885916': 'ISO8859-16', 'iso88592': 'ISO8859-2', 'iso88593': 'ISO8859-3', 'iso88594': 'ISO8859-4', 'iso88595': 'ISO8859-5', 'iso88596': 'ISO8859-6', 'iso88597': 'ISO8859-7', 'iso88598': 'ISO8859-8', 'iso88599': 'ISO8859-9', 'koi8r': 'KOI8-R', 'koi8t': 'KOI8-T', 'koi8u': 'KOI8-U', 'latin1': 'ISO8859-1', 'shiftjis': 'SJIS', 'utf8': 'UTF-8'}
------------------------------
看到这里了，点个关注吧
 <class 'str'>
------------------------------
Traceback (most recent call last):
  File "/python3-standard-library-example/source/39_str_bytes/08.py", line 28, in <module>
    content = fp.readline()
UnicodeDecodeError: 'gb2312' codec can't decode byte 0xe7 in position 0: illegal multibyte sequence
$
"""
