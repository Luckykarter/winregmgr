import winreg


class OpenKey:
    """
    Context manager for working with Windows registry
    """

    def __init__(self, key, sub_key):
        self.key = key
        self.sub_key = sub_key
        self.registry_key = None

    def __enter__(self):
        self.registry_key = winreg.OpenKey(self.key, self.sub_key, 0, winreg.KEY_ALL_ACCESS)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        winreg.CloseKey(self.registry_key)

    def set_value(self, name, value):
        winreg.SetValueEx(self.registry_key, name, 0, winreg.REG_SZ, value)

    def get_value_regtype(self, name):
        return winreg.QueryValueEx(self.registry_key, name)

    def get_value(self, name):
        value, _ = self.get_value_regtype(name)
        return value

    def delete_key(self, name):
        winreg.DeleteValue(self.registry_key, name)

    def get_values(self):
        """
        Reads all parameters from opened Registry key
        :return: dictionary with key: parameter name, value: parameter value
        """
        values = {}
        i = 0
        while True:
            try:
                key, value, _ = winreg.EnumValue(self.registry_key, i)
                values[key] = value
                i += 1
            except WindowsError:
                break
        return values
