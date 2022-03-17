from pylab import *
import math
from mpl_toolkits.mplot3d import Axes3D
 

def grav(pos1, pos2, pmass):
    G = 6.67*10**-11
    d = pos1-pos2
    distance = mag(d)
    vector = norm(d)
    a = ((-G*pmass)/(distance**2))*vector
    return a
    
def mag(vector):
    d = np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    return d

def norm(vector):
    norm = vector/mag(vector)
    return norm

def main():
    q = 50*(10**11)
    v = 29.8*(10**3)
    number = input('How many planets do you want?: ')
    val = number
    timestep = 86400*500
    
    x = np.linspace(-q,q,number)
    y = np.linspace(-q,q,number)
    z = np.linspace(-q,q,number)
    pos = np.vstack((x,y,z))*np.random.random((3,number))

    
    vx = np.random.random(number)*(v/2)
    vy = np.random.random(number)*(v/2)
    vz = np.random.random(number)*(v/2)
    vel = np.vstack((vx,vy,vz))
    
    mass = 10**30
    
    n = input('How many timesteps?: ')
    
    numsteps = 0
    
    fig = figure()
    ax = fig.add_subplot(111,projection = '3d')
    show()
    accel = np.zeros((3,number))
    
    while numsteps < n:
        for i in range(0,number):
            for j in range(0,number):
                if i != j: 
                    planet1 = np.array([pos[0,i], pos[1,i], pos[2,i]])
                    planet2 = np.array([pos[0,j],pos[1,j],pos[2,j]])
                    accel_pair = grav(planet1, planet2, mass)
                    accel[:,i] = accel[:,i] + accel_pair
                    
            #if (planet1[0]+vel[0,i]*timestep < q) and (planet1[0]+vel[0,i]*timestep > -q):
             #   if (planet1[1]+vel[1,i]*timestep < q) and (planet1[1]+vel[1,i]*timestep > -q):
              #      if (planet1[2]+vel[2,i]*timestep < q) and (planet1[2]+vel[2,i]*timestep > -q):
               #         vel[:,i] = vel[:,i] + accel[:,i]*timestep
                #        pos[:,i] = pos[:,i] + vel[:,i]*timestep
                 #   elif (planet1[2]+vel[2,i]*timestep >= q) or (planet1[2]+vel[2,i]*timestep <= -q):
                 #       vel[2,:] = -vel[2,:]
               # elif (planet1[1]+vel[1,i]*timestep >= q) and (planet1[1]+vel[1,i]*timestep <= -q):
               #     vel[1,:] = -vel[1,:]
           # elif (planet1[0]+vel[0,i]*timestep >= q) and (planet1[0]+vel[0,i]*timestep <= -q):
            #    vel[0,:] = -vel[0,:]
            
            if (planet1[0]+vel[0,i]*timestep < q) and (planet1[0]+vel[0,i]*timestep > -q)\
            and (planet1[1]+vel[1,i]*timestep < q) and (planet1[1]+vel[1,i]*timestep > -q)\
            and (planet1[2]+vel[2,i]*timestep < q) and (planet1[2]+vel[2,i]*timestep > -q):
                pos[:,i] = pos[:,i] + vel[:,i]*timestep
                vel[:,i] = vel[:,i] + accel[:,i]*timestep
            else:
                if (planet1[0]+vel[0,i]*timestep > q):
                    vel[0,i] = -vel[0,i]
                    pos[0,i] = q-1
                elif (planet1[0]+vel[0,i]*timestep < -q):
                    vel[0,i] = -vel[0,i]
                    pos[0,i] = q+1                    
                if (planet1[1]+vel[1,i]*timestep > q):
                    vel[1,i] = -vel[1,i]
                    pos[1,i] = q-1
                elif (planet1[1]+vel[1,i]*timestep < -q):
                    vel[1,i] = -vel[1,i]
                    pos[1,i] = q+1
                if (planet1[2]+vel[2,i]*timestep > q):
                    vel[2,i] = -vel[2,i]
                    pos[2,i] = q-1
                elif (planet1[2]+vel[2,i]*timestep < -q):
                    vel[2,i] = -vel[2,i]
                    pos[2,i] = q+1
                          
            ax.set_xlim3d(-q,q)
            ax.set_ylim3d(-q,q)
            ax.set_zlim3d(-q,q)
            ax.set_autoscale_on(False)
            
            if (mod(val,2)) != 0:
                sct = ax.scatter(pos[0,i], pos[1,i], pos[2,i], color = 'blue')
                print 'odd'
                
            else:
                sct = ax.scatter(pos[0,i], pos[1,i], pos[2,i], color = 'red')
                print 'even'
                
                
            if sct is not None:
                sct.remove()
            val = val - 1
            
            show()
            pause(.1)
            
        numsteps += 1
main()