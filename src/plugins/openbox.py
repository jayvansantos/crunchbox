from subprocess import call
from os.path import expanduser

class Openbox:

	def __init__(self, base):
		self.base = base
		self.cfg = [
			expanduser("~/.config/openbox/rc.xml"),
<<<<<<< HEAD
			expanduser("~/.config/openbox/menu.xml")
=======
			expanduser("~/.config/openbox/menu.xml"),
			expanduser("~/.config/openbox/autostart")
>>>>>>> aaf8dc0200e8df1a23c1fd453ea93306220c162b
		]

		# This is the path to where crunchbox stores all this plugin's cfg
		self.class_name = self.__class__.__name__
		self.plugin_cfg_dir = expanduser('~/.config/crunchbox/configs/' + self.class_name)

	def save(self, profile_name, plugin_obj):
		self.base.save(profile_name, self.class_name, plugin_obj)

	def load(self, profile_name, plugin_obj):
		self.base.load(profile_name, self.class_name, plugin_obj)

		# reload openbox's config
		# call('openbox --reconfigure', shell=True)
		call('openbox --restart', shell=True)

