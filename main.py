import taichi as ti
ti.init(arch=ti.vulkan)  # Alternatively, ti.init(arch=ti.cpu)

n = 128
quad_size = 1.0 / n


ball_radius = 0.3
ball_center = ti.Vector.field(3, dtype=float, shape=(1, ))
ball_center[0] = [0, 0, 0]

x = ti.Vector.field(3, dtype=float, shape= n)
v = ti.Vector.field(3, dtype=float, shape= n)
force = ti.Vector.field(3, dtype=float, shape= n)
dm = 0.1
# you need to define more parameters here, such as stiffness,dt,length of spring .......


#initialize two cubes
from taichiCubeImport import data

cube1_vertex = ti.Vector.field(3, dtype=float, shape= n)
scale = 0.1
for i in range(len(data)):
    cube1_vertex[i] = [scale* data[i][0],scale * data[i][1],scale*data[i][2]]

cube2_vertex = []


@ti.kernel
def update_Cube1():
    pass

@ti.kernel
def update_Cube2():
    pass


@ti.kernel
def initialize_mass_points():

    for i in x:
        x[i] = [
            i * quad_size , 0.6,
            0.5
        ]
        v[i] = [0, -1, 0]


@ti.kernel
def substep():
    #显式欧拉法（可能会不稳定）
    #velocity verlet 更新方法


    #step1 计算每个质点受到的力
   # compute_force()
    #step2 更新加速度
    #step3 更新速度

    #for i in ti.grouped(v):
    #    v = v + force/dm * dt
    #step4 利用速度更新指点的位置




    for i in ti.grouped(x):
        #pass;
        x[i] += v[i] * 0.01;


@ti.kernel
def boundary_condition():
    pass
    #保持你的绳子的两个节点跟随fixed的固定运动
    #直接把x赋值为你希望他所在位置

@ti.kernel
def compute_force():
    pass


window = ti.ui.Window("Test for Drawing 3d-lines", (768, 768))
canvas = window.get_canvas()
scene = ti.ui.Scene()
camera = ti.ui.Camera()
camera.position(5, 2, 2)

initialize_mass_points()

while window.running:

    substep()
    boundary_condition()


    camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.RMB)
    scene.set_camera(camera)
    scene.ambient_light((0.8, 0.8, 0.8))
    scene.point_light(pos=(0.5, 1.5, 1.5), color=(1, 1, 1))
    scene.mesh(cube1_vertex);

    # Draw 3d-lines in the scene
    scene.lines(x, color = (0.28, 0.68, 0.99), width = 5.0)
    canvas.scene(scene)
    window.show()