if __name__ == '__main__':
    print('Hello Wereld')

import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=SQLExpress;DATABASE=WifiMonitor')
cursor = cnxn.cursor()
cursor.execute("select PersonId, LastName from users")
rows = cursor.fetchall()
for row in rows:
    print row.PersonId, row.LastName
    

import fritzconnection as fc
print(fc.get_version())

connection = fc.FritzConnection(password='butt2740')
info = connection.call_action('WANIPConnection', 'GetInfo')
Uptime = info['NewUptime']
print(Uptime)

import fritzstatus as fs
fs.print_status()

#hostcount = connection.call_action('WANIPConnection', 'GetHostNumberOfEntries')
#import fritzhosts as fh
#hosts = fh.FritzHosts(fc=connection)
#fh.print_hosts(password='butt2740')


import fritzwlan as fw
wlan= fw.FritzWLAN(password='butt2740') 
'''fw.print_hosts(hosts)'''


status = fs.FritzStatus(fc=connection)
print(status.external_ip)
print(status.max_byte_rate)



#print(fw.get_version())
#print(wlan.modelname)
#hostinfo = wlan.get_hosts_info()
#print(hostinfo)



'''fc.print_servicenames()'''


'''fc.print_api()'''





'''info = connection.call_action('WANIPConnection:1', 'GetInfo')

from .fritzconnection import (
    FritzConnection,
    FritzInspection,
    print_servicenames,
    print_api,
)
from .fritzhosts import (
    FritzHosts,
    print_hosts,
)
from .fritzstatus import (
    FritzStatus,
    print_status,
)
from .fritzphonebook import (
    FritzPhonebook,
    print_phonebooks,
)'''
