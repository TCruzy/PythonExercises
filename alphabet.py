geo = " ააბბგგდდეევვზთიიკკლლმმნნოოპპჟრსტუუფფქქღყყშჩცძწჭხხჯჰჰ?.,!;:()1234567890-=+_'\"`~”\n"
eng = " aAbBgGdDeEvVzTiIkKlLmMnNoOpPJrstuUfFqQRyYSCcZwWxXjhH?.,!;:()1234567890-=+_'\"`~”\n"
in_geo = []
in_eng = []
for i in geo:
    in_geo.append(i)
for i in eng:
    in_eng.append(i)
text = """iyo arabeTs rostevan mefe RvTisagan sviani."""
def translate_to_ge(text):
    translated_string = ""

    for i in range(len(text)):
        translated_string += str(in_geo[eng.index(text[i])])
    return text + "\n\n" + translated_string

print(translate_to_ge(text))