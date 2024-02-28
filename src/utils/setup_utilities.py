# -*- coding: utf-8 -*-


import yaml
import logging


from ..data_preprocessing.data_loader import DataLoader

def load_config(config_path='config.yml'):
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config


def setup_logging(log_file='reports/logs/main.log', log_level=logging.INFO):
    logging.basicConfig(filename=log_file, level=log_level,
                        format='%(asctime)s - %(levelname)s - %(message)s')
                        
                        
                        
def load_data(config):
	
	data_loader = DataLoader(tickers=config['data']['tickers'],
                                          start_date=config['data']['start_date'],
                                          end_date=config['data']['end_date'],
                                          raw_data_path=config['data']['raw_data_path'])
        
	data = data_loader.load_data(interval = config['data']['interval'], 
								 features = config['data']['features'])
 
	return data







