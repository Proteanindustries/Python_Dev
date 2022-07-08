import re

pattern = re.compile(r"(^[a-zA-z0-9_.+-]'+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'Stephen'
pattern2 = re.compile(r"^[A-za-z0-9$%#@]{8,}\d")
password = 'dsafhJl432$%%%@9'

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)
