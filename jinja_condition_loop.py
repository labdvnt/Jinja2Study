from jinja2 import Template

template_text = """ 
{% for device in devices %}
hostname {{ device.hostname }}
interface Loopback {{ device.loopback }}
  ip address {{ device.ip }} {{ device.netmask }}
  {% if device.description is defined %}
  description {{ device.description }}
  {% endif %}
{% endfor %}
"""

temp = Template(template_text)

devices = [
    {"hostname": "router1", "loopback": "1", "ip": "192.168.1.1", "netmask": "255.255.255.0", "description": "Uplink Router"},
    {"hostname": "router2", "loopback": "2", "ip": "192.168.1.2", "netmask": "255.255.255.0"},
    {"hostname": "router3", "loopback": "3", "ip": "192.168.1.3", "netmask": "255.255.255.0"},
]

output = temp.render(devices=devices)
print(output)