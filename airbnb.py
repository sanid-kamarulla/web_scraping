import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.airbnb.co.in/s/Nagpur--Maharashtra/homes?adults=2&place_id=ChIJE68fo6XA1DsRKz670AZ9sxk&tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Nagpur%2C%20Maharashtra&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&federated_search_session_id=2d395441-457e-4ae6-8348-b77bdb34445d&cursor=eyJzZWN0aW9uX29mZnNldCI6MCwiaXRlbXNfb2Zmc2V0IjowLCJ2ZXJzaW9uIjoxfQ%3D%3D"

while True:
    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    np_link = soup.find("a", class_ = "l1ovpqvx atm_1y33qqm_1ggndnn_10saat9 atm_17zvjtw_zk357r_10saat9 atm_w3cb4q_il40rs_10saat9 c1ytbx3a atm_mk_h2mmj6 atm_9s_1txwivl atm_h_1h6ojuz atm_fc_1h6ojuz atm_bb_idpfg4 atm_26_1j28jx2 atm_3f_glywfm atm_7l_18pqv07 atm_gi_idpfg4 atm_l8_idpfg4 atm_uc_1dtz4sb atm_kd_glywfm atm_gz_xvenqj atm_uc_glywfm__p88qr9 atm_26_1nh1gcj_1rqz0hn_uv4tnr atm_tr_kv3y6q_csw3t1 atm_26_1nh1gcj_1ul2smo atm_3f_glywfm_jo46a5 atm_l8_idpfg4_jo46a5 atm_gi_idpfg4_jo46a5 atm_3f_glywfm_1icshfk atm_kd_glywfm_19774hq atm_70_glywfm_1w3cfyq atm_uc_x37zl0_9xuho3 atm_70_216vci_9xuho3 atm_26_1nh1gcj_9xuho3 atm_uc_glywfm_9xuho3_p88qr9 atm_70_glywfm_18zk5v0 atm_uc_x37zl0_fiqcvf atm_70_216vci_fiqcvf atm_26_1nh1gcj_fiqcvf atm_uc_glywfm_fiqcvf_p88qr9 atm_7l_161hw1_1o5j5ji atm_9j_13gfvf7_1o5j5ji atm_26_1j28jx2_154oz7f atm_92_1yyfdc7_vmtskl atm_9s_1ulexfb_vmtskl atm_mk_stnw88_vmtskl atm_tk_1ssbidh_vmtskl atm_fq_1ssbidh_vmtskl atm_tr_pryxvc_vmtskl atm_vy_1vi7ecw_vmtskl atm_e2_1vi7ecw_vmtskl atm_5j_1ssbidh_vmtskl atm_mk_h2mmj6_1ko0jae dir dir-ltr").get("href")
    full_nplink = "https://www.airbnb.co.in" + np_link
    url = full_nplink
    print(url)

