#!/usr/bin/python3
import Parser 
import Monitor
import json
import Prometheus

def start():
    cfg_param = []
    config_parser = Parser.parser()
    cfg_param = config_parser.component_parse()
    #jsonObject = json.loads(cfg_param)
    #cfg_param = config_parser.parse()
    if cfg_param.get('name') == "monitoring" and cfg_param.get('property') == "server":
        prom = Prometheus.prometheus()
        prom.server()    
        #print("Monitoring comp")

if __name__ == "__main__":
    start()