import base64
from Crypto.Cipher import AES
import string
emojisInit="🍎🍌🏎🚪👁👣😀🖐ℹ😂🥋✉🚹🌉👌🍍👑👉🎤🚰☂🐍💧✖☀🦓🏹🎈😎🎅🐘🌿🌏🌪☃🍵🍴🚨📮🕹📂🛩⌨🔄🔬🐅🙃🐎🌊🚫❓⏩😁😆💵🤣☺😊😇😡🎃😍✅🔪🗒"
alpha = string.ascii_lowercase+string.ascii_uppercase+string.digits+"+/="
a = "🙃💵🌿🎤🚪🌏🐎🥋🚫😆✅🍍🎤🐘🌏ℹ⌨😍🎈✉🤣🛩🍌🚪🍴ℹ☺🚹❓🍴🔬🌪🍵👣🔄☃👌😎👌🔄👌🔪🍌👁🍍🍌🌏🎃🚰🍵🐍🎅✅🍍🦓😎😊🤣🏹🍍💧🔄🔄🤣👁🥋🚫☺🍴😁🚫😇🚰⏩😍🌿💵🦓😇🛩✖🕹🐎📂📂💧🗒🗒"
base64data = ""
for i in a:
    base64data += alpha[emojisInit.index(i)]
print(base64data) #最后还要AES解密