#!/usr/bin/env python

import gtk
import os
from os.path import expanduser, join
from getpass import getuser
from subprocess import call
from dialog_save import SaveDialog
from layout import Layout
from crunchbox.conky import Conky
from crunchbox.tint2 import Tint2
from crunchbox.Gtk import GTK
from crunchbox.openbox import Openbox
from crunchbox.nitrogen import Nitrogen
from base import Base

class CrunchBox:

	def __init__(self):
		# the cfg_files dictionary maps each program to their default cfg/rc
		# files. The keys of this dictionary must be an app name and it must
		# be exactly like its folder in ./config/crunchbox/<app name>
		# whenever we add support for a new app, we add it here
		self.cfg_files = {
		'gtk'		: expanduser('~/.gtkrc-2.0'),
		'conky'		: expanduser('~/.conkyrc'),
		'tint2'		: expanduser('~/.config/tint2/tint2rc'),
		'openbox'	: expanduser('~/.config/openbox/rc.xml'),
		'nitrogen'	: expanduser('~/.config/nitrogen/bg-saved.cfg')
		}

		# -- instantiate objects and variables
		self.base = Base(self)
		self.cb_cfg_dir = expanduser('~/.config/crunchbox')
		self.check_cfg_folder()
		self.layout = Layout(self)	

		
		

	def save_clicked(self, w, e):
		dialog = SaveDialog(self)
		
		
		
	def save_profile(self, name):
		# For now, this program is made for crunchbang linux and its default
		# programs. So as of now it only supports those programs, which are
		# gtk, conky, tint2, nitrogen, terminator. (TODO?)in the future, maybe
		# we check if a program is installed in the user's computer by checking
		# if its config folder exists, if it does, add it to the self.cfg_files
				
		# -- tint2
		tint2 = Tint2(self.base)
		tint2.save(name)

		# -- conky
		conky = Conky(self.base)
		conky.save(name)
			
		# -- terminator
		# TODO
				
		# -- openbox
		openbox = Openbox(self.base)
		openbox.save(name)

		# -- Nitrogen (wallpaper)
		nitrogen = Nitrogen(self.base)
		nitrogen.save(name)

		# -- gtk
		g = GTK(self.base)
		g.save(name)
		
		self.save_screenshot(name)
		
	
	def load_profile(self, w, e):
		'''this is called from layout.py when screenshot is clicked'''
		# img_name is the name of the screenshot, aka name of our profile
		name = w.get_data('img_name')
		
		# -- tint2
		tint2 = Tint2(self.base)
		tint2.load(name)

		# -- conky
		conky = Conky(self.base)
		conky.load(name)
		
		# -- terminator
		# TODO
		
		# -- openbox
		openbox = Openbox(self.base)
		openbox.load(name)

		# -- Nitrogen (wallpaper)
		nitrogen = Nitrogen(self.base)
		nitrogen.load(name)
		
		# -- gtk
		g = GTK(self.base)
		g.load(name)
		

	def save_screenshot(self, name):
		'''
		unfortunatelly, imagick's screenshots won't show composite windows
		transparency like conky or transparent terminals. so we use scrot
		when i figure out how to do it, then we only need to call() once with
		import -window root -resize 200x175\! %s/%s.jpg;\
		'''
		path = expanduser('~/.config/crunchbox/screenshots')
		scrot = """scrot '%s.jpg' -e "mv '%s.jpg' '%s/%s.jpg'";""" % (name, name, path, name)
		convert = """convert -resize 200x125\! '%s/%s.jpg' '%s/%s.jpg'""" % (path, name, path, name)
		command = scrot + convert
		call(command, shell=True)
		self.layout.append_screenshot(name)
	
	
	def check_cfg_folder(self):
		'''check if ~/.config/crunchbox exists, creates it if notpythopygtk d'''
		if os.path.exists(self.cb_cfg_dir) == False:
			# create it, and all its apps subdirs. to do this, we first create ~/.config/crunchbox
			# and ~/.config/crunchbox/crunchbox
			# and then take all the keys from self.cfg_files (which are names of supported apps)
			# and make a dir with that key, and we'll get ~/.config/crunchbox/crunchbox/tint2, etc.
			os.mkdir(self.cb_cfg_dir)
			os.mkdir(self.cb_cfg_dir + '/screenshots')
			os.mkdir(self.cb_cfg_dir + '/crunchbox')
			for key in self.cfg_files:
				os.mkdir(self.cb_cfg_dir + '/crunchbox/%s' % key) 
	    
	


    	
def main():
	gtk.main()

if __name__ == "__main__":
	cb = CrunchBox()
	main()
