import pygame
pygame.init()

class grid_cell():
    def __init__(self,x,y,cell_width,cell_height,spacing,clicked,color_dead=(0,0,0),color_alive=(255,255,255),alive = False):
        self.clicked = clicked
        self.x = x
        self.y = y
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.alive = alive
        self.color_dead = color_dead
        self.color_alive = color_alive
        self.spacing = spacing
        self.counter =0
    def draw_cell(self):
        if self.alive:
            pygame.draw.rect(win,self.color_alive,(self.x,self.y,self.cell_width,self.cell_height))
        else:
            pygame.draw.rect(win,self.color_dead,(self.x,self.y,self.cell_width,self.cell_height))

    def hover(self,x,y):
        if x >= self.x and x<= self.x+self.cell_width and y >=self.y and y<= self.y+self.cell_height:
            return True

    def draw_x(self):
        #draws x on the cell
        if self.alive:
            pygame.draw.rect(win, self.color_alive, (self.x, self.y, self.cell_width, self.cell_height))
            pygame.draw.line(win, self.color_dead, (self.x, self.y),(self.x+self.cell_width, self.y+self.cell_height),self.spacing)
            pygame.draw.line(win, self.color_dead, (self.x + self.cell_width, self.y),(self.x , self.y + self.cell_height), self.spacing)
        else:
            pygame.draw.rect(win, self.color_dead, (self.x, self.y, self.cell_width, self.cell_height))
            pygame.draw.line(win, self.color_alive, (self.x, self.y), (self.x+self.cell_width, self.y+self.cell_height),self.spacing)
            pygame.draw.line(win, self.color_alive, (self.x + self.cell_width, self.y),(self.x, self.y + self.cell_height), self.spacing)

    def change_life_state(self):
        #changes te life state of cell
        global alive_cells
        if not self.clicked:
            if self.alive:
                self.alive = False
                alive_cells -= 1
            else:
                alive_cells +=1
                self.alive = True

            self.clicked= True


#standard code
WIDTH = HEIGHT = 600
PANEL_SIZE = 200
win = pygame.display.set_mode((WIDTH+PANEL_SIZE,HEIGHT))
pygame.display.set_caption("Game of Life")
CELL_SIZE = 10
SPACING = 1
GREY=(105,105,105)
LIGHT_GREY=(220,220,220)
FONT_SIZE = 80
font = pygame.font.SysFont('dejavuserif',FONT_SIZE)
small_font =  pygame.font.SysFont('dejavuserif',FONT_SIZE//2)


num_cells= int(WIDTH/CELL_SIZE)
matrix=[[0 for i in range(0,num_cells)] for j in range(0,num_cells)]
def init_grid(): #initializes the frid
    global matrix
    for i in range(0,num_cells):
        for j in range(0,num_cells):
            matrix[i][j] = grid_cell(j*(CELL_SIZE-SPACING)+j*SPACING,i*(CELL_SIZE-SPACING)+i*SPACING,(CELL_SIZE-SPACING),(CELL_SIZE-SPACING),SPACING,False,GREY)

def draw_grid(x,y):
    for i in range(0,num_cells):
        for j in range(0,num_cells):
            #draws the X if mouse is hovering over the cell and simulation isnt enabled
            if matrix[i][j].hover(x,y) and not simulate:
                matrix[i][j].draw_x()
            else:
                matrix[i][j].draw_cell()
    draw_panel()


def draw_panel():
    #draws left panel
    pygame.draw.rect(win, LIGHT_GREY, (WIDTH, 0, WIDTH + PANEL_SIZE, HEIGHT))
    text1 = font.render('Game',True,(0,0,0),LIGHT_GREY)
    text1Rect = text1.get_rect()
    text1Rect.center = (WIDTH+PANEL_SIZE//2,FONT_SIZE//2)
    win.blit(text1,text1Rect)

    text2 = font.render('of', True, (0, 0, 0), LIGHT_GREY)
    text2Rect = text2.get_rect()
    text2Rect.center = (WIDTH + PANEL_SIZE // 2, FONT_SIZE +FONT_SIZE//10)
    win.blit(text2, text2Rect)

    text3 = font.render('Life', True, (0, 0, 0), LIGHT_GREY)
    text3Rect = text3.get_rect()
    text3Rect.center = (WIDTH + PANEL_SIZE // 2, FONT_SIZE*2-FONT_SIZE//10 )
    win.blit(text3, text3Rect)

    restrt_text  = small_font.render('R - restart', True, (0, 0, 0), LIGHT_GREY)
    restrt_textRect = restrt_text.get_rect()
    restrt_textRect.center = (WIDTH + PANEL_SIZE // 2, FONT_SIZE*2+FONT_SIZE//2 )
    win.blit(restrt_text,restrt_textRect)

    sim_text = small_font.render('S - start', True, (0, 0, 0), LIGHT_GREY)
    sim_textRect = sim_text.get_rect()
    sim_textRect.center = (WIDTH + PANEL_SIZE // 2, FONT_SIZE * 2 + (FONT_SIZE // 2)*2)
    win.blit(sim_text, sim_textRect)

    ngen_text = small_font.render('A - next gen', True, (0, 0, 0), LIGHT_GREY)
    ngen_textRect = ngen_text.get_rect()
    ngen_textRect.center = (WIDTH + PANEL_SIZE // 2, FONT_SIZE * 2 + (FONT_SIZE // 2) * 3)
    win.blit(ngen_text, ngen_textRect)

    pygame.draw.line(win,(0,0,0),(WIDTH,FONT_SIZE * 2 + (FONT_SIZE // 2) * 4),(WIDTH+PANEL_SIZE,FONT_SIZE * 2 + (FONT_SIZE // 2) * 4),FONT_SIZE//8)

    gen_t = "Gen: "+str(gen)
    gen_text = small_font.render(gen_t, True, (0, 0, 0), LIGHT_GREY)
    gen_textRect = gen_text.get_rect()
    gen_textRect.center = (WIDTH + PANEL_SIZE // 2, FONT_SIZE * 2 + (FONT_SIZE // 2) * 5)
    win.blit(gen_text, gen_textRect)

    alive_t = "Alive cells: "
    alive_text = small_font.render(alive_t,True,(0,0,0),LIGHT_GREY)
    alive_textRect = alive_text.get_rect()
    alive_textRect.center = (WIDTH + PANEL_SIZE // 2, FONT_SIZE * 2 + (FONT_SIZE // 2) * 6)
    win.blit(alive_text,alive_textRect)

    alive_counter_text = small_font.render(str(alive_cells), True, (0, 0, 0), LIGHT_GREY)
    alive_counter_textRect = alive_counter_text.get_rect()
    alive_counter_textRect.center = (WIDTH + PANEL_SIZE // 2, FONT_SIZE * 2 + (FONT_SIZE // 2) * 7)
    win.blit(alive_counter_text, alive_counter_textRect)


def change_state(x,y,bool_state):
    #changes the state, used when the mouse is pressed
    #clicked is used so that the cell life state isnt always changing when the mouse is pressed
    #bool_state is state that cell should be at
    global matrix
    for i in range(0,num_cells):
        for j in range(0,num_cells):
            if matrix[i][j].hover(x, y) :
                if not matrix[i][j].alive == bool_state:
                    matrix[i][j].change_life_state()
            else:
                matrix[i][j].clicked = False

def get_num_of_live_cells(x,y):
    #calculates the number of alive cells around cell
    number_of_live_cells = 0
    if x!=0:
        if matrix[x - 1][y].alive: number_of_live_cells += 1
        if y!=0:
            if matrix[x - 1][y - 1].alive: number_of_live_cells += 1
        if y!=num_cells-1:
            if matrix[x - 1][y + 1].alive: number_of_live_cells += 1
    if y!=0:
        if matrix[x][y - 1].alive: number_of_live_cells += 1
        if x!=num_cells-1:
            if matrix[x + 1][y - 1].alive: number_of_live_cells += 1
    if x!=num_cells-1:
        if matrix[x + 1][y].alive  : number_of_live_cells += 1
        if y!=num_cells-1:
            if matrix[x + 1][y + 1].alive: number_of_live_cells += 1
    if y != num_cells - 1:
        if matrix[x][y + 1].alive: number_of_live_cells += 1

    return  number_of_live_cells


def advance_life():
    #advences to the nex generation; first sets the temporary matrix, so it doesnt interfere with the simulation;
    global matrix,alive_cells
    temp_matrix = [[0 for i in range(0,num_cells)] for j in range(0,num_cells)]

    for i in range(0,num_cells):
        for j in range(0,num_cells):
            num_of_live_cells = get_num_of_live_cells(i,j)
            if matrix[i][j].alive:
                if num_of_live_cells==2 or num_of_live_cells==3:
                    temp_matrix[i][j] = True
                else:
                    temp_matrix[i][j] = False
            else:
                if num_of_live_cells ==3:
                    temp_matrix[i][j] = True
                else:
                    temp_matrix[i][j] = False

    # sets the real matrix based on the temporary
    for i in range(0,num_cells):
        for j in range(0,num_cells):
            if temp_matrix[i][j] == True :
                if not matrix[i][j].alive: alive_cells+=1
                matrix[i][j].alive = True
            else:
                if matrix[i][j].alive:
                    matrix[i][j].alive = False
                    alive_cells-=1

def restart():
    #restarts the grid
    global matrix,alive_cells,simulate,gen
    gen =0
    alive_cells=0
    simulate=False
    for i in range(0, num_cells):
        for j in range(0, num_cells):
            matrix[i][j].alive = False

init_grid()
gen=0
alive_cells = 0

simulate = False
run = True
while run:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if not simulate:
            #gets left and right mouse mouse click and changes the life state of the cell
            if pygame.mouse.get_pressed()[0]:
                change_state(mouse_pos[0],mouse_pos[1], True)
            if pygame.mouse.get_pressed()[2]:
                change_state(mouse_pos[0], mouse_pos[1], False)
        if event.type == pygame.KEYDOWN:
            if not simulate:
                if event.key == pygame.K_a:
                    gen+=1
                    advance_life()
                if event.key == pygame.K_r:
                    restart()
            if event.key == pygame.K_s:
                if simulate:
                    simulate= False
                else:
                    simulate = True

    if simulate and alive_cells>0:
        advance_life()
        gen+=1
        pygame.time.delay(250)

    if alive_cells==0 and simulate: simulate = False

    win.fill((255,255,255))
    draw_grid(mouse_pos[0],mouse_pos[1])
    pygame.display.update()


pygame.quit()