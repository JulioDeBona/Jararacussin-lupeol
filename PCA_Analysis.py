#developed by Julio De Bona

from prody import *
from numpy import *
from pylab import *
ion()

# PREPARE ENSEMBLE
ubi = parsePDB('4gso+ligand.pdb', subset='calpha')
ensemble = Ensemble('4gso NMR ensemble')
ensemble.setCoords( ubi.getCoords() )
ensemble.addCoordset( ubi.getCoordsets() )
ubi_ensemble = Ensemble(ubi)
ubi_ensemble.iterpose()

## PCA
pca = PCA('4gso+ligand')
pca.buildCovariance(ubi_ensemble)
pca.calcModes()
for mode in pca[:20]:
    print(calcFractVariance(mode).round(2))
saveModel(pca)

## ANM
anm, atoms = calcANM(ubi, selstr='calpha')
anm = ANM('4gso+ligand')
anm.buildHessian(ubi)
anm.calcModes()
saveModel(anm)

##ENSEMBLE
slowest_mode = anm[0]
print( slowest_mode )
print( slowest_mode.getEigval().round(3) )
printOverlapTable(pca[:20], anm[:20])
writeNMD('4gso+ligant_pca.nmd', pca[:20], ubi)
writeArray('4gso+ligant_pca_modes.txt', pca.getArray(), format='%8.3f')
nma = parseModes(normalmodes='4gso_anm_slwevs.txt',eigenvalues='4gso_anm_eigvals.txt',nm_usecols=range(1,21), ev_usecols=[1], ev_usevalues=range(6,26))
nma.setTitle('4gso ANM')
slowmode = nma[1]
print(slowmode.getEigval().round(2))

plt.figure(0)
showOverlapTable(pca[:20], anm[:20]); #show1

#plt.figure(1)
#showSqFlucts(slowmode); #show2

plt.figure(2)
showOverlap(pca[0], anm); #show3

plt.figure(3)
showCumulOverlap(pca[0], anm, 'r'); #show4

plt.figure(4)
showSqFlucts(pca[:20]); #show 5
showSqFlucts(anm[:20]); #show 5

plt.figure(5)
showScaledSqFlucts(pca[0], anm[0]); #show6
legend(); #show 6

plt.figure(6)
showScaledSqFlucts(pca[1], anm[0]); #show7
legend(); #show 7

plt.figure(7)
showScaledSqFlucts(pca[19], anm[19]); #show8
legend(); #show 8

wait = input("PRESS ENTER TO FINISH.")
