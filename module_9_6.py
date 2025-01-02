def all_variants(text):
    for l in range(len(text)):
        for r in range(l, len(text)):
            yield text[l:r+1]

a = all_variants("abc")

for i in a:
    print(i)