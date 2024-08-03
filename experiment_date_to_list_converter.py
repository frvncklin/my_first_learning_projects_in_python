# Convertendo data em mês e ano;

#data = "XXXX - XX - XX"

def convert_data_str_to_mounth_year_day_list(data):

    data = data.replace(' ', '').replace('-', '').strip()
    year = data[0:4]
    mounth = data[4:6]
    day = data[6:]
    return [year, mounth, day]

data = '2004-05-15'

data = convert_data_str_to_mounth_year_day_list(data)
print(data)