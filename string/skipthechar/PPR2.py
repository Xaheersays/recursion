upr= "absndbaaanaaamhds"
def f(processed_Str , unprocessed_str):
    if len(unprocessed_str) == 0:
        print(processed_Str)
        return
    ch = unprocessed_str[0]
    if ch == 'a':
        f(processed_Str,unprocessed_str[1:])
    else:
        processed_Str+=ch
        f(processed_Str,unprocessed_str[1:])

f('',upr)

