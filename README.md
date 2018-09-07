#### Zabbix monitoring processes running under monit supervisor

###### Content:

* `lld_monit_process.py` LLD script
* `get_monit_process_metrics.py` UserDefined script for data gathering
* `requirements.txt` Required modules for python
* `zabbix-monit-template.xml` Template for zabbix
* `userparameter_monit.conf` Config for zabbix agent
* `deploy.yml` Ansible deploy playbook


1. Python requirements
Ensure you have all python modules from requirements.txt on monitored machines.
Deploy doesn't cover requirements installation
If you have several python installations you could pick right interpreter by setting
environment variable `PATH` for zabbix-agent process.<br>
Like so: `export PATH="/path/to/yours/python/bin:${PATH:+$PATH:}/usr/sbin:/sbin`<br>
The fist interpreter in PATH will be used.<br>

2. Deploy
You need installed zabbix-agent before run it
`ansible-playbook -b -i inventory -l <list of groups or hosts> deploy.yml`

3. Testing
*On monitored machine*<br>
Test LLD:<br>
`sudo -u zabbix PATH=/opt/waf/python/bin /usr/sbin/zabbix_agentd -t monit.lld[http://localhost:2812,monit,monit]`<br>
Test Item<br>
`sudo -u zabbix PATH=/opt/waf/python/bin /usr/sbin/zabbix_agentd -t monit.process[http://localhost:2812,monit,monit,<process name from lld>,Status]`<br>
*On zabbix server*<br>
Test LLD:<br>
`zabbix_get -s <monitored server> -k "monit.lld[http://localhost:2812,monit,monit]"`<br>
Test Item<br>
`zabbix_get -s <monitored server> -k "monit.process[http://localhost:2812,monit,monit,<process name from lld>,Status]"`<br>


