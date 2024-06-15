import yaml

def convert_yml_to_requirements(yml_file, requirements_file):
    with open(yml_file, 'r') as stream:
        try:
            env_data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return

    dependencies = env_data.get('dependencies', [])
    pip_packages = []

    with open(requirements_file, 'w') as req_file:
        for dep in dependencies:
            if isinstance(dep, str):
                req_file.write(f"{dep}\n")
            elif isinstance(dep, dict) and 'pip' in dep:
                pip_packages.extend(dep['pip'])

        for pip_dep in pip_packages:
            req_file.write(f"{pip_dep}\n")

# Usage
convert_yml_to_requirements('py4fi2nd.yml', 'requirements.txt')
