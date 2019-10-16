
txt = """[QUOTE=Kcbv''Yel Butter;154408597][IMG]https://imgur.com/syDQHdr.jpg[/IMG][IMG]https://imgur.com/0isoxMB.jpg[/IMG][IMG]https://imgur.com/fCdeN7L.jpg[/IMG]

[URL="https://twitter.com/nakamanian/status/1182450674761519104"]Sóng đánh sát bờ.[/URL][/QUOTE]"""

start = '[IMG]'
end = '[/IMG]'
while txt.find(start) != -1:
    t = txt[txt.find(start)+len(start):txt.find(end)]
    txt = txt.replace('[IMG]{}[/IMG]'.format(t), '[URL="{}"]Ảnh[/URL]'.format(t))

print(txt)

