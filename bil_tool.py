
from mne.io.ctf.ctf import read_raw_ctf

def extract_data(dataPath, divert=False):

    test_data = "/Users/milton/Documents/MATLAB/Test_Dataset/sub-01_task-arrow_run-3.ds"
    p = read_raw_ctf(test_data)
    pi = p.info

    if divert:
        print("RAW: ", p._raw_extras)
        print("\n Length: " + str(len(p)))
        print("\n Type: " + str(type(p)))
        print("\n Returned value: " + str(p) + "\n\n")

        print("p[x]: ", p[304])

        print("p[0]: ", p[0], "\n")
        print("Len p[0]: ", len(p[0]), "\n")

        print("************************************")
        print("Type p[0][0]: ", type(p[0][0]), "\n")
        print("Len p[0][0]: ", len(p[0][0]), "\n")
        print("p[0][0]: ", p[0][0], "\n")
        print("len(p[0][0][0]): ", len(p[0][0][0]), "\n")
        print("************************************")
        print("Type p[0][1]: ", type(p[0][1]), "\n")
        print("Len p[0][1]: ", len(p[0][1]), "\n")
        print("p[0][1]: ", p[0][1], "\n")
        print("************************************")
        q = p[0][1][5999] - p[0][1][0]
        print("Last - first: ", q)

        print("INFO keys: ", pi.keys(), "\n\n")
        # print("Channel Names: ", pi.ch_names)
        
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
    else:
        d = pi["meas_date"]

        # Dictionary containing desired data
        datus = {}

        setup = {}
        setup["date"] = (str(d.month) + "/" + str(d.day) + "/" + str(d.year))
        setup["time"] = (str(d.hour) + ":" + str(d.minute))
        setup["number_samples"] = p._raw_extras[0]["block_size"]
        setup["number_channels"] = pi["nchan"]
        setup["sample_rate"] = pi["sfreq"]
        setup["sample_msec"] = p[0][1][1] * 1000
        setup["sample_sec"] = p[0][1][1]
        setup["number_trials"] = p._raw_extras[0]["n_samp_tot"] / p._raw_extras[0]["block_size"]
        setup["duration_trial"] = round(p.times[5999])
        setup["duration_total"] = setup["duration_trial"] * setup["number_trials"]
        setup["subject"] = pi["subject_info"]["his_id"]
        setup["start_msec"] = 0
        setup["end_msec"] = p.times[5999] * 1000
        setup["start_sec"] = 0
        setup["end_sec"] = p.times[5999]
        setup["time_sec"] = p.times[:6000]
        print("Setup: ", setup)
        
        datus["setup"] = setup
        datus["data"] = {}


if __name__ == '__main__':
    test_data = "/Users/milton/Documents/MATLAB/Test_Dataset/sub-01_task-arrow_run-3.ds"
    p = read_raw_ctf(test_data)
    print("RAW: ", p._raw_extras)
    print("\n Length: " + str(len(p)))
    print("\n Type: " + str(type(p)))
    print("\n Returned value: " + str(p) + "\n\n")

    print("p[x]: ", p[304])

    print("p[0]: ", p[0], "\n")
    print("Len p[0]: ", len(p[0]), "\n")

    print("************************************")
    print("Type p[0][0]: ", type(p[0][0]), "\n")
    print("Len p[0][0]: ", len(p[0][0]), "\n")
    print("p[0][0]: ", p[0][0], "\n")
    print("len(p[0][0][0]): ", len(p[0][0][0]), "\n")
    print("************************************")
    print("Type p[0][1]: ", type(p[0][1]), "\n")
    print("Len p[0][1]: ", len(p[0][1]), "\n")
    print("p[0][1]: ", p[0][1], "\n")
    print("************************************")
    q = p[0][1][5999] - p[0][1][0]
    print("Last - first: ", q)

    pi = p.info

    print("INFO keys: ", pi.keys(), "\n\n")
    # print("Channel Names: ", pi.ch_names)
    
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

    # print("date: ", type(pi["meas_date"]))
    d = pi["meas_date"]

    # Dictionary containing desired data
    datus = {}

    setup = {}
    setup["date"] = (str(d.month) + "/" + str(d.day) + "/" + str(d.year))
    setup["time"] = (str(d.hour) + ":" + str(d.minute))
    setup["number_samples"] = p._raw_extras[0]["block_size"]
    setup["number_channels"] = pi["nchan"]
    setup["sample_rate"] = pi["sfreq"]
    setup["sample_msec"] = p[0][1][1] * 1000
    setup["sample_sec"] = p[0][1][1]
    setup["number_trials"] = p._raw_extras[0]["n_samp_tot"] / p._raw_extras[0]["block_size"]
    setup["duration_trial"] = round(p.times[5999])
    setup["duration_total"] = setup["duration_trial"] * setup["number_trials"]
    setup["subject"] = pi["subject_info"]["his_id"]
    setup["start_msec"] = 0
    setup["end_msec"] = p.times[5999] * 1000
    setup["start_sec"] = 0
    setup["end_sec"] = p.times[5999]
    setup["time_sec"] = p.times[:6000]
    print("Setup: ", setup)
    
    datus["setup"] = setup
    datus["data"] = {}


