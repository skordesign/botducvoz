
txt = """[IMG]https://2.pik.vn/201927169705-2868-4004-b385-a52fd49356d2.png[/IMG]
Loại này """

start = '[IMG]'
end = '[/IMG]'
while txt.find(start) != -1:
    t = txt[txt.find(start)+len(start):txt.find(end)]
    txt = txt.replace('[IMG]{}[/IMG]'.format(t), '[URL="{}"]Ảnh[/URL]'.format(t))

print(txt)

