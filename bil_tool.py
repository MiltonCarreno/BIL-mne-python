
from mne.io.ctf.ctf import read_raw_ctf

if __name__ == '__main__':
    test_data = "/Users/milton/Documents/MATLAB/Test_Dataset/sub-01_task-arrow_run-1.ds"
    p = read_raw_ctf(test_data)
    print("\n Length: " + str(len(p)))
    print("\n Type: " + str(type(p)))
    print("\n Returned value: " + str(p) + "\n\n")

    print("p[0]: ", p[0], "\n")
    print("Len p[0]: ", len(p[0]), "\n")

    print("Type p[0][0]: ", type(p[0][0]), "\n")
    print("Len p[0][0]: ", len(p[0][0]), "\n\n")
    print("Type p[0][1]: ", type(p[0][1]), "\n")
    print("Len p[0][1]: ", len(p[0][1]), "\n\n")

    print("len(p[0][0][0]): ", len(p[0][0][0]), "\n\n")

    # sampling_freq = p.info['sfreq']
    # start_stop_seconds = np.array([100, 110])
    # start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
    # channel_index = 70
    # raw_selection = p[channel_index, start_sample:stop_sample]
    # print(raw_selection)
    #
    # x = raw_selection[1]
    # y = raw_selection[0].T
    # plt.plot(x, y)
    # # plt.show()
    #
    # print(p.get_channel_types())
    #
    pi = p.info

    print("INFO keys: ", pi.keys(), "\n\n")
    print("Channel Names: ", pi.ch_names)
    
    print(type(pi), len(pi), pi)
    list_chs = pi["chs"]
    print("\n\n")
    print("len(chs): ", len(list_chs))
    print("\n\n")
    
    first_ch_keys = list_chs[0].keys()
    print("Channel info keys: ", first_ch_keys)
    print("Comps keys: ", pi["comps"][0].keys())
    print(len(pi["comps"]))

    print("n_times: ", p.n_times, "\n", p.times[-5:])

    # for x in pi:
    #     print(x, ": ", pi[x], "\n")
    # print("\n\n")
    #
    # channel_names = ['G11-2205', 'G12-2205']
    # two_meg_chans = p[channel_names, start_sample:stop_sample]
    # y_offset = np.array([5e-11, 0])  # just enough to separate the channel traces
    # x = two_meg_chans[1]
    # y = two_meg_chans[0].T + y_offset
    # lines = plt.plot(x, y)
    # plt.legend(lines, channel_names)
    # # plt.show()