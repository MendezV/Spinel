import numpy as np
import matplotlib.pyplot as plt

S = [  200 , 54 , 72  ]          #Sample count
L = [  43.5641, 10.891, 15.4022 ]    #Lattice vector lengths (bohrs)


z = np.arange(S[0])*L[0]/S[0]  #z-coordinates of grid points

def readPlanarlyAveraged(fileName, S):
    out = np.fromfile(fileName, dtype=np.float64)
    out = np.reshape(out, S)   #Reshape data
    print(np.shape(out))
    out = np.mean(out, axis=1) #y average
    out = np.mean(out, axis=1) #x average
    return out

dVacuum = readPlanarlyAveraged('Vacuum.d_tot',S)
dSolvated = readPlanarlyAveraged('Solvated.d_tot',S)
dShift = dSolvated - dVacuum

print("VBMshift =", dShift[0]*27.2114 ) #Report VBM shift in eV
print("VBMVacuum =", dVacuum[0] ) #Report VBM shift in Hartree
print("VBMSolvated =", dSolvated[0] ) #Report VBM shift in Hartree
plt.plot(z*0.529, dShift*27.2114, c='r', lw=4);     #Plot with unit conversions
plt.xlabel('z [Angstroms]', size=20)
plt.ylabel('Potential [eV]', size=20)
plt.xlim([0, L[0]/2*0.529])            #Select first half (top surface only)
plt.xticks(size=20)
plt.yticks(size=20)
plt.show()
