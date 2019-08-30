from openstack import connection
import json

def jk():
	with open(r'C:\keys\keys.json', 'r') as key:
		jlo = json.load(key)
		return jlo[0]
k = jk()

conn = connection.Connection(
    region_name='RegionOne',
    auth=dict(
        auth_url='https://infra.mail.ru:35357/v3/',
        username=k['username'],
        password=k['password'],
        project_id=k['project_id'],
        user_domain_id='users'),
    compute_api_version='2',
    identity_interface='publicURL')
conn.identity.projects()