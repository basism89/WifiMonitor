if __name__ == '__main__':
    print('Hello Heimid!')

import fritzconnection as fc
print(fc.get_version())

connection = fc.FritzConnection(password='butt2740')
info = connection.call_action('WANIPConnection', 'GetInfo')
Uptime = info['NewUptime']
print(Uptime)

import fritzhosts as fh
print(fh.get_version())
host = fh.FritzHosts(password='butt2740')
#fh.print_hosts(host)

hosts = host.get_hosts_info()
for index, host in enumerate(hosts):
    status = 'active' if host['status'] == '1' else  '-'
    ip = '-' if host['ip'] == None else host['ip']
    mac = '-' if host['mac'] == None else host['mac']


import fritzstatus as fs
fs.print_status()




#hostcount = connection.call_action('WANIPConnection', 'GetHostNumberOfEntries')
#import fritzhosts as fh
#hosts = fh.FritzHosts(fc=connection)
#fh.print_hosts(password='butt2740')




status = fs.FritzStatus(fc=connection)
print(status.external_ip)
print(status.max_byte_rate)



import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=JULIA\SQLEXPRESS;DATABASE=WifiMonitor')

cursor = cnxn.cursor()
cursor.execute("select PersonId, LastName from users")
rows = cursor.fetchall()
for row in rows:
    print row.PersonId, row.LastName
    

'''
print(fw.get_version())
print(wlan.modelname)
hostinfo = wlan.get_hosts_info()
print(hostinfo)



fc.print_servicenames()'''


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
