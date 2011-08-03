import mdp
from PIL import Image, ImageDraw, ImageFont

#Generate data

#Fix the random number generator
mdp.numx_rand.seed(1266090063)

#Functions for generating shpes taken from the mdp tutorial
def uniform(min_, max_, dims):
    """Return a random number between min_ and max_ ."""
    return mdp.numx_rand.random(dims)*(max_-min_)+min_

def circumference_distr(center, radius, n):
    """Return n random points uniformly distributed on a circumference."""
    phi = uniform(0, 2*mdp.numx.pi, (n,1))
    x = radius*mdp.numx.cos(phi)+center[0]
    y = radius*mdp.numx.sin(phi)+center[1]
    return mdp.numx.concatenate((x,y), axis=1)

def circle_distr(center, radius, n):
    """Return n random points uniformly distributed on a circle."""
    phi = uniform(0, 2*mdp.numx.pi, (n,1))
    sqrt_r = mdp.numx.sqrt(uniform(0, radius*radius, (n,1)))
    x = sqrt_r*mdp.numx.cos(phi)+center[0]
    y = sqrt_r*mdp.numx.sin(phi)+center[1]
    return mdp.numx.concatenate((x,y), axis=1)

def rectangle_distr(center, w, h, n):
    """Return n random points uniformly distributed on a rectangle."""
    x = uniform(-w/2., w/2., (n,1))+center[0]
    y = uniform(-h/2., h/2., (n,1))+center[1]
    return mdp.numx.concatenate((x,y), axis=1)

N = 2000

cf1 = circumference_distr([7.5,6], 2, N/2)
cf2 = circumference_distr([5,1], 0.3, N/2)
cl1 = circle_distr([3.5,9], 0.5, N/2)
cl2 = circle_distr([3,2.5], 0.7, N)
r1 = rectangle_distr([5.5,3], 1, 1, N/2)
r2 = rectangle_distr([0.5,1], 1, 2, N)
r3 = rectangle_distr([1,7.5], 2, 1, N/2)
r4 = rectangle_distr([8,1], 2, 1, N/2)
x = mdp.numx.concatenate([cf1, cf2, cl1, cl2, r1,r2,r3,r4], axis=0)
x = mdp.numx.take(x,mdp.numx_rand.permutation(x.shape[0]), axis=0)

gng = mdp.nodes.GrowingNeuralGasNode(max_nodes=400)

#Create base image

#Convert floating point numbers to intergers for display in an image
def point_convert (x, y):
    """Convert point for gng to image point"""
    scale = 100.
    nx = int(x*scale)
    ny = int(y*scale)
    return (nx, ny)

baseim = Image.new('RGB', (1000, 1000), '#ffffff')
pix = baseim.load()

for point in x:
    impoint = point_convert(point[0], point[1])
    pix[impoint[0], impoint[1]] = (0,0,0)


font = ImageFont.truetype("arial.ttf", 24)

step = 20
total_points = x.shape[0]
fills = ['#ff0000', '#00ff00', '#0000ff', '#ff00ff', '#00ffff', '#ff0088', '#ff8800', '#0088ff']
for i in range(0, total_points, step):
    im = baseim.copy()
    gng.train(x[i: i+step])
    objs = gng.graph.connected_components()
    n_obj = len(objs)
    
    draw = ImageDraw.Draw(im)
    
    for j,obj in enumerate(objs):
        for node in obj:
            fx, fy = node.data.pos
            nx, ny = point_convert(fx, fy)
            draw.ellipse((nx-5, ny-5, nx+5, ny+5), fill=fills[j % 8])
    
    
    draw.text((700,900), "{0:.2%} complete".format(float(i+step)/float(total_points)), font=font, fill='#000000')
    draw.text((700,930), "{0:d} connected components".format(n_obj), font=font, fill='#000000')
    del draw
    im.save('training{0:d}.png'.format(i+step), 'PNG')

