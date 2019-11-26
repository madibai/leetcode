import requests
#from test import srv
import json
from collections import Counter


#def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
#    server_address = ('', 8000)
#    httpd = server_class(server_address, handler_class)
#    httpd.serve_forever()

def conn1c():
    #URL = "https://httpbin.org/get"
    URL  = "http://10.7.10.153/Test/hs/TestURL"
    try:
        r = requests.get(URL)
        print('connected')
        #data = r.json()
        print(r.text)
    except Exception as e:
        print(e)
    finally:
        print('end')

    #for i in data:
    #    print(i)

def checkjson():
    #a = open("document.json")
    x = '{"selling":{"amount": "123","number": "1","date": "25-11-2019","items":[{"name":"bolty","amount":"121"},{"name":"gaiki","amount":"22"},{"name":"gvozdi","amount":"333"}]}}'
    d = json.loads(x)
    #d2 = json.loads(d['selling'])
    print(d['selling']['date'])
def leetcode3():
    s = "pwwkew"
    print(s[::-1])
    print(s[::-1][1::2])
    str_list = []
    max_length = 0
    for i in s:
        if i in str_list:
            str_list = str_list[str_list.index(i)+1:]
        str_list.append(i)
        max_length = max(max_length, len(str_list))
    print(max_length)

def leetcode5(s):
    max_length = ""
    for i in range(len(s)):
        j = i + 1
        while j <= len(s):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(max_length):
                max_length = s[i:j]
            j += 1
    return max_length

def leetcode516(s):
    max_length = ""
    c = Counter(s)

    return c.most_common(1)[0][1]

def longestPalindromeSubseq(s):
    d = {}
    def f(s):
        if s not in d:
            maxL = 0
            for c in set(s):
                i, j = s.find(c), s.rfind(c)
                maxL = max(maxL, 1 if i == j else 2 + f(s[i + 1:j]))
            d[s] = maxL
        return d[s]
    return f(s)


def leetcode(s):
    def bt(start, current):
        if len(current) == 4:
            if start == len(s):
                result.append('.'.join(current))
            return
        for i in range(start + 1, min(start + 4, len(s) + 1)):
            if i - 1 > start and s[start] == '0':
                continue
            a = s[start:i]
            if 0 <= int(a) <= 255:
                current.append(a)
                bt(i, current)
                current.pop()
    result = []
    bt(0, [])
    return result

if __name__ == '__main__':
    #leetcode3()
    #print(leetcode5("babad"))
    #print(leetcode516("asdasdasdaaaaasdd"))
    #print(longestPalindromeSubseq("asdasdasdaaaaasdd"))
    print(leetcode("25525511133"))


    #print('asdasd')
    #conn1c()
    #srv()
    #checkjson()