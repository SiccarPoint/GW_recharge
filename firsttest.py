from landlab import RasterModelGrid, imshow_grid_at_node
from landlab.components import FlowAccumulator
from landlab.components import SpatialPrecipitationDistribution
from landlab.components import SoilInfiltrationGreenAmpt
from matplotlib.pyplot import show, figure

mg = RasterModelGrid((100, 100), 100.)
z = mg.add_zeros('node', 'topographic__elevation', dtype=float)
z[:] = mg.node_x/100000.

STORM = SpatialPrecipitationDistribution(mg)
WUFI = mg.add_field('node', 'water__unit_flux_in',
                    mg.at_node['rainfall__flux'])
fa = FlowAccumulator(mg)

count = 0
for storm in STORM.yield_storms():
    fa.run_one_step()
    print storm
    count += 1
    if count % 10 == 0:
        figure(count)
        imshow_grid_at_node(mg, 'rainfall__flux')
        figure(count+1)
        imshow_grid_at_node(mg, 'surface_water__discharge')

show()
