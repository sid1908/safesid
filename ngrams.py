import re
text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

# regex removing link
text = re.findall(r'^|\@+',tweet.full_text, flags=0)