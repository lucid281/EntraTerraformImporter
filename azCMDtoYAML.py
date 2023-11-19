import subprocess
from pathlib import Path
import fire
import yaml


class AZtoYaml:
    def users(self, force=False):
        users = Path("users.yml")
        if not users.exists() or force:
            with subprocess.Popen("az.cmd ad user list -o yaml".split(" "),
                                  stdout=subprocess.PIPE,
                                  universal_newlines=True) as proc:
                new_file = users.open("w")
                [new_file.write(str(line)) for line in proc.stdout.readlines()]
            new_file.close()
            print(f'updated {users.absolute()}')

    def groups(self, force=False):
        groups = Path("groups.yml")
        if not groups.exists() or force:
            with subprocess.Popen("az.cmd ad group list -o yaml".split(" "),
                                  stdout=subprocess.PIPE,
                                  universal_newlines=True) as proc:
                new_file = groups.open("w")
                [new_file.write(str(line)) for line in proc.stdout.readlines()]
            new_file.close()
            print(f'updated {groups.absolute()}')


class YamlToImport:
    def users(self, tf_name, key="userPrincipalName"):
        users = yaml.safe_load(Path("users.yml").open('r'))
        for user in users:
            value = user[key]
            print(f'import azuread_user.{tf_name}["{value}"] {user["id"]}')

    def groups(self, tf_name, key="displayName"):
        groups = yaml.safe_load(Path("groups.yml").open('r'))
        for group in groups:
            value = group[key]
            print(f'import azuread_group.{tf_name}["{value}"] {group["id"]}')


class AZtools:
    def yaml(self):
        """
        Create .yml output files of Azure resources
        :return: AZtoYaml
        """
        return AZtoYaml

    def imports(self):
        """
        Generate `terraform import` commands from yaml files.
        :return: YamlToImport
        """
        return YamlToImport


if __name__ == "__main__":
    fire.Fire(AZtools)
