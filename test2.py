
import requests
import base64
  
r = requests.get('https://cat726.github.io')

key_1 = "知"
key_2 = "少"
end_char = '">'
f=base64.encode("e")
print(f)
def key_get(key_n):
    key_entry = ''
    for i in range(len(r.text)):
        if r.text[i] == key_n:
            c = 0
            while True:
                if r.text[i+c+1] == '"':
                    esc_char = r.text[i+c+1] + r.text[i+c+2]
                    if esc_char == end_char:
                        break
                c += 1
                key_entry += r.text[i+c]
            return str(key_entry[1:])

#start
a = input("enter key: ")
if a == key_get(key_1):
    print("success")
    print(key_get(key_2))
else:
    print("error")
