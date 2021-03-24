import matplotlib.pyplot as plt
import numpy as np
Q2Reg = 200.
EProton = 920.
epString = '920'

Q2Bins = [200.,250.,350.,450.,650.,800.,1200.,1500.,2000.,3000.,5000.,8000.,12000.,20000.,30000.]

for Q2Reg in Q2Bins:
	# variables that hold for the whole plot/data included here
	print(Q2Reg)
	#Plot HERA data:
	#this is combined data
	fig, ax = plt.subplots(1,1,figsize=(10,10))

	source = '/temp_local/mov57924/myPythia/pythia8303/HERAData/herapdf_tables_150323/HERA1+2_NCep_' + epString + '.dat'
	data = np.loadtxt(source)
	#length of the data tables:
	#920 -> 485 
	#820 -> 111
	#575 -> 259
	#460 -> 209
	ZeileA = 0
	ZeileO = 485


	nTable_xBjorken = 1
	nTable_sigma = 3
	nTable_Q2 = 0


	for i in range(ZeileA,ZeileO):
		xB = data[i,nTable_xBjorken]
		sigma = data[i,nTable_sigma]
		Q2 = data[i,nTable_Q2]
		if(Q2==Q2Reg):
			dataPoints, = ax.plot( xB, sigma, 'r X')
			#print("x " + str(x) +" sigma: "+str(sigma))

	#DESY-02-113
	if(EProton==920.):
		source = '/temp_local/mov57924/myPythia/pythia8303/HERAData/DESY-02-113.dat'
		data = np.loadtxt(source)
		nTable_xBjorken = 5
		nTable_sigma = 6
		nTable_Q2 = 2
		
		Q2 = data[:,nTable_Q2]
		xB = data[:,nTable_xBjorken]
		xB_P = xB[Q2==Q2Reg]
		sigma = data[:,nTable_sigma]
		sigma_P = sigma[Q2==Q2Reg]
		
		
		dataPointsDESY02133, = ax.plot( xB_P, sigma_P, 'y X')
		
	#This is ZEUS+H1 data
	"""
	source = '/temp_local/mov57924/myPythia/pythia8303/HERAData/HERA_DataFromCSV_Formate/HEPData-ins1377206-v1-Table_5.csv'
	data = np.loadtxt(source)

	ZeileA = 0
	ZeileO = 159

	nTable_xBjorken = 1
	nTable_sigma = 2
	nTable_Q2 = 0


	for i in range(ZeileA,ZeileO):
		#print(data[i,0]-Q2reg)
		xB = data[i,nTable_xBjorken]
		sigma = data[i,nTable_sigma]
		Q2 = data[i,nTable_Q2]
		#print(Q2,Q2Reg)
		if(Q2==Q2Reg):
			dataPointsZeusandH1, = ax.plot( xB, sigma, 'b X')
	"""
	
	
	#This is H1 data
	"""
	source = '/temp_local/mov57924/myPythia/pythia8303/HERAData/HERA_DataFromCSV_Formate/HEPData-ins539088-v1-Table_6.csv'
	data = np.loadtxt(source)

	ZeileA = 0
	ZeileO = 126

	nTable_xBjorken = 1
	nTable_sigma = 2
	nTable_Q2 = 0


	for i in range(ZeileA,ZeileO):
		#print(data[i,0]-Q2reg)
		xB = data[i,nTable_xBjorken]
		sigma = data[i,nTable_sigma]
		Q2 = data[i,nTable_Q2]
		#print(Q2,Q2Reg)
		if(Q2==Q2Reg):
			dataPointsH1, = ax.plot( xB, sigma, 'y X')
	
	"""
			
	#Very good. Now I plot my own data.
	#Compare old v1 to new v2
	#v1:
	"""
	#simgaR
	source = '/temp_local/mov57924/myPythia/pythia8303/Datafiles/v1/920/Q2='+str(Q2Reg)+'00000_sR.dat'
	data = np.loadtxt(source)
	xB = data[:,0]
	sigma = data[:,1]

	sigmaR, = ax.step(xB, sigma, 'k-')	
	"""

	#v2:
	source = '/temp_local/mov57924/myPythia/pythia8303/Datafiles/v2/'+epString+'/EP='+epString+'.000000Q2='+str(Q2Reg)+'00000_sR.dat'
	data = np.loadtxt(source)
	
	xB = data[:,1] #upper limit of bin. like this values are ok.
	sigma = data[:,5]
	sigmaR, = ax.step(xB, sigma, 'k-')






	if(EProton==920.):
		dataPointsDESY02133.set_label('DESY-02-133')
	dataPoints.set_label('Data Points HERA combined')
	#dataPointsH1.set_label('Data Points HERA H1')
	#dataPointsZeusandH1.set_label('Data Points HERA ZEUS+H1')
	sigmaR.set_label(r'Pythia8-$\sigma_R$-')

	ax.legend()


	ax.set_xlabel(r'$x$')
	ax.set_ylabel(r'$\sigma^{-}_{r,NC}(x,Q^2=$'+str(Q2Reg)+r'$)$')
	ax.set_title('DIS ' + r'$e^-~p$ collision, $E_p = $' + epString + '$\, GeV$, $E_{e^-} = 27.5\,GeV$,  $\~{} 10^8$ Events')
	ax.set_xscale('log')

	plt.savefig('/temp_local/mov57924/myPythia/pythia8303/myPlots/v1-v2Plots/EP='+epString+'Q2='+str(Q2Reg)+'.png',dpi=300, bbox_inches='tight')
	#plt.show()
