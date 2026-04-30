import pygame
import random
import sys

pygame.init()

# 🎨 Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BROWN = (160, 82, 45)
GREEN = (0, 200, 0)
RED = (220, 20, 20)
BLUE = (30, 144, 255)
YELLOW = (255, 215, 0)
SILVER = (192, 192, 192)

# 📐 Kích thước
SCREEN_WIDTH = 520
SCREEN_HEIGHT = 520
TILE_SIZE = 20
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🎮 Battle City - Xe Tăng Cổ Điển")
clock = pygame.time.Clock()

# 🔫 Hướng
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, owner):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.speed = 6
        self.owner = owner
        
    def update(self):
        if self.direction == UP:
            self.rect.y -= self.speed
        elif self.direction == DOWN:
            self.rect.y += self.speed
        elif self.direction == LEFT:
            self.rect.x -= self.speed
        elif self.direction == RIGHT:
            self.rect.x += self.speed
            
        if (self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or
            self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT):
            self.kill()

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, color, is_player=False):
        super().__init__()
        self.size = 16  # Giảm kích thước cho dễ di chuyển
        self.color = color
        self.is_player = is_player
        self.direction = UP
        self.speed = 2 if is_player else 1
        self.cooldown = 0
        self.start_pos = (x, y)
        
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.update_image()
        
    def set_direction(self, new_dir):
        if self.direction != new_dir:
            self.direction = new_dir
            self.update_image()
            
    def update_image(self):
        self.image.fill((0, 0, 0, 0))  # Trong suốt
        
        # Vẽ thân xe
        pygame.draw.rect(self.image, self.color, (2, 2, 12, 12))
        
        # Vẽ bánh xích
        pygame.draw.rect(self.image, GRAY, (0, 1, 3, 14))
        pygame.draw.rect(self.image, GRAY, (13, 1, 3, 14))
        
        # Vẽ nòng súng theo hướng
        if self.direction == UP:
            pygame.draw.rect(self.image, self.color, (6, 0, 4, 5))
        elif self.direction == DOWN:
            pygame.draw.rect(self.image, self.color, (6, 11, 4, 5))
        elif self.direction == LEFT:
            pygame.draw.rect(self.image, self.color, (0, 6, 5, 4))
        elif self.direction == RIGHT:
            pygame.draw.rect(self.image, self.color, (11, 6, 5, 4))
            
    def move(self, dx, dy, walls):
        old_x = self.rect.x
        old_y = self.rect.y
        
        # Di chuyển từng trục riêng để dễ xử lý va chạm
        self.rect.x += dx
        hits_walls = False
        
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                hits_walls = True
                break
                
        if hits_walls or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.rect.x = old_x
            
        self.rect.y += dy
        hits_walls = False
        
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                hits_walls = True
                break
                
        if hits_walls or self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.rect.y = old_y
            
    def shoot(self):
        if self.cooldown == 0:
            self.cooldown = 25
            cx, cy = self.rect.centerx, self.rect.centery
            
            if self.direction == UP:
                return Bullet(cx, self.rect.top, UP, self)
            elif self.direction == DOWN:
                return Bullet(cx, self.rect.bottom, DOWN, self)
            elif self.direction == LEFT:
                return Bullet(self.rect.left, cy, LEFT, self)
            elif self.direction == RIGHT:
                return Bullet(self.rect.right, cy, RIGHT, self)
        return None
        
    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1

class Enemy(Tank):
    def __init__(self, x, y):
        super().__init__(x, y, RED, False)
        self.direction = random.choice([DOWN, LEFT, RIGHT])
        self.move_timer = 0
        self.update_image()
        
    def ai_move(self, walls, player):
        self.move_timer += 1
        
        # Thay đổi hướng ngẫu nhiên hoặc khi va chạm
        if self.move_timer > 60 or random.random() < 0.02:
            old_dir = self.direction
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
            
            # Thử di chuyển theo hướng mới
            test_x, test_y = self.rect.x, self.rect.y
            if self.direction == UP:
                test_y -= 2
            elif self.direction == DOWN:
                test_y += 2
            elif self.direction == LEFT:
                test_x -= 2
            elif self.direction == RIGHT:
                test_x += 2
                
            # Nếu hướng mới bị chặn, quay lại hướng cũ
            test_rect = pygame.Rect(test_x, test_y, self.size, self.size)
            blocked = False
            for wall in walls:
                if test_rect.colliderect(wall.rect):
                    blocked = True
                    break
                    
            if blocked:
                self.direction = old_dir
            self.move_timer = 0
            
        # Di chuyển
        if self.direction == UP:
            self.move(0, -self.speed, walls)
        elif self.direction == DOWN:
            self.move(0, self.speed, walls)
        elif self.direction == LEFT:
            self.move(-self.speed, 0, walls)
        elif self.direction == RIGHT:
            self.move(self.speed, 0, walls)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, wall_type="brick"):
        super().__init__()
        self.wall_type = wall_type
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        
        if wall_type == "brick":
            self.image.fill(BROWN)
            for i in range(0, TILE_SIZE, 5):
                pygame.draw.line(self.image, (80, 40, 20), (0, i), (TILE_SIZE, i))
            for i in range(0, TILE_SIZE, 10):
                pygame.draw.line(self.image, (80, 40, 20), (i, 0), (i, TILE_SIZE))
        elif wall_type == "steel":
            self.image.fill(SILVER)
            pygame.draw.rect(self.image, WHITE, (2, 2, 16, 16), 2)
        elif wall_type == "water":
            self.image.fill(BLUE)
        elif wall_type == "grass":
            self.image.fill(GREEN)
        elif wall_type == "base":
            self.image.fill(BLACK)
            pygame.draw.polygon(self.image, YELLOW, [(10, 2), (2, 18), (18, 18)])
            
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Game:
    def __init__(self):
        self.reset_game()
        
    def reset_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        
        self.create_map()
        
        # Spawn player ở vị trí an toàn - bên trái base
        self.player = Tank(200, 480, GREEN, True)
        self.all_sprites.add(self.player)
        
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.win = False
        self.enemy_spawn_timer = 0
        self.enemies_destroyed = 0
        self.total_enemies = 20
        
    def create_map(self):
        # 0 = empty, 1 = brick, 2 = steel, 3 = water, 4 = grass, 5 = base
        map_layout = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0],
            [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0],
            [0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0],
            [0,1,1,0,0,1,1,0,0,1,2,1,0,0,1,2,1,0,0,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
            [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
            [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
            [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
            [0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0],
            [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
            [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
            [0,0,0,0,0,0,0,0,0,1,1,1,3,3,1,1,1,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
            [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
            [0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0],
            [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
            [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
            [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,5,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        
        for row in range(len(map_layout)):
            for col in range(len(map_layout[0])):
                tile = map_layout[row][col]
                x = col * TILE_SIZE
                y = row * TILE_SIZE
                
                if tile == 1:
                    wall = Wall(x, y, "brick")
                elif tile == 2:
                    wall = Wall(x, y, "steel")
                elif tile == 3:
                    wall = Wall(x, y, "water")
                elif tile == 5:
                    wall = Wall(x, y, "base")
                    self.base = wall
                else:
                    continue
                    
                self.walls.add(wall)
                self.all_sprites.add(wall)
        
    def spawn_enemy(self):
        spawn_points = [(0, 0), (240, 0), (480, 0)]
        if len(self.enemies) < 4 and self.enemies_destroyed + len(self.enemies) < self.total_enemies:
            x, y = random.choice(spawn_points)
            enemy = Enemy(x, y)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
            
    def run(self):
        running = True
        font = pygame.font.Font(None, 32)
        small_font = pygame.font.Font(None, 22)
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.game_over:
                        self.reset_game()
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if not self.game_over and event.key == pygame.K_SPACE:
                        bullet = self.player.shoot()
                        if bullet:
                            self.bullets.add(bullet)
                            self.all_sprites.add(bullet)
            
            if not self.game_over:
                keys = pygame.key.get_pressed()
                
                # Di chuyển người chơi
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.player.set_direction(UP)
                    self.player.move(0, -self.player.speed, self.walls)
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.player.set_direction(DOWN)
                    self.player.move(0, self.player.speed, self.walls)
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.player.set_direction(LEFT)
                    self.player.move(-self.player.speed, 0, self.walls)
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.player.set_direction(RIGHT)
                    self.player.move(self.player.speed, 0, self.walls)
                    
                # Spawn địch
                self.enemy_spawn_timer += 1
                if self.enemy_spawn_timer > 120:
                    self.spawn_enemy()
                    self.enemy_spawn_timer = 0
                    
                # AI địch
                for enemy in self.enemies:
                    enemy.ai_move(self.walls, self.player)
                    if random.random() < 0.02:
                        bullet = enemy.shoot()
                        if bullet:
                            self.enemy_bullets.add(bullet)
                            self.all_sprites.add(bullet)
                            
                # Cập nhật
                self.all_sprites.update()
                
                # Đạn người chơi
                for bullet in self.bullets:
                    wall_hit = pygame.sprite.spritecollide(bullet, self.walls, False)
                    if wall_hit:
                        wall = wall_hit[0]
                        if wall.wall_type == "brick":
                            wall.kill()
                        bullet.kill()
                        continue
                        
                    enemy_hit = pygame.sprite.spritecollide(bullet, self.enemies, True)
                    if enemy_hit:
                        bullet.kill()
                        self.score += 100
                        self.enemies_destroyed += 1
                        continue
                        
                # Đạn địch
                for bullet in self.enemy_bullets:
                    if pygame.sprite.collide_rect(bullet, self.player):
                        bullet.kill()
                        self.lives -= 1
                        if self.lives <= 0:
                            self.game_over = True
                        else:
                            self.player.rect.topleft = self.player.start_pos
                        continue
                        
                    wall_hit = pygame.sprite.spritecollide(bullet, self.walls, False)
                    if wall_hit:
                        wall = wall_hit[0]
                        if wall.wall_type == "brick":
                            wall.kill()
                        elif wall.wall_type == "base":
                            self.game_over = True
                        bullet.kill()
                        continue
                        
                # Kiểm tra thắng
                if self.enemies_destroyed >= self.total_enemies:
                    self.win = True
                    self.game_over = True
                    
            # 🎨 Vẽ
            screen.fill(BLACK)
            self.all_sprites.draw(screen)
            
            # UI
            score_text = font.render(f"Score: {self.score}", True, WHITE)
            lives_text = font.render(f"Lives: {self.lives}", True, WHITE)
            enemies_text = small_font.render(f"Enemies: {self.enemies_destroyed}/{self.total_enemies}", True, WHITE)
            screen.blit(score_text, (10, 10))
            screen.blit(lives_text, (10, 45))
            screen.blit(enemies_text, (10, 80))
            
            if self.game_over:
                if self.win:
                    msg = font.render("YOU WIN! Press R", True, GREEN)
                else:
                    msg = font.render("GAME OVER! Press R", True, RED)
                screen.blit(msg, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2))
                
            pygame.display.flip()
            clock.tick(FPS)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()