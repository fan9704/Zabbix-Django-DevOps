import psutil
from pyzabbix import ZabbixAPI
import time
import requests


zabbix_api = ZabbixAPI("http://localhost:10050/zabbix")
zabbix_api.login("zabbix", "zabbix")

zabbix_agent_container_name = 'zabbix-agent'
zabbix_agent_service_name = 'zabbix-agent'
zabbix_agent_network_name = 'zbx_net'

# response = requests.get(f'http://localhost:2375/v1.24/containers/{zabbix_agent_container_name}/json')
# json_data = response.json()
# zabbix_agent_ip = json_data['NetworkSettings']['Networks'][zabbix_agent_network_name]['IPAddress']

# 取得 Zabbix Agent 的 host ID
host_name = 'Zabbix Agent Host'
host_id = zabbix_api.host.get(filter={'host': host_name})[0]['hostid']

# 傳送監控數據至 Zabbix Server
item_key = 'system.cpu.load[all,avg1]'
item_value = '1.23'

zabbix_api.item.create(hostid=host_id, key=item_key, value_type=0, type=0, name=item_key)
zabbix_api.item.update(hostid=host_id, key=item_key, status=0)
zabbix_api.history.create(itemid=1, clock=int(time.time()), value=item_value)


# def getMemoryAndCPUInfo():
#     process = psutil.Process()

#     # 获取 CPU 使用率
#     cpu_percent = process.cpu_percent()

#     # 获取内存占用情况
#     memory_info = process.memory_info()
#     rss = memory_info.rss / 1024 / 1024  # 单位 MB
#     vms = memory_info.vms / 1024 / 1024  # 单位 MB
#     return rss,vms,cpu_percent


# # Define Zabbix server details
# zabbixServer = 'localhost'
# zabbixPort = 10051


# # Create Zabbix sender object
# zabbixSender = ZabbixSender(zabbixServer, zabbixPort)




# while True:
#     # Define metric
#     rss,vms,cpu_percent=getMemoryAndCPUInfo()
#     MEMORY_RSS_KEY = "zabbixApp.memory.rss"
#     MEMORY_RSS_VALUE = rss
#     MEMORY_VMS_KEY = "zabbixApp.memory.vms"
#     MEMORY_VMS_VALUE = vms
#     CPU_PERCENT_KEY = "zabbixApp.cpu.percent"
#     CPU_PERCENT_VALUE = cpu_percent
#     # Create Zabbix metric object
#     packet = [
#         ZabbixMetric('zabbixApp.host', MEMORY_RSS_KEY, MEMORY_RSS_VALUE),
#         ZabbixMetric('zabbixApp.host', MEMORY_VMS_KEY, MEMORY_VMS_VALUE),
#         ZabbixMetric('zabbixApp.host', CPU_PERCENT_KEY, CPU_PERCENT_VALUE),
#     ]
#     # Send the metric to Zabbix server
#     result = ZabbixSender(use_config=True).send(packet)
#     # Check the result
#     if result.failed > 0:
#         print('Failed to send metric to Zabbix server.')
#     time.sleep(60)