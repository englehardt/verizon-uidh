from automation import TaskManager
import os

NUM_BROWSERS = 10

sites = list()
with open('alexa500.txt','r') as f:
    for line in f:
        sites.append('http://'+line.strip())

db_loc  = os.path.expanduser('~/verizon.sqlite')

browser_params = TaskManager.load_default_params(NUM_BROWSERS)
for i in range(NUM_BROWSERS):
    browser_params[i]['headless'] = True

manager = TaskManager.TaskManager(db_loc, browser_params, NUM_BROWSERS)

for site in sites:
    manager.get(site, reset=True)

manager.close()
