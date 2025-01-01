# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import Tk, Canvas, PhotoImage, mainloop
import random
import math
import time

def matrix_mult(a, b, g,vec):

    xx = (1 * vec[0] + 0 * vec[1] + 0 * vec[2])
    yx = (0 * vec[0] + math.cos(a) * vec[1] + -math.sin(a) * vec[2])
    zx = (0 * vec[0] + math.sin(a) * vec[1] + math.cos(a) * vec[2])

    xy = (math.cos(b) * xx + 0 * yx + math.sin(b) * zx)
    yy = (0 * xx + 1 * yx + 0 * zx)
    zy = (-math.sin(b) * xx + 0 * yx + math.cos(b) * zx)

    x = (math.cos(g) * xy + -math.sin(g) * yy + 0 * zy)
    y = (math.sin(g) * xy + math.cos(g) * yy + 0 * zy)
    z = (0 * xy + 0 * yy + 1 * zy)

    return(x,y,z)

def angle_between(p_vector,v2):
    return math.acos(dot(p_vector,v2)/(mag(p_vector)*mag(v2)))

def vec_between(p1,p2):
    return (p1[0]-p1[0], p1[1]-p2[1], p1[2]-p2[2])

def projection(x_y_z,a_b_c,d_e_f):
    a=a_b_c[0]
    b=a_b_c[1]
    c=a_b_c[2]

    d=d_e_f[0]
    e=d_e_f[1]
    f=d_e_f[2]

    x=x_y_z[0]
    y=x_y_z[1]
    z=x_y_z[2]

    t= (a*d-a*x+b*e-b*y+c*f-c*z)/(a*a+b*b+c*c)
    #print("t=",t)
    return(x+t*a,y+t*b,z+t*c)

def proj(origin_p,pointing_v,y_orient_v,z_orient_v,point_p):
    r_O = origin_p
    n = pointing_v
    e_1 = y_orient_v
    e_2 = z_orient_v

    #print("dot1=", dot(n, e_1))
   # print("dot1=", dot(n, e_2))
    #print("dot1=", dot(e_1, e_2))

   # print(p_vector)
   # print(p_vector)

   # p_axis_x = (1, 0, 0)
    r_P = point_p
   # p_axis_y = (0, 1, 0)
   # p_axis_z = (0, 0, 1)

    s = dot(n, vec_between(r_P, r_O))
    t_1 = dot(e_1, vec_between(r_P, r_O))
    t_2 = dot(e_2, vec_between(r_P, r_O))

    xp = r_O[0] + t_1 * e_1[0] + t_2 * e_2[0] + s * n[0]
    yp = r_O[1] + t_1 * e_1[1] + t_2 * e_2[1] + s * n[1]
    zp = r_O[2] + t_1 * e_1[2] + t_2 * e_2[2] + s * n[2]
    return((xp,yp,zp))

def mag(x):
    return math.sqrt(x[0]*x[0]+x[1]*x[1]+x[2]*x[2])

def norm(x):
    mag = math.sqrt(x[0] * x[0] + x[1] * x[1] + x[2] * x[2])
    return (x[0]/mag,x[1]/mag,x[2]/mag)

def dot(x,y):
    return x[0]*y[0]+x[1]*y[1]+x[2]*y[2]

def dist_2d(p1,p2):
    return((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]))

def dist_3d(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def print_to_screen_coor(WIDTH,HEIGHT,canvas,x,y,color):
    x=x+WIDTH/2
    y=y+HEIGHT/2
    if(x>WIDTH):
        return x,y
    if(y>HEIGHT):
        return x,y
    #for inc in range(5):
    #    imageput(color,(int(x),int(y+inc*inc)))

    imageput(canvas, color, (x,y))

    #broaden points
    p_2=(x,y)
    n = 2
    iii = 0
    for xx in range(-n, n + 1):
        for yy in range(-n, n + 1):
            if ((xx / n) ** 2 + (yy / n) ** 2) <= 1:
                iii = iii + 1
    for m in range(iii):
        imageput(canvas, color, nearest_neighbors(n, m, p_2))

    #print("cor:",x,y)
    return x,y

def imgput(color,xy):
    img.put(color, (int(xy[0]), int((HEIGHT-xy[1]))))

def imageput(canvas,color,xy):
    canvas.create_rectangle(int(xy[0]), int((HEIGHT-xy[1])),int(xy[0]+1), int((HEIGHT-(xy[1]+1))),fill=color,outline="")

# brute force method to broaden lines
def nearest_neighbors(n,m,current_p):
    iii=0
    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            if((x/n)**2+(y/n)**2)<=1:
                if(m==iii):
                    return(int(current_p[0]+x),int(current_p[1]+y))
                iii=iii+1

def print_line(WIDTH, HEIGHT, img, p_1, p_2, color,scale=1):
    x0=p_1[0]
    y0=p_1[1]
    x1 = p_2[0]
    y1 = p_2[1]
    # find absolute differences
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)

    # find maximum difference
    steps = max(dx, dy)

    #thicken the line brute force
    if(steps<1):
        n = 5
        iii = 0
        for xx in range(-n, n + 1):
            for yy in range(-n, n + 1):
                if ((xx / n) ** 2 + (yy / n) ** 2) <= 1:
                    iii = iii + 1
        for m in range(iii):
            imageput(canvas,color, nearest_neighbors(n, m, p_2))
        return

    # calculate the increment in x and y
    xinc = (x1-x0) / steps
    yinc = (y1-y0) / steps

    # start with 1st point
    x = float(x0)
    y = float(y0)

    # make a list for coordinates
    x_coorinates = []
    y_coorinates = []

    n = 3
    iii = 0
    for xx in range(-n, n + 1):
        for yy in range(-n, n + 1):
            if ((xx / n) ** 2 + (yy / n) ** 2) <= 1:
                iii = iii + 1

    for i in range(int(steps)):
        # increment the values
        x = x + xinc
        y = y + yinc
        imageput(canvas,color, (int(x), int(y)))

        p = (int(x), int(y))
        n = 3
        for m in range(iii):
            imageput(canvas,color,nearest_neighbors(n,m,p))

        if(i==int(steps)-1):
            n = 6
            iii = 0
            for xx in range(-n, n + 1):
                for yy in range(-n, n + 1):
                    if ((xx / n) ** 2 + (yy / n) ** 2) <= 1:
                        iii = iii + 1

            n = 6
            for m in range(iii):
                imageput(canvas,color, nearest_neighbors(n, m, p))

def looping(current,min,max,change):
    current=current+change
    while(current<min):
        diff = max - min
        current=current+diff
    while (current > max):
        diff = max - min
        current=current - diff
    return current

def law_of_cosines(a,b,angle):
    return math.sqrt(a*a+b*b-2*a*b*math.cos(angle))

def law_of_sines_ang(a,angle,angle_b):
    return (a/math.sin(angle))*math.sin(angle_b)

def law_of_sines_side(a,b,angle):
    return b*(math.sin(angle))/a

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    WIDTH,HEIGHT = 640,480
    scale = 100
    window = Tk()
    canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height = HEIGHT)
    canvas.create_image((WIDTH/2,HEIGHT/2), image = img, state="normal")

    time.sleep(10)

    for x in range (4 * WIDTH):
        y = int(HEIGHT/3 + HEIGHT/3 +math.sin(x/80))
        imageput(canvas,"#0000ff",(x//4,y))
        #print(img.get(x//4,y))

    window.update()
    time.sleep(0)
    canvas.delete("all")
    for x in range (4 * WIDTH):
        y = int(HEIGHT/2 + HEIGHT/4 +math.sin(x/80))
        imageput(canvas,"#0000ff",(x//3,y))
        #print(img.get(x//4,y))

    window.update()
    time.sleep(0)

    pxx = print_to_screen_coor(WIDTH,HEIGHT,canvas,0,0,"#ffffff")
    pyy = print_to_screen_coor(WIDTH, HEIGHT, canvas, 0, 0, "#ffffff")
    pzz = print_to_screen_coor(WIDTH, HEIGHT, canvas, 0, 50, "#ffffff")

    perspective = (30/360)*2*math.pi
    #print_line(WIDTH, HEIGHT, img,pxx,pzz,"#ffffff")
    a1 = math.pi/16#0 * random.random()
    a2 = 0#180 * random.random()
    a3 = 0#0 * random.random()

    plot_data = []
    number =20
    for iii in range(number):
        plot_data.append((5 * random.uniform(-1, 1), 5 * random.uniform(-1, 1), 5 * random.uniform(-1, 1)))
        #plot_data.append(((iii+1)*2,(iii+1)*2,(iii+1)*2))

    while 1 :
        #clear()
        canvas.delete("all")

        p_pos = (6, 0, 0) #camera initial position
        p_vector = norm((-1, 0, 0))
        p_vector_y = norm((0, 1, 0))
        p_vector_z = norm((0, 0, 1))
        a1 = 0# math.pi/16+a1
        a2 =  looping(a2,0.1,math.pi*2-.1,math.pi/32) #math.pi/4
        a3 = math.pi/8
        perspective = math.pi/1.9#looping(perspective,0.1,math.pi-.1,math.pi/32)
        #intt = .01
        #print(perspective)
        p_axis_x = (1, 0, 0)
        axis_vectors = [(1,0,0),(0,1,0),(0,0,1)]
        axis_colors = ("#ff0000","#00ff00","#0000ff")
        order = [0,1,2]
        rotated_axis_vectors = []

        for iii in range(number):
            axis_vectors.append(plot_data[iii])
            order.append(iii + 3)

        for axis in axis_vectors: #rotated axis
            #stores only the x coordinate as that defines order from the camera
            new_vector =matrix_mult(a1, a2, a3, axis)
            rotated_axis_vectors.append(new_vector[0])

        #sorts rotated vector points to find draw order
        vectors = sorted(zip(rotated_axis_vectors,order))

        for point in vectors:
            if(p_pos[0]<point[0]):
                break
            rotated_v = matrix_mult(a1, a2, a3, axis_vectors[point[1]])
            new_p = proj(p_pos, p_vector, p_vector_y, p_vector_z, rotated_v)

            s1 = dist_3d(rotated_v, p_pos)
            h = dist_3d(rotated_v, p_pos)
            s2 = dist_3d(p_pos,new_p)
            s3 = dist_3d(new_p,rotated_v)
            alpha1 = math.acos(s2/s1)
            alpha22 = math.asin(s2 / s1)
            alpha2 = math.acos(s3/s1)
            alpha11 = math.asin(s3 / s1)
            angle3= math.pi/2

            #rudimentary attempt at changing perspective angle
            #forces the angle of differnce between
            if(perspective<math.pi/2):
                angle4=math.pi-perspective
                s4 = law_of_cosines(s2,s3,perspective)
                s5 = s2
                s6 = s3
                angle5 = law_of_sines_side(s4,s5,perspective)
                angle6 = law_of_sines_side(s4, s6, perspective)

                s7=s6
                angle7=math.pi-angle4
                angle8=math.pi/2
                angle9=math.pi-(angle8+angle7)
                s8=law_of_sines_ang(s7,angle8,angle9)

                ratio=(s8+s2)/s2
                temp = norm(new_p)
                new_p = (ratio*new_p[0],ratio*new_p[1],ratio*new_p[2])
            if(perspective>=math.pi/2):
                angle4=math.pi/2 -(perspective- math.pi/2)


                angle5 = alpha1
                alpha6=math.pi-(angle4+angle5)

                s4 = s2
                s5 = law_of_sines_ang(s4, alpha6, angle4)
                s6 = law_of_sines_ang(s4, alpha6, angle5)

                s7=s5
                angle7=math.pi/2
                angle8=angle5
                s8=law_of_sines_ang(s5,angle7,angle8)
                alpha9 = math.pi - (angle7 + angle8)
                s9=law_of_sines_ang(s5,angle7,alpha9)
                if(s2==0):
                    ratio=0
                else:
                    ratio = (s2 -(s2-s9))/ s2
                temp = norm(new_p)
                new_p = (ratio * new_p[0], ratio * new_p[1], ratio * new_p[2])

            if (new_p[1] < 0):
                1
            pxx = print_to_screen_coor(WIDTH, HEIGHT, canvas, p_pos[2], p_pos[1], "#ffffff")
            #pyy = print_to_screen_coor(WIDTH, HEIGHT, canvas, 10 * new_p[2], 10 * new_p[1], "#ffffff")
            #pyy = print_to_screen_coor(WIDTH, HEIGHT, canvas, 20 * new_p[2], 20 * new_p[1], "#ffffff")
            pyy = print_to_screen_coor(WIDTH, HEIGHT, canvas, 100 * new_p[2], 100 * new_p[1], "#ffffff")
            #pyy = print_to_screen_coor(WIDTH, HEIGHT, canvas, new_p[2], new_p[1], "#ffffff")

            # print((p_pos[1], p_pos[2]))
            # print((new_p[1], new_p[2]))
            #if (point[1] == 1):
            #    print("\t",pxx)
            #    print("\t", pyy)
            if(point[1]<3):
                print_line(WIDTH, HEIGHT, canvas, pxx, pyy, axis_colors[point[1]])  # "#a7d5a5", scale)
            # "#01028f"
            # "#ea11d6"
        window.update()
