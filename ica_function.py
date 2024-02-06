from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)

import mne

def ica_visualization(f, path):
    sample_data_folder = path # path to the .fif file 
    sample_data_raw_file = sample_data_folder+"/"+f
    raw = mne.io.read_raw_fif(sample_data_raw_file, preload= True)
    

    # Set up and fit the ICA
    raw.set_channel_types(mapping = {"Fz":"eog"}) 
    r_filter = raw.filter(l_freq = 1, h_freq = 100, picks = ["Fz", "C3", "Cz", "C4", "Pz", "PO7", "Oz", "PO8"]) 
    ica = ICA(n_components = 7, max_iter= "auto", random_state= 97) 
    ica.fit(raw)
       
        
    # Let the algorithm pick the eye artifacts:
    ica.exclude = []
    eog_indices, eog_scores = ica.find_bads_eog(raw, verbose = False)
    ica.exclude = eog_indices
    
    if eog_indices == []:
        print("****No ICA components to remove found****")
    else:
        print("****The ICA indices to remove are: {}. Removing them...****".format(eog_indices))
    

    # Plot components for visualisation
    ica.plot_components(verbose = False)
    
    # APPLY the ica model to the file 
    ica.apply(raw)


    # Save updated file:
    old_name = f
    
    if "Closed" in old_name:
        new_name = old_name[0:13]+"_ica.fif"
        raw.save(fname = "3. ICA/"+new_name, overwrite = True)
    else:
        new_name = old_name[0:11]+"_ica.fif"
        raw.save(fname = "3. ICA/"+new_name, overwrite = True)
        
    

