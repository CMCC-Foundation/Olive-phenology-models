# Model to predict olive phenophases for the cultivars 'Picholine', 'Carolea', 'Coratina' and 'Picholine+Carolea+Coratina'
# Phenophases: budbreak, inflorescence <5%, flowering <5%, pit hardening <5%, olive maturation index 1

import numpy as np
import os
os.chdir('C:/Users/claud/OneDrive/Documenti/CMCC/Progetti/NEMESI/Fenologia/Github')

###############################################################################
# ACTION! Unselect the desired cultivar
###############################################################################
#cultivar = 'picholine' 
cultivar = 'carolea' 
#cultivar = 'coratina'
#cultivar = 'combined'  

###############################################################################
# Define functions
###############################################################################
def Sigm (x) :
    return 1.0/(1.0 + np.exp(-x))

def stable_softmax(x):
    exps = np.exp(x - np.max(x))
    return exps / np.sum(exps) * 365.0

def olive_phen_model(clim_cue_std_by10):
    xk = np.transpose([clim_cue_std_by10])
    v1 = np.dot(w1, xk) + b1
    y1 = Sigm(v1)
    v2 = np.dot(w2, y1) + b2
    y2 = Sigm(v2)
    v3 = np.dot(w3, y2) + b3
    y3 = Sigm(v3)
    v4 = np.dot(w4, y3) + b4
    y4 = Sigm(v4)
    v = np.dot(w5, y4) + b5
    yreal = stable_softmax(v)
    return yreal.astype(int)       

 ###############################################################################
# Upload coefficients
###############################################################################
if (cultivar == 'picholine'):
    coeff  = np.load('Coefficients_Picholine.npz')
elif (cultivar == "carolea"):
    coeff  = np.load('Coefficients_Carolea.npz')
elif (cultivar == "coratina"):
    coeff  = np.load('Coefficients_Coratina.npz')
elif (cultivar == "combined"):
    coeff  = np.load('Coefficients_Combined_Cultivars.npz')
        
coeff_np = [coeff[key] for key in coeff]       
w1 = coeff_np[0]
w2 = coeff_np[1]
w3 = coeff_np[2]
w4 = coeff_np[3]   
w5 = coeff_np[4] 
b1 = coeff_np[5]  
b2 = coeff_np[6] 
b3 = coeff_np[7] 
b4 = coeff_np[8] 
b5 = coeff_np[9]

###############################################################################
# Upload climatic cues
###############################################################################
if (cultivar == 'carolea'):
    mean_temp = np.genfromtxt('Daily_insolation_example.txt', usecols=3)
    mean_temp_std = (mean_temp - 288.997359855334)/6.82566414520133
    mean_temp_std_by5 = np.zeros(91, dtype = float)
    mean_temp_std_by5 = [sum(mean_temp_std[i:i+5])/5.0 for i in range(0, 455, 5)]    
    mean_temp_std_by10 = np.zeros(45, dtype = float)
    mean_temp_std_by10 = [sum(mean_temp_std[i:i+10])/10.0 for i in range(0, 450, 10)]
    insolation = np.genfromtxt('Daily_insolation_example.txt', usecols=3)
    insolation_std = (insolation - 219855893.958262)/103632768.2942
    insolation_std_by5 = np.zeros(91, dtype = float)
    insolation_std_by5 = [sum(insolation_std[i:i+5])/5.0 for i in range(0, 455, 5)]    
    insolation_std_by10 = np.zeros(45, dtype = float)
    insolation_std_by10 = [sum(insolation_std[i:i+10])/10.0 for i in range(0, 450, 10)]  
    clim_cue_std = np.concatenate((mean_temp_std, insolation_std))
    clim_cue_std_by5 = np.concatenate((mean_temp_std_by5, insolation_std_by5))
    clim_cue_std_by10 = np.concatenate((mean_temp_std_by10, insolation_std_by10))
else:
    insolation = np.genfromtxt('Daily_insolation_example.txt', usecols=3)
    clim_cue_std = (insolation - 219855893.958262)/103632768.2942
    clim_cue_std_by5 = np.zeros(91, dtype = float)
    clim_cue_std_by5 = [sum(clim_cue_std[i:i+5])/5.0 for i in range(0, 455, 5)]    
    clim_cue_std_by10 = np.zeros(45, dtype = float)
    clim_cue_std_by10 = [sum(clim_cue_std[i:i+10])/10.0 for i in range(0, 450, 10)]    

###############################################################################
# Run the model
###############################################################################
y = olive_phen_model(clim_cue_std_by10)
y_pred = np.zeros(5, dtype = float)
for i in range (0, 5):
    y_pred[i] = np.sum(y[0:i+1])

filename = 'predictions_example.txt'
with open(filename, 'w') as file:
    file.write("BBCH1  = " + str(y_pred[0]) + "\n"+
               "BBCH51 = " + str(y_pred[1]) + "\n"+
               "BBCH61 = " + str(y_pred[2]) + "\n"+ 
               "BBCH71 = " + str(y_pred[3]) + "\n"+
               "BBCH80 = " + str(y_pred[4]))
file.close       
