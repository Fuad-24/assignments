def capitalize_words(s):
    d=s.split(" ")
    result=""
    for ts in d:
        result+=ts[0].upper()
        for i in range(1,len(ts)):
            result+=ts[i]
        result+=" "
    return result
print(capitalize_words("Why so serious"))