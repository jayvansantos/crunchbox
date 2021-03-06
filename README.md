# Dependencies
Python2  
Scrot & ImageMagick (for saving + resizing screenshot)  
  
 
## What
A themes manager that saves your current programs  
themes and easily loads them later.   
Changes the look of your desktop on the fly.  
* [Here's a video of the program in action](http://www.youtube.com/watch?v=tmftzqiv0c4)


programs supported: Any.  

Out of the box, Crunchbox comes with the following plugins
- Openbox
- GTK2 theme and icon theme
- Tint2
- Conky
- Nitrogen
- Bash 
- Urxvt (.Xresources)
- Weechat
- Ncmpcpp 


## Screenshot
![Screenshot](http://i.imgur.com/bU9Qo.png)



## Instructions
1.How to start:  
 a. Extract the 'crunchbox' folder to anywhere you want. Assume it's in ~/downloads/crunchbox, just do:  
    $ cd downloads/crunchbox/src  
    $ python crunchbox.py


Some screenshots and more info can be found here:
http://crunchbanglinux.org/forums/topic/17149/mmmcrunchbox/


## HOW TO ADD SUPPORT FOR A PROGRAM (plugin)
It's extremely simple. All you have to do is tell Crunchbox
where the program's config file is located. If you know minimal Python,
you will figure out right away. If you know 0 python, follow steps below.

Look at plugins that ship with Crunchbox. 

Say you want to add support for Openbox(which is there already. Just using for example).

__1)__ Create file openbox.py inside the plugins directory  
__2)__ Copy the content of (ie, tint2.py) into openbox.py  
__3)__ Change the class name on line #4. So "class Tint2: " becomes "class Openbox: "  
__4)__ Change the line that is the path to the config file in your system.  
   So in our case, we would change the line  
   -> self.cfg = [ expanduser("~/.config/tint2/tint2rc) ]  
   to make it look like  
   -> self.cfg = [ expanduser("~/.config/openbox/rc.xml") ]  

__5)__ Inside the load method, we tell Crunchbox what command to run to restart the program.  
   Notice that inside tint2.py, we have:     
   call('killall tint2; tint2 &') <--- this causes tint2 to restart, with the new cfg!  
   As another example, look inside openbox.py. We have  
   call('openbox --reconfigure')  
   You simply write just as you would if you were in a terminal


## F A Q
Q) When i save, the program disappear for about a second, and then appears again.  
A) This is intended. This is so the program itself isn't present in your screenshot.  




   
