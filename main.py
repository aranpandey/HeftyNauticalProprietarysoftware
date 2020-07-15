import pygame
pygame.init()
screen_info=pygame.display.Info()
print(screen_info)
size=(width,height)=(screen_info.current_w,screen_info.current_h)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
color= (30,0,30)
Player = Ship()
def main():
  
  while True:
    clock.tick(60)
    screen.fill(color)
    screen.blit(Player.image, Player.rect)
    pygame.display.flip()
if __name__=='__main__':
  main()