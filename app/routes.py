from flask import render_template
from app import app
from nornir_app import *
import yaml



def load_hosts_inventory(filename):
    return yaml.load(open(filename, "r"), Loader=yaml.SafeLoader)


hosts = load_hosts_inventory("hosts.yaml")

# print(hosts)
inventory = []
for host in hosts:
    inventory.append({"name": host, "mgmt_ip": hosts[host]["hostname"], "platform": hosts[host]["platform"]})


# print(type(hosts_list))
@app.route('/')
@app.route('/index')
def index():
    name = "NetApp"
    return render_template("index.html", title="NetApp", name="netapp", inventory = inventory)

@app.route('/facts/<string:device_name>')
def display_facts(device_name):
    facts = get_facts(device_name)
    device_interface_list = []    
    for interface in facts["facts"]["interface_list"]:
        device_interface_list.append({"name": interface,
        "enabled":  facts["interfaces"][interface]["is_enabled"],
        "up": facts["interfaces"][interface]["is_up"],
        "description": facts["interfaces"][interface]["description"],
        "mac": facts["interfaces"][interface]["mac_address"],
        "mtu": facts["interfaces"][interface]["mtu"],
        "speed": facts["interfaces"][interface]["speed"],
        "last_flapped": facts["interfaces"][interface]["last_flapped"]
        })
    return render_template("facts.html", device_name=device_name, facts=facts, interface_list=device_interface_list)
