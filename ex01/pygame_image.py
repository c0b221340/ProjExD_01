import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imglst = []
    for i in range(10):
        kk_imglst.append(pg.transform.rotozoom(kk_img, i, 1.0))
    for i in range(10,0,-1):
        kk_imglst.append(pg.transform.rotozoom(kk_img, i, 1.0))


    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600 - x, 0])
        screen.blit(bg_img, [3200 - x, 0])
        screen.blit(kk_imglst[tmr % 20],[300,200])
        pg.display.update()
        print(x)
        tmr += 1
        x += 1
        if x > 3200 :
            x = 0
        

        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()