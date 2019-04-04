from getpass import getpass
password = getpass()

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "platform": "ios",
}

arista1 = {
    "hostname": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "platform": "eos",
}

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "platform": "nxos",
    "optional_args": {"port": 8443},
}

# List of devices (only cisco3 and arista1)
network_devices = [nxos1]
