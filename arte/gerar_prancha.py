from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

root=Path(r'C:\Users\Home\Documents\ChatGPT\prospecção\output\artezanal-jardim-camburi-conceito')
art=root/'arte'
W,H=1920,1420
bg='#f4f1e9'; paper='#fffdf8'; green='#183c32'; dark='#102c25'; ink='#1d2c25'; muted='#6b746c'; line='#d8d5cb'; gold='#d4a652'; clay='#9c5639'
im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
def font(name,size):
    path={'serif':r'C:\Windows\Fonts\georgia.ttf','serifbold':r'C:\Windows\Fonts\georgiab.ttf','sans':r'C:\Windows\Fonts\segoeui.ttf','sansbold':r'C:\Windows\Fonts\segoeuib.ttf'}[name]
    return ImageFont.truetype(path,size)
def text(x,y,s,size=20,color=ink,name='sans'):
    d.text((x,y),s,font=font(name,size),fill=color)
def crop_cover(src,w,h):
    src=src.convert('RGB'); sw,sh=src.size; scale=max(w/sw,h/sh); src=src.resize((int(sw*scale),int(sh*scale)),Image.Resampling.LANCZOS); x=(src.width-w)//2; y=(src.height-h)//2; return src.crop((x,y,x+w,y+h))
def rounded_mask(size,r):
    mask=Image.new('L',size,0); ImageDraw.Draw(mask).rounded_rectangle((0,0,size[0]-1,size[1]-1),radius=r,fill=255); return mask
def place_rounded(src,xywh,r=8):
    x,y,w,h=xywh; tile=crop_cover(src,w,h); mask=rounded_mask((w,h),r); im.paste(tile,(x,y),mask)
# top identity
# brand mark
d.ellipse((80,56,128,104),outline=green,width=2); d.text((95,60),'A',font=font('serif',30),fill=green)
text(143,61,'ARTEZANAL FUNCIONAL',16,green,'sansbold'); text(143,84,'JARDIM CAMBURI · VITÓRIA, ES',9,muted)
text(1515,73,'PRÉVIA CONCEITUAL  ·  CARDÁPIO DIGITAL',10,ink,'sansbold')
d.line((80,124,1840,124),fill=line,width=1)
text(80,158,'Uma vitrine feita para',56,ink,'serif'); text(80,220,'acolher.',56,green,'serif')
text(1115,178,'56 itens organizados por categoria,',18,muted,'sans'); text(1115,210,'ingredientes, preços e contato direto.',18,muted,'sans')
# Laptop outer shadow and frame
laptop=(70,328,1084,720); x,y,w,h=laptop
d.rounded_rectangle((x+8,y+12,x+w+8,y+h+14),radius=22,fill='#dcd8cd')
d.rounded_rectangle((x,y,x+w,y+h),radius=20,fill='#182c26')
screen=Image.open(art/'artezanal-desktop-hero.png')
# capture screen image to 1040x693 ratio
tw,th=1040,693
screen=crop_cover(screen,tw,th); im.paste(screen,(x+22,y+22),rounded_mask((tw,th),7))
d.rounded_rectangle((x+22,y+22,x+22+tw,y+22+th),radius=7,outline='#31463e',width=1)
# laptop base
d.polygon([(x-32,y+h-5),(x+w+30,y+h-5),(x+w+88,y+h+28),(x-88,y+h+28)],fill='#d5d0c5')
d.rounded_rectangle((x+420,y+h+3,x+670,y+h+10),radius=4,fill='#b6b1a7')
# Tablet on right, slightly over desktop
bx,by,bw,bh=1225,334,424,574
d.rounded_rectangle((bx+8,by+10,bx+bw+8,by+bh+10),radius=24,fill='#d8d4ca')
d.rounded_rectangle((bx,by,bx+bw,by+bh),radius=23,fill='#17251f')
tablet=Image.open(art/'artezanal-tablet-cardapio.png')
# crop scrollbar, preserve tall visible interface
if tablet.width>804: tablet=tablet.crop((0,0,804,tablet.height))
place_rounded(tablet,(bx+14,by+22,bw-28,bh-44),7)
d.ellipse((bx+bw//2-3,by+8,bx+bw//2+3,by+14),fill='#738077')
# phone overlaps tablet, crop scrollbar and place in portrait
gx,gy,gw,gh=1565,660,267,560
d.rounded_rectangle((gx+8,gy+10,gx+gw+8,gy+gh+10),radius=34,fill='#d4d0c6')
d.rounded_rectangle((gx,gy,gx+gw,gy+gh),radius=34,fill='#10231d')
phone=Image.open(art/'artezanal-mobile.png')
if phone.width>375: phone=phone.crop((0,0,375,phone.height))
place_rounded(phone,(gx+9,gy+13,gw-18,gh-26),24)
d.rounded_rectangle((gx+95,gy+10,gx+172,gy+19),radius=5,fill='#10231d')
# Section caption / proof points
text(80,1135,'UM CARDÁPIO MAIS FÁCIL DE EXPLORAR',10,clay,'sansbold')
d.line((80,1162,1840,1162),fill=line,width=1)
columns=[(80,'01  ·  DESCOBERTA','Busca, categorias e 56 itens distintos.'),(680,'02  ·  CUIDADO','Avisos de ingredientes e alergênicos.'),(1280,'03  ·  CONTATO','WhatsApp por item e localização no Maps.')]
for x,label,body in columns:
    text(x,1184,label,10,green,'sansbold'); text(x,1212,body,14,muted,'sans')
d.line((80,1280,1840,1280),fill=line,width=1)
text(80,1304,'Fotos reais extraídas do cardápio enviado pela loja. Valores sujeitos a confirmação.',10,muted)
text(1430,1304,'ARTEZANAL FUNCIONAL  ·  CONCEITO DIGITAL',9,green,'sansbold')
out=art/'prancha-artezanal.png'
im.save(out,optimize=True)
print(out, out.stat().st_size)
