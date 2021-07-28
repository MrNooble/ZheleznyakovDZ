original_text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
final_text = []
for i in original_text:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            final_text.append(f"'{int(i):02}'")
        else:
            final_text.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        final_text.append(i)
print(" ".join(final_text))
