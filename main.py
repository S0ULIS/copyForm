#*-* coding: utf-8 *-*
from browser import browser
import json

NUM_PAGES = 20

def get_done_services(data):
    try:
        with open("done_services.json","r") as f:
            done_services = json.load(f.read())
    except:
        "[-] Error en lectura de archivo 'done_services.json' empezando de 0"
        done_services = {}
    non_repeated = []
    for service in data:
        if service["service_description"] in done_services and all(host in done_services[service["service_description"]] for host in service["service_hPars-t[]"][0]):
            print("[+] Servicio {} ya añadido, eliminándolo de lista a migrar")
        elif service["service_description"] in done_services:
            non_repeated.append(service)
            done_services[service["service_description"]].extend(service["service_hPars-t[]"])
            done_services[service["service_description"]] = list(set(done_services[service["service_description"]]))
        else:
            non_repeated.append(service)
            done_services[service["service_description"]] = service["service_hPars-t[]"]
    
    with open("done_services.json","w") as f:
        f.write(json.dumps(done_services, indent = 4))
    
    return non_repeated, done_services

if __name__=="__main__":
    i = 0
    br1 = browser("http://centreon1/main.php?p=601",page_number=0,item_offset=4)
    br2 = browser("http://centreon2/centreon/")
    
    while i<NUM_PAGES:
        data = br1.get_Services_Information()
        #print(data)
        
        
        #non_repeated, done_services = get_done_services(data)
        
        
        print("[+] Migrando {} items".format(len(data)))
        #data = [{'service_description': 'Prueba CPU', 'service_template_model_stm_id': 'generic-service', 'service_is_volatile[service_is_volatile]': '0', 'timeperiod_tp_id': '24x7', 'command_command_id': 'check_nrpe', 'ARG1': 'check_load', 'service_max_check_attempts': '3', 'service_normal_check_interval': '5', 'service_retry_check_interval': '1', 'service_active_checks_enabled[service_active_checks_enabled]': '2', 'service_passive_checks_enabled[service_passive_checks_enabled]': '2', 'service_notifications_enabled[service_notifications_enabled]': '2', 'service_cs-t[]': [[' ']], 'service_cgs-t[]': [['admins2']], 'service_notification_interval': '120', 'timeperiod_tp_id2': '24x7', 'service_notifOpts[w]': True, 'service_notifOpts[u]': True, 'service_notifOpts[c]': True, 'service_notifOpts[r]': True, 'service_notifOpts[f]': False, 'service_notifOpts[s]': False, 'service_first_notification_delay': '', 'li#c2 a': True, 'service_hPars-t[]': [['AFIRMATICKETS', 'CONSOLA_NAM']], 'mnftr': '_None_', 'service_traps-t[]': [[' ']], 'service_obsess_over_service[service_obsess_over_service]': '2', 'li#c3 a': True, 'service_check_freshness[service_check_freshness]': '2', 'service_freshness_threshold': '', 'service_flap_detection_enabled[service_flap_detection_enabled]': '2', 'service_low_flap_threshold': '', 'service_high_flap_threshold': '', 'service_process_perf_data[service_process_perf_data]': '2', 'service_retain_status_information[service_retain_status_information]': '2', 'service_retain_nonstatus_information[service_retain_nonstatus_information]': '2', 'service_stalOpts[o]': False, 'service_stalOpts[w]': False, 'service_stalOpts[u]': False, 'service_stalOpts[c]': False, 'service_event_handler_enabled[service_event_handler_enabled]': '2', 'command_command_id2': '', 'command_command_id_arg2': '', 'li#c4 a': True, 'graph_id': '', 'service_categories-t[]': [[' ']], 'esi_notes_url': '', 'esi_notes': '', 'esi_action_url': '', 'esi_icon_image': '', 'esi_icon_image_alt': '', 'criticality_id': '', 'service_activate[service_activate]': '1', 'service_comment': '15/01/2014 - 10:17:23', 'host_name': 'AFIRMATICKETS'}]
        br2.create_Services(data)
        br1.next_service_page()
        i+=1
    
