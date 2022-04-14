def determine_initials(name):
    names=name.split()
    result=""
    for s in names:
        result+=(s[0]+".")
    return result

name_list= ["Peter Gene Hernandez", "Steveland Judkins", "Norma JeanMortensen", "Ramon Antonio Gerard Estevez", "Declan Patrick McManus"]

for name in name_list:
    print(determine_initials(name))
