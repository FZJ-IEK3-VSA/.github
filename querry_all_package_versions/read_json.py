import json
import pathlib

# mamba search pandas --json > ".\querry_all_package_versions\pandas_version.json" 2>&1
current_directory = pathlib.Path(__file__).parent
with open(current_directory.joinpath(r"pandas_version.json")) as handle:
    version_dict = json.loads(handle.read())

package_list = version_dict["result"]["pkgs"]
output_version_list = []
for current_package_dict in package_list:
    current_version = current_package_dict["version"]
    output_version_list.append(current_version)


unique_version_list = sorted(list(set(output_version_list)))
print(unique_version_list)

pass
