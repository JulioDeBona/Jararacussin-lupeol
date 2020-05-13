#developed by Julio De Bona

#SETUP ENVIROMENT

from prody import *
from pylab import *
ion()
structure = parsePDB('md_100_noligand.pdb')

#EDA CALCULATIONS FOR LARGE TRAJECTORY
ensemble = parseDCD('md_noligand.dcd')
ensemble.setCoords(structure)
ensemble.setAtoms(structure.calpha)
ensemble.superpose()
eda_ensemble = EDA('MD Ensemble')
eda_ensemble.buildCovariance( ensemble )
eda_ensemble.calcModes()

dcd = DCDFile('md_noligand.dcd')
dcd.link(structure)
dcd.setAtoms(structure.calpha)
eda_trajectory = EDA('MD Trajectory')
eda_trajectory.buildCovariance( dcd )
eda_trajectory.calcModes()

printOverlapTable(eda_ensemble[:2], eda_trajectory[:2])

trajectory = Trajectory('md_noligand.dcd')
trajectory.addFile('md_noligand.dcd')
trajectory.link(structure)
trajectory.setCoords(structure)
trajectory.setAtoms(structure.calpha)
eda = EDA('md')
eda.buildCovariance( trajectory )
eda.calcModes()
saveModel(eda)

#PLOTTING

mdm2ca_sim1 = trajectory[:250]
mdm2ca_sim1.superpose()
mdm2ca_sim2 = trajectory[250:]
mdm2ca_sim2.superpose()
# We project independent trajectories in different color
showProjection(mdm2ca_sim2, eda[:3], color='red', marker='.');
# Now let's mark the beginning of the trajectory with a circle
showProjection(mdm2ca_sim2[0], eda[:3], color='red', marker='o', ms=12);
# Now let's mark the end of the trajectory with a square
showProjection(mdm2ca_sim2[-1], eda[:3], color='red', marker='s', ms=12);

structure = parsePDB('4gso+ligand.pdb')

#EDA CALCULATIONS FOR LARGE TRAJECTORY
ensemble = parseDCD('md_100-ligand.dcd')
ensemble.setCoords(structure)
ensemble.setAtoms(structure.calpha)
ensemble.superpose()
eda_ensemble = EDA('MD Ensemble')
eda_ensemble.buildCovariance( ensemble )
eda_ensemble.calcModes()

dcd = DCDFile('md_100-ligand.dcd')
dcd.link(structure)
dcd.setAtoms(structure.calpha)
eda_trajectory = EDA('MD Trajectory')
eda_trajectory.buildCovariance( dcd )
eda_trajectory.calcModes()

trajectory = Trajectory('md_100-ligand.dcd')
trajectory.addFile('md_100-ligand.dcd')
trajectory.link(structure)
trajectory.setCoords(structure)
trajectory.setAtoms(structure.calpha)
eda = EDA('md')
eda.buildCovariance( trajectory )
eda.calcModes()
saveModel(eda)

mdm2ca_sim1 = trajectory[:250]
mdm2ca_sim1.superpose()
mdm2ca_sim2 = trajectory[250:]
mdm2ca_sim2.superpose()
# We project independent trajectories in different color
showProjection(mdm2ca_sim2, eda[:3], color='blue', marker='.');
# Now let's mark the beginning of the trajectory with a circle
showProjection(mdm2ca_sim2[0], eda[:3], color='blue', marker='o', ms=12);
# Now let's mark the end of the trajectory with a square
showProjection(mdm2ca_sim2[-1], eda[:3], color='blue', marker='s', ms=12);

wait = input("PRESS ENTER TO FINISH.")
