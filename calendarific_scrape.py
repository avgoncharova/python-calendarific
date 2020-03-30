import calendarific
import pandas as pd
# from datetime import datetime
import numpy as np

# countries = ['af', 'al', 'dz', 'as', 'ad', 'ao', 'ai', 'ag', 'ar', 'am', 'aw', 'au', 'at', 'az', 'bh', 'bd', 'bb', 'by', 'be', 'bz', 'bj', 'bm', 'bt', 'bo', 'ba', 'bw', 'br', 'vg', 'bn', 'bg', 'bf', 'bi', 'cv', 'kh', 'cm', 'ca', 'ky', 'cf', 'td', 'cl', 'cn', 'co', 'km', 'cg', 'cd', 'ck', 'cr', 'ci', 'hr', 'cu', 'cw', 'cy', 'cz', 'dk', 'dj', 'dm', 'do', 'tl', 'ec', 'eg', 'sv', 'gq', 'er', 'ee', 'et', 'fk', 'fo', 'fj', 'fi', 'fr', 'pf', 'ga', 'gm', 'ge', 'de', 'gh', 'gi', 'gr', 'gl', 'gd', 'gu', 'gt', 'gg', 'gn', 'gw', 'gy', 'ht', 'va', 'hn', 'hk', 'hu', 'is', 'in', 'id', 'ir', 'iq', 'ie', 'im', 'il', 'it', 'jm', 'jp', 'je', 'jo', 'kz', 'ke', 'ki', 'xk', 'kw', 'kg', 'la', 'lv', 'lb', 'ls',
#              'lr', 'ly', 'li', 'lt', 'lu', 'mo', 'mg', 'mw', 'my', 'mv', 'ml', 'mt', 'mh', 'mq', 'mr', 'mu', 'yt', 'mx', 'fm', 'md', 'mc', 'mn', 'me', 'ms', 'ma', 'mz', 'mm', 'na', 'nr', 'np', 'nl', 'nc', 'nz', 'ni', 'ne', 'ng', 'kp', 'mk', 'mp', 'no', 'om', 'pk', 'pw', 'pa', 'pg', 'py', 'pe', 'ph', 'pl', 'pt', 'pr', 'qa', 're', 'ro', 'ru', 'rw', 'sh', 'kn', 'lc', 'mf', 'pm', 'vc', 'ws', 'sm', 'st', 'sa', 'sn', 'rs', 'sc', 'sl', 'sg', 'sx', 'sk', 'si', 'sb', 'so', 'za', 'kr', 'ss', 'es', 'lk', 'bl', 'sd', 'sr', 'se', 'ch', 'sy', 'tw', 'tj', 'tz', 'th', 'bs', 'tg', 'to', 'tt', 'tn', 'tr', 'tm', 'tc', 'tv', 'vi', 'ug', 'ua', 'ae', 'gb', 'us', 'uy', 'uz', 'vu', 've', 'vn', 'wf', 'ye', 'zm', 'zw', 'sz']

# 'us': 'United States'
countries = {'al': 'Albania', 'dz': 'Algeria', 'as': 'American Samoa', 'ad': 'Andorra', 'ao': 'Angola', 'ai': 'Anguilla', 'ag': 'Antigua and Barbuda', 'ar': 'Argentina', 'am': 'Armenia', 'aw': 'Aruba', 'au': 'Australia', 'at': 'Austria', 'az': 'Azerbaijan', 'bh': 'Bahrain', 'bd': 'Bangladesh', 'bb': 'Barbados', 'by': 'Belarus', 'be': 'Belgium', 'bz': 'Belize', 'bj': 'Benin', 'bm': 'Bermuda', 'bt': 'Bhutan', 'bo': 'Bolivia', 'ba': 'Bosnia and Herzegovina', 'bw': 'Botswana', 'br': 'Brazil', 'vg': 'British Virgin Islands', 'bn': 'Brunei', 'bg': 'Bulgaria', 'bf': 'Burkina Faso', 'bi': 'Burundi', 'cv': 'Cabo Verde', 'kh': 'Cambodia', 'cm': 'Cameroon', 'ca': 'Canada', 'ky': 'Cayman Islands', 'cf': 'Central African Republic', 'td': 'Chad', 'cl': 'Chile', 'cn': 'China', 'co': 'Colombia', 'km': 'Comoros', 'cg': 'Congo', 'cd': 'Congo Democratic Republic', 'ck': 'Cook Islands', 'cr': 'Costa Rica', 'ci': "Cote d'Ivoire", 'hr': 'Croatia', 'cu': 'Cuba', 'cw': 'Curaçao', 'cy': 'Cyprus', 'cz': 'Czech Republic', 'dk': 'Denmark', 'dj': 'Djibouti', 'dm': 'Dominica', 'do': 'Dominican Republic', 'tl': 'East Timor', 'ec': 'Ecuador', 'eg': 'Egypt', 'sv': 'El Salvador', 'gq': 'Equatorial Guinea', 'er': 'Eritrea', 'ee': 'Estonia', 'et': 'Ethiopia', 'fk': 'Falkland Islands', 'fo': 'Faroe Islands', 'fj': 'Fiji', 'fi': 'Finland', 'fr': 'France', 'pf': 'French Polynesia', 'ga': 'Gabon', 'gm': 'Gambia', 'ge': 'Georgia', 'de': 'Germany', 'gh': 'Ghana', 'gi': 'Gibraltar', 'gr': 'Greece', 'gl': 'Greenland', 'gd': 'Grenada', 'gu': 'Guam', 'gt': 'Guatemala', 'gg': 'Guernsey', 'gn': 'Guinea', 'gw': 'Guinea-Bissau', 'gy': 'Guyana', 'ht': 'Haiti',
             'va': 'Holy See (Vatican City)', 'hn': 'Honduras', 'hk': 'Hong Kong', 'hu': 'Hungary', 'is': 'Iceland', 'in': 'India', 'id': 'Indonesia', 'ir': 'Iran', 'iq': 'Iraq', 'ie': 'Ireland', 'im': 'Isle of Man', 'il': 'Israel', 'it': 'Italy', 'jm': 'Jamaica', 'jp': 'Japan', 'je': 'Jersey', 'jo': 'Jordan', 'kz': 'Kazakhstan', 'ke': 'Kenya', 'ki': 'Kiribati', 'xk': 'Kosovo', 'kw': 'Kuwait', 'kg': 'Kyrgyzstan', 'la': 'Laos', 'lv': 'Latvia', 'lb': 'Lebanon', 'ls': 'Lesotho', 'lr': 'Liberia', 'ly': 'Libya', 'li': 'Liechtenstein', 'lt': 'Lithuania', 'lu': 'Luxembourg', 'mo': 'Macau', 'mg': 'Madagascar', 'mw': 'Malawi', 'my': 'Malaysia', 'mv': 'Maldives', 'ml': 'Mali', 'mt': 'Malta', 'mh': 'Marshall Islands', 'mq': 'Martinique', 'mr': 'Mauritania', 'mu': 'Mauritius', 'yt': 'Mayotte', 'mx': 'Mexico', 'fm': 'Micronesia', 'md': 'Moldova', 'mc': 'Monaco', 'mn': 'Mongolia', 'me': 'Montenegro', 'ms': 'Montserrat', 'ma': 'Morocco', 'mz': 'Mozambique', 'mm': 'Myanmar', 'na': 'Namibia', 'nr': 'Nauru', 'np': 'Nepal', 'nl': 'Netherlands', 'nc': 'New Caledonia', 'nz': 'New Zealand', 'ni': 'Nicaragua', 'ne': 'Niger', 'ng': 'Nigeria', 'kp': 'North Korea', 'mk': 'North Macedonia', 'mp': 'Northern Mariana Islands', 'no': 'Norway', 'om': 'Oman', 'pk': 'Pakistan', 'pw': 'Palau', 'pa': 'Panama', 'pg': 'Papua New Guinea', 'py': 'Paraguay', 'pe': 'Peru', 'ph': 'Philippines', 'pl': 'Poland', 'pt': 'Portugal', 'pr': 'Puerto Rico', 'qa': 'Qatar', 're': 'Reunion', 'ro': 'Romania', 'ru': 'Russia', 'rw': 'Rwanda', 'sh': 'Saint Helena', 'kn': 'Saint Kitts and Nevis', 'lc': 'Saint Lucia', 'mf': 'Saint Martin', 'pm': 'Saint Pierre and Miquelon', 'vc': 'Saint Vincent and the Grenadines', 'ws': 'Samoa', 'sm': 'San Marino', 'st': 'Sao Tome and Principe', 'sa': 'Saudi Arabia', 'sn': 'Senegal', 'rs': 'Serbia', 'sc': 'Seychelles', 'sl': 'Sierra Leone', 'sg': 'Singapore', 'sx': 'Sint Maarten', 'sk': 'Slovakia', 'si': 'Slovenia', 'sb': 'Solomon Islands', 'so': 'Somalia', 'za': 'South Africa', 'kr': 'South Korea', 'ss': 'South Sudan', 'es': 'Spain', 'lk': 'Sri Lanka', 'bl': 'St. Barts', 'sd': 'Sudan', 'sr': 'Suriname', 'se': 'Sweden', 'ch': 'Switzerland', 'sy': 'Syria', 'tw': 'Taiwan', 'tj': 'Tajikistan', 'tz': 'Tanzania', 'th': 'Thailand', 'bs': 'The Bahamas', 'tg': 'Togo', 'to': 'Tonga', 'tt': 'Trinidad and Tobago', 'tn': 'Tunisia', 'tr': 'Turkey', 'tm': 'Turkmenistan', 'tc': 'Turks and Caicos Islands', 'tv': 'Tuvalu', 'vi': 'US Virgin Islands', 'ug': 'Uganda', 'ua': 'Ukraine', 'ae': 'United Arab Emirates', 'gb': 'United Kingdom', 'us': 'United States', 'uy': 'Uruguay', 'uz': 'Uzbekistan', 'vu': 'Vanuatu', 've': 'Venezuela', 'vn': 'Vietnam', 'wf': 'Wallis and Futuna', 'ye': 'Yemen', 'zm': 'Zambia', 'zw': 'Zimbabwe', 'sz': 'eSwatini'}
omit_holiday = {'Clock change/Daylight Saving Time', 'Common local holiday', 'Local holiday', 'Local observance',
                'Season', 'Worldwide observance', 'United Nations observance'}

calapi = calendarific.v2('553fbfa98c58d7940930e4aad6be0c4dc4764ed7')
for i in countries:
    parameters = {
        # Required
        'country': i,
        'year':    2021,
    }

    holidays = calapi.holidays(parameters)

    holiday_no = len(holidays['response']['holidays'])
    holiday_names = []
    holiday_dates = []
    holiday_descriptions = []
    holiday_types = []

    for j in range(0, holiday_no):
        if (holidays['response']['holidays'][j]['type'][0] not in omit_holiday):
            date = str(holidays['response']['holidays'][j]['date']['datetime']['year']) + \
                "-" + str(holidays['response']['holidays'][j]['date']
                          ['datetime']['month']).zfill(2) + \
                "-" + str(holidays['response']['holidays']
                          [j]['date']['datetime']['day']).zfill(2)
            holiday_names.append(holidays['response']['holidays'][j]['name'])
            holiday_dates.append(date)
            holiday_descriptions.append(
                holidays['response']['holidays'][j]['description'])
            holiday_types.append(holidays['response']['holidays'][j]['type'])

    d = {'country': countries[i],
         'holiday_names': holiday_names,
         'holiday_date': holiday_dates,
         'holiday_types': holiday_types,
         'holiday_descriptions': holiday_descriptions}

    holiday_df = pd.DataFrame(data=d)
    holiday_df = pd.DataFrame(np.unique(holiday_df),
                              columns=holiday_df.columns)
    # holiday_df = pd.DataFrame(holiday_df, columns=holiday_df.columns)

    holiday_df.to_csv("holidays_by_country.csv",
                      mode='a', encoding="utf-8")
