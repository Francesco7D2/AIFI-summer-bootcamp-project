# -*- coding: utf-8 -*-
"""
Spyder Editor

"""


import logging

from src.utils.setup_utilities import load_config, setup_logging
from src.data_preprocessing.data_loader import DataLoader

def main():
    #global stock_data
    # load configuration
    config = load_config()
    
    #set up logging
    setup_logging()
    
    
    logging.info("Starting the pipeline")
    
    #try: 
    data_loader = DataLoader(tickers=config['data']['tickers'],
                                          start_date=config['data']['start_date'],
                                          end_date=config['data']['end_date'],
                                          raw_data_path=config['data']['raw_data_path'])
        
    stock_data = data_loader.load_data(interval = config['data']['interval'])
    
    print(stock_data.head())
    print('hola')
    logging.info("Pipeline completed successfully")
        
#    except Exception as e:
#        logging.error(f"An error occurred: {str(e)}", exc_info=True)
    

if __name__  == "__main__":
    main()
    

