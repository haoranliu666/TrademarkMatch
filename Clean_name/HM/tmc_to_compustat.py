import pandas as pd
import math

# registration -> gvkey, from HM
HM = pd.read_csv('/Users/haoranliu/match/Trademark/Original_data/Heath and Mace/heath_mace_tm_bridge.csv', header = 3)

registration_list = list(HM['tm_reg_num'])
gvkey_list = list(HM['gvkey'])

registration_gvkey = {}
for i in range(0, len(registration_list)):
    if math.isnan(gvkey_list[i]) == False:
        registration_gvkey[registration_list[i]] = gvkey_list[i]



# registration -> serial, from TMC casefile
tmc_serial_to_reg = pd.read_stata('/Users/haoranliu/match/Trademark/My_data/tmc_serial_to_reg.dta')

registration_list = list(tmc_serial_to_reg['registration_no'])
serial_list = list(tmc_serial_to_reg['serial_no'])

registration_serial = {}
for i in range(0, len(registration_list)):
    registration_serial[registration_list[i]] = serial_list[i]

# serial -> gvkey
serial_gvkey = {}
for i,j in registration_gvkey.items():
    serial_gvkey[registration_serial[i]] = j

serial_gvkey_stata = pd.DataFrame()
serial_gvkey_stata['serial_no'] = list(serial_gvkey.keys())
serial_gvkey_stata['gvkey'] = list(serial_gvkey.values())

serial_gvkey_stata.to_stata('/Users/haoranliu/match/Trademark/My_data/hm_serial_gvkey.dta', version = 117)
