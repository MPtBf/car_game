import pygame as pg
from setts import *

pg.init()
pg.font.init()

sc = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Работа с изображениями')
clock = pg.time.Clock()
font1 = pg.font.Font(None,25)


car_img = pg.image.load("images/car.bmp")
car_img.set_colorkey(WHITE)
car_img = pg.transform.scale(car_img,(car_img.get_width()*images_pultiplier,car_img.get_height()*images_pultiplier))
finish_img = pg.image.load("images/finish.png")
finish_img = pg.transform.scale(finish_img,(finish_img.get_width()*images_pultiplier,finish_img.get_height()*images_pultiplier))
bg_img = pg.image.load("images/sand.jpg")
bg_img = pg.transform.scale(bg_img, (bg_img.get_width()*bg_multiplier,bg_img.get_height()*bg_multiplier))

car_rect = car_img.get_rect()
finish_rect = finish_img.get_rect()

car_dir_up = car_img
car_dir_upright = pg.transform.rotate(car_img, -45)
car_dir_right = pg.transform.rotate(car_img, -90)
car_dir_downright = pg.transform.rotate(car_img, -135)
car_dir_down = pg.transform.flip(car_img, True, True)
car_dir_downleft = pg.transform.rotate(car_img, 135)
car_dir_left = pg.transform.rotate(car_img, +90)
car_dir_upleft = pg.transform.rotate(car_img, 45)
car_rect.x = 0
car_rect.y = 0



game = True
while game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False

    sc.fill(BLACK)

    keys = pg.key.get_pressed()

    if keys[pg.K_w] and keys[pg.K_d]:
        car_rect.x += car_speed
        car_rect.y -= car_speed
        car_img = car_dir_upright
    elif keys[pg.K_s] and keys[pg.K_d]:
        car_rect.x += car_speed
        car_rect.y += car_speed
        car_img = car_dir_downright
    elif keys[pg.K_s] and keys[pg.K_a]:
        car_rect.x -= car_speed
        car_rect.y += car_speed
        car_img = car_dir_downleft
    elif keys[pg.K_w] and keys[pg.K_a]:
        car_rect.x -= car_speed
        car_rect.y -= car_speed
        car_img = car_dir_upleft
    elif keys[pg.K_w]:
        car_img = car_dir_up
        car_rect.y -= car_speed
    elif keys[pg.K_d]:
        car_img = car_dir_right
        car_rect.x += car_speed
    elif keys[pg.K_s]:
        car_img = car_dir_down
        car_rect.y += car_speed
    elif keys[pg.K_a]:
        car_img = car_dir_left
        car_rect.x -= car_speed

    # print(car_rect.collidelist(finish_rect))




    sc.blit(bg_img,(0,0))
    sc.blit(car_img,(car_rect.x,car_rect.y))
    sc.blit(finish_img,(WIDTH-finish_img.get_width(),HEIGHT-finish_img.get_height()))


    now_fps = clock.get_fps()
    fps_label = font1.render(f"FPS: {round(now_fps)}", True, DGREEN)
    sc.blit(fps_label, fps_location)

    pg.display.flip()
    clock.tick(FPS)
pg.quit()