import ansible_runner
import requests

# Run playbook
r = ansible_runner.run(private_data_dir='./', playbook='hello.yml')
print("Playbook Run Results:")
print(r.stats)

# Check response from NodeJS servers (assuming the ports are as defined earlier)
for port in [3000, 3001, 3002]:
    try:
        response = requests.get(f'http://localhost:{port}')
        print(f"Server on port {port} returned status code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request to server on port {port} failed with error: {e}")
