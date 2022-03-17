from pylab import *
import math
from mpl_toolkits.mplot3d import Axes3D
 

def gravitational_force(pos1, pos2, pmass):
    grav_constant = 6.67*10**-11
    temp_distance = pos1-pos2
    distance = magnitude(temp_distance)
    unit_vector = normal(temp_distance)
    acceleration = ((-grav_constant*pmass)/(distance**2))*unit_vector
    return acceleration
            
def magnitude(vector):
    d = np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    return d

def normal(vector):
    normal = vector/magnitude(vector)
    return normal

def main():
    box_length = 2
    num_planets = input('How many planets do you want?: ')
    timestep = 0.005
    x_pos_list = [0]
    y_pos_list = [0]
    z_pos_list = [0]
    x_vel_list = [0]
    y_vel_list = [0]
    z_vel_list = [0]
    mass_list = [5.11*(10**11)]
    
    for w in range(1,num_planets):
        x_pos_list.append(np.random.random())
        y_pos_list.append(0)
        z_pos_list.append(0)
        x_vel_list.append(0)
        y_vel_list.append(7.54)
        z_vel_list.append(0)
        mass_list.append(0.15)
               
    x_pos_array = np.array(x_pos_list)
    y_pos_array = np.array(y_pos_list)
    z_pos_array = np.array(z_pos_list)
    stacked_pos_array = np.vstack((x_pos_array,y_pos_array,z_pos_array))
    x_vel_array = np.array(x_vel_list)
    y_vel_array = np.array(y_vel_list)
    z_vel_array = np.array(z_vel_list)
    stacked_vel_array = np.vstack((x_vel_array,y_vel_array,z_vel_array))
    num_timesteps = input('How many timesteps?: ')
    numsteps = 0
    fig = figure()
    ax = fig.add_subplot(111,projection = '3d')
    show()
    acceleration_array = np.zeros((3,num_planets))
    
    while numsteps < num_timesteps:
        for i in range(0,num_planets):
            for j in range(0,num_planets):
                if i != j: 
                    planet1 = np.array([stacked_pos_array[0,i], stacked_pos_array[1,i], stacked_pos_array[2,i]])
                    planet2 = np.array([stacked_pos_array[0,j], stacked_pos_array[1,j], stacked_pos_array[2,j]])
                    acceleration_pair = gravitational_force(planet1, planet2, mass_list[j])
                    acceleration_array[:,i] = acceleration_array[:,i] + acceleration_pair
                    
            stacked_vel_array[:,i] = stacked_vel_array[:,i] + acceleration_array[:,i]*timestep
            stacked_pos_array[:,i] = stacked_pos_array[:,i] + stacked_vel_array[:,i]*timestep
            
        acceleration_array = np.zeros((3,num_planets))
            #resets the acceleration array     
        ax.set_xlim3d(-box_length, box_length)
        ax.set_ylim3d(-box_length, box_length)
        ax.set_zlim3d(-box_length, box_length)
        ax.set_autoscale_on(False)
        sct = ax.scatter(stacked_pos_array[0,:], stacked_pos_array[1,:], stacked_pos_array[2,:], color = 'red')
        show()
        pause(.1)
        
        if sct is not None:
            sct.remove()
            
        num_timesteps += 1
        
main()