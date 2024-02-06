import mne

def epoching(f, path):
    sample_data_folder = path # path to the .fif file 
    sample_data_raw_file = sample_data_folder+"/"+f # extract the raw file
    r = mne.io.read_raw_fif(sample_data_raw_file, preload= False, on_split_missing = "warn") # this function is to reads .fif file
      
    
    # EXTRACT "CLOSED EYES" MARKER EPOCH ---------------------------
    
    if "Closed_Eyes" in f:
        events, event_dict_closed_eyes = mne.events_from_annotations(r, event_id =  "auto", verbose = False)  


        # Creating epoch files from important event triggers:
        epoch_closed_eyes = mne.Epochs(r, events, event_id = event_dict_closed_eyes, baseline = (None, 0), tmin = -1, tmax = 5, verbose = True, preload = True) 

        # Savinng the "closed eyes" epoched file
        epoch_closed_eyes.save("4. Epoch/Closed/"+ f[0:13] + "-closed_eyes"+"_epo.fif", overwrite = True)

       # EXTRACT "OPEN EYES" MARKER EPOCH ---------------------------
    
    if "Open_Eyes" in f:
     
        events, event_dict_open_eyes = mne.events_from_annotations(r, event_id =  "auto", verbose = False)  

        # Creating epoch files from important event triggers:
        epoch_open_eyes = mne.Epochs(r, events, event_id = event_dict_open_eyes, baseline = (None, 0), tmin = -1, tmax = 5, verbose = True,  preload = True)

        # Savinng the "openn eyes" epoched file
        epoch_open_eyes.save("4. Epoch/Open/"+ f[0:11] + "-open_eyes"+"_epo.fif",overwrite = True)

