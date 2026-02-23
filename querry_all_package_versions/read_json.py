import json
import pathlib
import subprocess

# mamba search tqdm --json > ".\querry_all_package_versions\tqdm_version.json" 2>&1
library_name = "python"
current_directory = pathlib.Path(__file__).parent
output_file = current_directory.joinpath(f"{library_name}_version.json")
subprocess.run(f'mamba search {library_name} --json > "{output_file}" 2>&1', shell=True)

with open(output_file) as handle:
    version_dict = json.loads(handle.read())

package_list = version_dict["result"]["pkgs"]
output_version_list = []
for current_package_dict in package_list:
    current_version = current_package_dict["version"]
    output_version_list.append(current_version)


unique_version_list = sorted(list(set(output_version_list)))
print(library_name, ":\n", unique_version_list)

pass
