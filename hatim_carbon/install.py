import frappe
from hatim_carbon.patches import stock_enable, batch_enable


def after_install():    
    stock_enable.execute()
    batch_enable.execute()