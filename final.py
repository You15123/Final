import pyxel

pyxel.init(200, 200)


enemies = []
bullets = []

#class player():

#class bullet():
#class enemy():


class App():
    def __init__(self):
        pyxel.load('map.pyxres')     # pyxel editorで指定した名前+'.pyxres' を読み込む
        pyxel.run(self.update, self.draw)
    def update(self):
        ()

    def draw(self):
       pyxel.cls(0)
       #タイルマップの描画
       pyxel.bltm(0,0,0,0,0,128,128)

App()



