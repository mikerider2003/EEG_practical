from mne.time_frequency import tfr_multitaper
import numpy as np
import mne
import os


def tfr_analysis(l_open, l_closed, path_open, path_closed, nr_files, freq_range, fmin, fmax, channel):

    final_array_open = np.zeros((nr_files, 8, freq_range, 151)) 
    final_array_closed = np.zeros((nr_files, 8, freq_range, 151))

    freqs = np.arange(fmin, fmax, 1.)
    n_cycles = freqs / 2.

    sample_rate = 250
    

    for i in range(nr_files): 


        ################## for every OPEN EYES epoch:

        sample_data_folder = path_open # path to the .fif file 
        sample_data_raw_file = sample_data_folder+"/"+l_open[i]
        raw_open_eyes = mne.read_epochs(sample_data_raw_file, preload= True, verbose = False)

        # power analysis:
                
        power_open = tfr_multitaper(raw_open_eyes, picks = channel , freqs = freqs, n_cycles = n_cycles, decim = 10, return_itc=False, average = True )
        final_array_open[i] = power_open.data


        ################## for every CLOSED EYES epoch:

        sample_data_folder = path_closed # path to the .fif file 
        sample_data_raw_file = sample_data_folder+"/"+l_closed[i]
        raw_closed_eyes = mne.read_epochs(sample_data_raw_file, preload= True, verbose = False)

        # power analysis:

        power_closed = tfr_multitaper(raw_closed_eyes, picks = channel , freqs = freqs, n_cycles = n_cycles, decim = 10, return_itc=False, average = True )
        final_array_closed[i] = power_closed.data

    ##### EXIT LOOP

    final_to_plot_open_eyes = np.mean(final_array_open, axis = 0 ) # average across files
    final_to_plot_closed_eyes = np.mean(final_array_closed, axis = 0 ) # average across files

    
    return [final_to_plot_open_eyes, final_to_plot_closed_eyes]