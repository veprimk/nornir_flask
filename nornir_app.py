from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get




def get_facts(device):
    nr = InitNornir()
    nr = nr.filter(name=device)
    results = nr.run(
        task=napalm_get, 
        getters=["facts", "interfaces"]
    )
    return results[device][0].result