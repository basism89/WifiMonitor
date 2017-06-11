#if __name__ == '__main__':
#    print('Hello Heimid!')

import fritzconnection as fc
#print(fc.get_version())

connection = fc.FritzConnection(password='butt2740')
info = connection.call_action('WANIPConnection', 'GetInfo')
Uptime = info['NewUptime']
#print(Uptime)

import fritzhosts as fh
#print(fh.get_version())
host = fh.FritzHosts(password='butt2740')
#fh.print_hosts(host)


import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=JULIA\SQLEXPRESS;DATABASE=WifiMonitor')
cursor = cnxn.cursor()

hosts = host.get_hosts_info()
for index, host in enumerate(hosts):
    if host['status'] == '1': 
        ip = '-' if host['ip'] == None else host['ip']
        mac = '-' if host['mac'] == None else host['mac']
        name = '-' if host['name'] == None else host['name']
        insertstatement = 'INSERT INTO HOSTS VALUES (getdate(), \'' + name + '\',\''  + ip + '\',\'' + mac + '\')' 
        print(insertstatement)
        cursor.execute(insertstatement)

cnxn.commit()
    
      
import fritzstatus as fs
#fs.print_status()
status = fs.FritzStatus(fc=connection)
#print(status.external_ip)
#print(status.max_byte_rate)


    



