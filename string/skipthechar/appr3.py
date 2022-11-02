upr= "absndbaaanaaamhds"
def f(unprocessed_str):
    if len(unprocessed_str)==0:
        return  ""
    ch = unprocessed_str[0]
    if ch != 'a':
        return ch+f(unprocessed_str[1:])
    else:
        return  f(unprocessed_str[1:])
print(f(upr))

    #this is good way
    