txt_fl1 = open('first_textfl.text', 'w+')
txt_fl1.write(
    "is simply dummy text of the printing and typesetting industry.\n Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. \n It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,\n  and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet.")

txt_fl1.close()

txt_fl2 = open('scnd_textfl.text', 'w+')
txt_fl2.write(
    "Contrary to popular belief, Lorem Ipsum is not simply random text.\n It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.\n Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance.\n The first line of Lorem Ipsum, amet... It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc")
txt_fl2.close()

txt_fl1 = open('first_textfl.text', 'r')
x = txt_fl1.read()
x_l = list(x.split())
txt_fl1.close()
print(x)
print("\n")
txt_fl2 = open('scnd_textfl.text', 'r')
y = txt_fl2.read()
y_l = list(y.split())
print(y)

txt_fl2.close()

common = []
for i in range(0, len(x_l)):
    if x_l[i] in y_l:
        common.append(x_l[i])
print(common)
str = str(common)
txt_fl3 = open('common.text', 'w')
for i in common :
    txt_fl3.write(i+",")
