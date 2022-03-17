from pylab import *
import random

i = 0

#Length
L = 5

#Positions
x = 0
y = 0
x2 = 2.5
y2 = 0

a1x = 0
a1y = 0
a2x = 0
a2y = 0

m1 = 5.4*10**10
m2 = 1

timestep = 0.1
v = [0.001,0.001] # X & Y Velocity array
vx = v[0] #X Velocity
vy = v[1] #Y Velocity
v2= [0,1]
vx2 = v2[0]
vy2 = v2[1]

n = input('Input a plot value: ') #Number of points plotted

scatter(x,y,color = 'blue', label = 'N Body Simulator')
scatter(x2, y2, color = 'red', label = 'N Body simulator')
xlim(-L,L)
ylim(-L,L)
show()

if mod(a,2) == 0:
    vx = -vx
    vx2 = -vx2
    if mod(a,5) == 0:
        vy = -vy
        vy2 = -vy2
        
while i<=n+1:
    
    dx = absolute(x-x2)
    dy = absolute(y-y2)
    
    dist = (dx*dx)+(dy*dy)
    distance = np.sqrt(dist)
    
    vector = [(x2-x),(y2-y)]/distance
    
    G = 6.67*10**-11
    fg = (G*(m1*m2))/(distance**2)
    
    a = (fg/m1)*vector
    a2 = -(fg/m2)*vector
    print a
    print a2
    print ''
    
    x = x+vx*timestep
    y = y+vy*timestep
    x2 = x2+vx2*timestep
    y2 = y2+vy2*timestep
    
    vx = vx+a[0]*timestep
    vy = vy+a[1]*timestep
    vx2 = vx2+a2[0]*timestep
    vy2 = vy2+a2[1]*timestep
    
    
    scatter(x2, y2, color='red', label='N Body')
    scatter(x, y, color='blue', label='N Body')
    xlim(-L,L)
    ylim(-L,L)
    show()
    pause(.1)
    
    print 'Red Position: ','(',x,' , ',y,')','    ',\
    'Blue Position: ','(',x2,' , ',y2,')'
    print ' '
    print 'Distance: ',distance   
    print 'i: ',i
    
    i = i+1