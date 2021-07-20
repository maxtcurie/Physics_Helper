from parIOWrapper import init_read_parameters_file
from nrgWrapper import read_from_nrg_files
from nrgWrapper import read_Gamma_Q


setTime=-1
suffix='_0001'

pars = init_read_parameters_file(suffix)

time, nrgi, nrge, nrgz = read_from_nrg_files(pars,suffix,False)

Gamma_es, Gamma_em, Q_es, Q_em = \
	read_Gamma_Q(time,nrg,False,setTime)

Gamma = Gamma_es + Gamma_em
Qtot = Q_es + Q_em
#Qtot = Qtot - 5./3.*Gamma
Qtot = Qtot - 3./2.*Gamma*T
Qes = Q_es - 3./2.*Gamma_es*T
Qem = Q_em - 3./2.*Gamma_em*T
D = Gamma / omn / n
chi = Qtot / omt / n / T
Dochi = Gamma/Qtot*omt/omn*T




