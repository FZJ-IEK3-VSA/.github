import yaml

path_to_yaml_file = r"C:\Programming\RESKit\requirements-dev.yml"
with open(path_to_yaml_file) as stream:
    try:
        output_dict = yaml.safe_load(stream)
        dependency_list = output_dict["dependencies"]
        dependency_iterator = 0
        for current_dep in dependency_list:
            print(dependency_iterator, current_dep)
            dependency_iterator = dependency_iterator + 1
    except yaml.YAMLError as exc:
        print(exc)
