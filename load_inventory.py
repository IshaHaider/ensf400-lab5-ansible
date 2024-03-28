

import ansible_runner

# Define the inventory path and playbook
inventory_path = './hosts.yml'
playbook_path = 'hello.yml'

# Run an ad-hoc command ('ping' module) against all hosts
r = ansible_runner.run(
    private_data_dir='.', 
    inventory=inventory_path,
    host_pattern='all',
    module='ping'
)

# Print the output
print("Ping Results:")
for host, result in r.stats.items():
    print(f"{host}: {result}")

