# Phenological observations for the cultivars 'Picholine', 'Carolea' and 'Coratina'
# Phenophases: budbreak, inflorescence <5%, flowering <5%, pit hardening <5%, olive maturation index 1

import numpy as np

#################################################################################
# Picholine phenological observations
#################################################################################
picholine_obs_lab_abs = np.array ([[95, 134, 154, 210, 288, 0],     #Montepaldi 1997
                                   [25,  62, 137, 191, 291, 0],     #Valenzano 1997
                                   [74,  88, 124, 185, 336, 0],     #Belici Mare 1999
                                   [34,  60, 137, 205, 279, 0],     #Rende 1999
                                   [68, 103, 145, 201, 264, 0]])    #SApollinare 1998

picholine_obs_lab_incr = np.array ([[95,  39,  20,  56,  78,  77],    #Montepaldi 1997
                                    [25,  37,  75,  54, 100,  74],    #Valenzano 1997
                                    [74,  14,  36,  61, 151,  29],    #Belici Mare 1999
                                    [34,  26,  77,  68,  74,  86],    #Rende 1999
                                    [68,  35,  42,  56,  63, 101]])   #SApollinare 1998

picholine_obs_unlab_abs = np.array ([[ 97, 133, 148, 202,   0, 0],  #Montepaldi 1998
                                     [111, 130, 150, 194,   0, 0],  #Montepaldi 1999
                                     [  0,   0, 117, 177,   0, 0],  #Villasor 1997
                                     [  0, 104, 126, 195, 269, 0],  #Villasor 1998
                                     [  0, 105, 135,   0, 290, 0],  #Villasor 1999 
                                     [  0,   0, 137, 202,   0, 0],  #Villasor 2000
                                     [  0,  75, 133, 207, 288, 0],  #Valenzano 1998
                                     [  0,  59, 138, 198,   0, 0],  #Valenzano 1999
                                     [  0,  77, 132,   0,   0, 0],  #Valenzano 2000
                                     [ 66,  87,  94,   0, 340, 0],  #Torre Allegra 1997
                                     [ 44,  95, 132, 158,   0, 0],  #Torre Allegra 1998
                                     [ 67,  89, 131, 159,   0, 0],  #Torre Allegra 1999
                                     [  0,   0, 107, 180,   0, 0],  #Belici Mare 1997
                                     [  0,  84, 116, 171,   0, 0],  #Belici Mare 1998
                                     [  0,   0, 117, 177,   0, 0],  #Rende 1997
                                     [ 56,  96,   0,   0,   0, 0],  #Rende 1998
                                     [  0, 122, 147, 204, 286, 0],  #S.Apollinare 1997 
                                     [  0, 130, 144, 200, 256, 0],  #S.Apollinare 1999
                                     [ 82,   0,   0, 222,   0, 0]]) #S.Apollinare 2000

picholine_obs_unlab_incr = np.array ([[ 97,   36,  15,  54, -999, 365],  #Montepaldi 1998
                                      [111,   19,  20,  44, -999, 365],  #Montepaldi 1999
                                      [-999,-999, 117,  60, -999, 365],  #Villasor 1997
                                      [-999, 104,  22,  69,   74,  96],  #Villasor 1998
                                      [-999, 105,  30,-999,  290,  75],  #Villasor 1999
                                      [-999,-999, 137,  65, -999, 365],  #Villasor 2000
                                      [-999,  75,  58,  74,   81,  77],  #Valenzano 1998
                                      [-999,  59,  79,  60, -999, 365],  #Valenzano 1998
                                      [-999,  77,  55,-999, -999, 365],  #Valenzano 2000
                                      [  66,  21,   7,-999,  340,  25],  #Torre Allegra 1997
                                      [  44,  51,  37,  26, -999, 365],  #Torre Allegra 1998
                                      [  67,  22,  42,  28, -999, 365],  #Torre Allegra 1998
                                      [-999,-999, 107,  73, -999, 365],  #Belici Mare 1997
                                      [-999,  84,  32,  55, -999, 365],  #Belici Mare 1998
                                      [-999,-999, 117,  60, -999, 365],  #Rende 1997
                                      [  56,  40,-999,-999, -999, 365],  #Rende 1998
                                      [-999, 122,  25,  57,   82,  79],  #S.Apollinare 1997
                                      [-999, 130,  14,  56,   56, 109],  #S.Apollinare 1999
                                      [  82,-999,-999, 222, -999, 365]]) #S.Apollinare 2000 

picholine_obs_test_abs = np.array([[0, 0, 126, 0, 0, 0],  #Rende 2017
                                   [0, 0, 124, 0, 0, 0]]) #Rende 2018

#################################################################################
# Carolea phenological observations
#################################################################################   

carolea_obs_lab_abs = np.array ([[95, 132, 155, 210, 280, 0], #Montepaldi 1997
                                [28, 104, 131, 192, 267, 0],  #Villasor 1998
                                [25,  69, 137, 188, 280, 0],  #Valenzano 1997
                                [68,  96, 145, 201, 294, 0]]) #S.Apollinare 1998
 

carolea_obs_lab_incr = np.array  ([[95,  37,  23,  55,  70,  85],   #Montepaldi 1997 
                                [28,  76,  27,  61,  75,  98],   #Villasor 1998 
                                [25,  44,  68,  51,  92,  85],   #Valenzano 1997
                                [68,  28,  49,  56,  93,  71]])  #S.Apollinare 1998 


carolea_obs_unlab_abs = np.array([[97, 131, 148, 202,  0, 0],  #Montepaldi 1998
                                [108, 136, 150, 194,  0, 0],  #Montepaldi 1999
                                [  0,   0, 117, 185,295, 0],  #Villasor 1997
                                [ 36,  94, 134,   0,278, 0],  #Villasor 1999
                                [  0,   0, 138, 196,  0, 0],  #Villasor 2000
                                [  0,  75, 134,   0,281, 0],  #Valenzano 1998
                                [  0,  71, 140,   0,  0, 0],  #Valenzano 1999
                                [  0,  77, 133, 180,  0, 0],  #Valenzano 2000
                                [ 66,  87,  94,   0,278, 0],  #Torre Allegra 1997
                                [ 41,  91, 124, 152,  0, 0],  #Torre Allegra 1998
                                [ 66,  85, 129, 152,  0, 0],  #Torre Allegra 1999
                                [  0,   0, 100, 183,  0, 0],  #Belici Mare 1997
                                [  0,  85, 117, 173,314, 0],  #Belici Mare 1998
                                [ 74,  83, 117,   0,  0, 0],  #Belici Mare 1999
                                [ 15,   0,   0, 185,  0, 0],  #Rende 1997
                                [ 56, 117,   0,   0,  0, 0],  #Rende 1998
                                [ 34,  60, 134,   0,282, 0],  #Rende 1999      
                                [  0, 124, 150, 204,286, 0],  #S.Apollinare 1997
                                [  0, 130, 144, 200,264, 0],  #S.Apollinare 1999
                                [ 75, 117,   0, 215,  0, 0]]) #S.Apollinare 2000


carolea_obs_unlab_incr = np.array ([[97,  34,  17,  54,  -999,  365],  #Montepaldi 1998
                                   [108, 28,  14,  44,  -999,  365],  #Montepaldi 1999
                                   [-999,-999, 117,  68, 110,   70],  #Villasor 1997
                                   [  36,  58,  40,-999, 278,  87],  #Villasor 1999
                                   [-999,-999, 138,  58,-999, 365],  #Villasor 2000 
                                   [-999,  75,  59,-999, 281,  84],  #Valenzano 1998
                                   [-999,  71,  69,-999,-999, 365],  #Valenzano 1999
                                   [-999,  77,  56,  47,-999, 365],  #Valenzano 2000
                                   [66,  21,   7,  -999, 278,  87],  #Torre Allegra 1997
                                   [  41,  50,  33,  28,-999, 365],  #Torre Allegra 1998
                                   [  66,  19,  44,  23,-999, 365],  #Torre Allegra 1999
                                   [-999,-999, 100,  83,-999, 365],  #Belici Mare 1997
                                   [-999,  85,  32,  56, 141,  51],  #Belici Mare 1998
                                   [  74,   9,  34,-999,-999, 365],  #Belici Mare 1999
                                   [  15,-999,-999, 185,-999, 365],  #Rende 1997
                                   [  56,  61,-999,-999,-999, 365],  #Rende 1998
                                   [  34,  26,  74,-999, 282,  83],  #Rende 1999
                                   [-999, 124,  26,  54,  82,  79],  #S.Apollinare 1997
                                   [-999, 130,  14,  56,  64, 101],  #S.Apollinare 1999
                                   [  75,  42,-999, 215,-999, 365]]) #S.Apollinare 2000  

carolea_obs_test_abs = np.array([[0, 0, 125, 0, 0, 0],  #Rende 2017
                                 [0, 0, 121, 0, 0, 0]]) #Rende 2018 


#################################################################################
# Coratina phenological observations
################################################################################# 
coratina_obs_lab_abs = np.array ([[94, 132, 153, 210, 275, 0],  #Montepaldi 1997
                                [34,  60, 137, 204, 284, 0],  #Rende 1999
                                [75, 110, 145, 201, 257, 0]]) #S.Apollinare 1998

coratina_obs_lab_incr = np.array([[94,  38,  21,  57,  65,  90],      #Montepaldi 1997
                                [34,  26,  77,  67,  80,  81],      #Rende 1999
                                [75,  35,  35,  56,  56,  108]])    #S.Apollinare 1998

coratina_obs_unlab_abs = np.array ([[102, 127, 152, 202,  0,  0],  #Montepaldi 1998
                                  [111, 133, 149, 200,  0,  0],  #Montepaldi 1999
                                  [  0,   0, 127, 196, 295, 0],  #Villasor 1997
                                  [  0, 104, 131, 192, 259, 0],  #Villasor 1998
                                  [  0,  69, 126,   0, 279, 0],  #Villasor 1999
                                  [  0,   0, 138, 202,   0, 0],  #Villasor 2000
                                  [ 25,  34, 135, 196,   0, 0],  #Valenzano 1997
                                  [ 58,  80,  94,   0, 310, 0],  #Torre Allegra 1997
                                  [  41,  87, 123, 158,   0, 0],  #Torre Allegra 1998
                                  [  65,  83, 130, 151,   0, 0],  #Torre Allegra 1999
                                  [   0,   0, 127, 196,   0, 0],  #Rende 1997
                                  [  64, 128,   0,   0,   0, 0],  #Rende 1998
                                  [   0, 122, 145, 204, 272, 0],  #S.Apollinare 1997
                                  [   0, 130, 144, 200, 263, 0],  #S.Apollinare 1999
                                  [  89, 121, 142, 222,   0, 0]]) #S.Apollinare 2000

coratina_obs_unlab_incr = np.array ([[102,   25,  25,  50, -999, 365],  #Montepaldi 1998
                                  [111,   22,  16,  51, -999, 365],  #Montepaldi 1999
                                  [-999,-999, 127,  69,   99,  70],  #Villasor 1997 n4
                                  [-999, 104,  27,  61,   67, 106],  #Villasor 1998 n5
                                  [-999,  69,  57,-999,  279, 365],  #Villasor 1999 n6 
                                  [-999,-999, 138,  64, -999, 365],  #Villasor 2000 n7 
                                  [  25,   9, 101,  61, -999, 365],  #Valenzano 1997 n8
                                  [  58,  22,  14, -999, 310,  55],  #Torre Allegra 1997 
                                  [  41,  46,  36,  35, -999, 365],  #Torre Allegra 1998
                                  [  65,  18,  47,  21, -999, 365],  #Torre Allegra 1999
                                  [-999,-999, 127,  69, -999, 365],  #Rende 1997
                                  [  64,  64,-999,-999, -999, 365],  #Rende 1998
                                  [-999, 122,  23,  59,   68,  93],  #S.Apollinare 1997
                                  [-999, 130,  14,  56,   63, 102],  #S.Apollinare 1999
                                  [ 89,  32,  21,  81,  -999, 365]]) #S.Apollinare 2000


coratina_obs_test_abs = np.array([[0, 0, 127, 0, 0, 0],  #Rende 2017 n25t
                                  [0, 0, 126, 0, 0, 0]]) #Rende 2018 n26t     