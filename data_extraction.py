import os
import json
import pandas as pd

path="/home/kishore/phone-pe pulse/pulse/data/aggregated/transaction/country/india/state/"


def Aggregated_transaction(path):
    

    Agg_state_list=os.listdir(path)
    Agg_state_list
    clm={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

    for i in Agg_state_list:
        p_i=path+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                data=open(p_k,'r')
                d=json.load(data)

                for z in d['data']['transactionData']:
                    Name = z['name']
                    count = z['paymentInstruments'][0]['count']
                    amount = z['paymentInstruments'][0]['amount']
                    clm['Transaction_type'].append(Name)
                    clm['Transaction_count'].append(count)
                    clm['Transaction_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))

    Agg_Trans = pd.DataFrame(clm)
    print(Agg_Trans)

    

# def Aggregated_users(path):
#     path="/home/kishore/phone-pe pulse/pulse/data/aggregated/user/country/india/state/"

#     Agg_state_list=os.listdir(path)
#     Agg_state_list
#     # clm={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}
#     device_data = {
#         'State': [], 'Year': [], 'Quarter': [],
#         'Device_Brand': [], 'User_Count': []
#     }
#     for i in Agg_state_list:
#         p_i=path+i+"/"
#         Agg_yr=os.listdir(p_i)
#         for j in Agg_yr:
#             p_j=p_i+j+"/"
#             Agg_yr_list=os.listdir(p_j)
#             for k in Agg_yr_list:
#                 p_k=p_j+k
#                 data=open(p_k,'r')
#                 d=json.load(data)

#                 users = d['data'].get('usersByDevice')

#                 # for z in d['data']['usersByDevice']:
#                 #     brand = z['brand']
#                 if users:  # skip if it's None
#                         for user in users:
#                             device_data['State'].append(i)
#                             device_data['Year'].append(j)
#                             device_data['Quarter'].append(int(k.strip('.json')))
#                             device_data['Device_Brand'].append(user['brand'])
#                             device_data['User_Count'].append(user['count'])

#     # Convert to DataFrame
#     Agg_User_By_Device = pd.DataFrame(device_data)


# def Aggregated_insurance(path):
#     path = "/home/kishore/phone-pe pulse/pulse/data/aggregated/insurance/country/india/state/"
#     state_list = os.listdir(path)

#     insurance_data = {
#         'State': [], 'Year': [], 'Quarter': [],
#         'Insurance_Type': [], 'Transaction_Count': [], 'Transaction_Amount': []
#     }

#     for state in state_list:
#         p_state= os.path.join(path, state)
#         agg_yr= os.listdir(p_state)

#         for year in agg_yr:
#             p_year= os.path.join(p_state, year)
#             agg_quarter= os.listdir(p_year)

#             for file in agg_quarter:
#                 p_file= os.path.join(p_year, file)
#                 with open(p_file,'r') as f:
#                     data = json.load(f)
#                     trans_data = data['data'].get('transactionData')
#                     if trans_data:
#                         for entry in trans_data:
#                             insurance_data['State'].append(state)
#                             insurance_data['Year'].append(year)
#                             insurance_data['Quarter'].append(int(file.strip('.json')))
#                             insurance_data['Insurance_Type'].append(entry['name'])
#                             insurance_data['Transaction_Count'].append(entry['paymentInstruments'][0]['count'])
#                             insurance_data['Transaction_Amount'].append(entry['paymentInstruments'][0]['amount'])
                            
#     Agg_Insurance = pd.DataFrame(insurance_data)

# print("success")