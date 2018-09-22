import h5py
from astropy.io import fits

with h5py.File('false_postive_spectra_final.hdf5','r') as hf:

     info = hf["info"][:]
     pred_label = hf["pred_label"][:]
     true_label = hf["true_label"][:]
     z_info = hf["redshift"][:]
     ew2796_info = hf["ew2796"][:]
     ew2803_info = hf["ew2803"][:]
     check_info = hf["check_info"][:]

ra=info[:,0]
dec=info[:,1]
mjd=info[:,2]
plate=info[:,3]
fiber=info[:,4]
zqso=info[:,5]
SNR=info[:,6]


index = np.argwhere(check_info > 0.0)
index_pass_FP = index_plots_FP[:,0]

ra = ra[index_pass_FP]
dec = dec[index_pass_FP]
mjd = mjd [index_pass_FP]
plate =plate[index_pass_FP]
fiber =fiber[index_pass_FP]
zqso = zqso[index_pass_FP]
z_info = z_info[index_pass_FP]
ew2796_info = ew2796_info[index_pass_FP]
ew2803_info = ew2803_info[index_pass_FP]
