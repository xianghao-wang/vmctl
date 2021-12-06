import os
from config import CONFIGS


class VM:
    """
    A class used to representing VMWare virtual machine instance

    Attributes:
        name: the name of this vm instance
    """

    def __init__(self, name):
        self.name = name

    def is_running(self):
        """
        Check whether the vm is running

        :return: whether the vm is running
        """

        res = os.popen('vmrun list')
        for i, line in enumerate(res):
            if i != 0 and self.name in line:
                return True
        return False

    def path(self):
        """
        Get the absolute path of vm

        :return: a string of the absolute path of the vm instance
        """

        return CONFIGS['vm_dir'] + self.name

    def start(self, gui):
        """
        Start the vm instance

        :param gui: true if start with gui; false if no gui
        """

        op = 'gui' if gui else 'nogui'
        os.popen('vmrun start ' + self.get_path() + ' '  + op)

    def stop(self, soft):
        """

        :param soft: true if stop softtly (running the shutdown script): false if hardly poweroff
        """

        op = 'soft' if soft else 'hard'
        os.popen('vmrun stop ' + self.get_path() + ' ' + op)
