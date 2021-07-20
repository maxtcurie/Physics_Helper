from read_write_geometry import read_geometry_global

pars = init_read_parameters_file(suffix)

gpars,geometry = read_geometry_global(pars['magn_geometry'][1:-1]+suffix)

real_R=geometry['geo_R'] #it is major radius in meter
real_Z=geometry['geo_Z'] #it is height in meter, midland is 0, down is negative ,up is positive
    
gxx=geometry['gxx']
gxy=geometry['gxy']
gxz=geometry['gxz']
gyy=geometry['gyy']
gyz=geometry['gyz']
gzz=geometry['gzz']