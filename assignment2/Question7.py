def display_with_dash(s):
    for i in range(len(s)-1):
        print(s[i],end="-")
    print(s[len(s)-1])
words = ['Elvis', 'has', 'left', 'the', 'building!']
for s in words:
    display_with_dash(s)