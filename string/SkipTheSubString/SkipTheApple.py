s = "asnghaapplemdsbabapple"

def f(s):
    if len(s)==0:
        return "a"
    if s.startswith('apple'):
        return f(s[5:])
    else:
        return s[0]+f(s[1:])

print(f(s))