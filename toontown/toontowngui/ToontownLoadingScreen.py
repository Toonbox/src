from pandac.PandaModules import *
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import random


class ToontownLoadingScreen:
	
	defaultTex = 'phase_3.5/maps/loading/default.jpg'
	zone2video = {
	    ToontownGlobals.ToontownCentral : '',
	    ToontownGlobals.SillyStreet : '',
	    ToontownGlobals.LoopyLane : '',
	    ToontownGlobals.PunchlinePlace : '',
	    ToontownGlobals.DonaldsDock : '',
	    ToontownGlobals.BarnacleBoulevard : '',
	    ToontownGlobals.SeaweedStreet : '',
	    ToontownGlobals.LighthouseLane : '',
	    ToontownGlobals.TheBrrrgh : '',
	    ToontownGlobals.WalrusWay : '',
	    ToontownGlobals.SleetStreet : '',
	    ToontownGlobals.PolarPlace : '',
	    ToontownGlobals.MinniesMelodyland : '',
	    ToontownGlobals.AltoAvenue : '',
	    ToontownGlobals.BaritoneBoulevard : '',
	    ToontownGlobals.TenorTerrace : '',
	    ToontownGlobals.DaisyGardens : '',
	    ToontownGlobals.ElmStreet : '',
	    ToontownGlobals.MapleStreet : '',
	    ToontownGlobals.OakStreet : '',
	    ToontownGlobals.DonaldsDreamland : '',
	    ToontownGlobals.LullabyLane : '',
	    ToontownGlobals.OutdoorZone : '',
	    ToontownGlobals.GolfZone : '',
	    ToontownGlobals.GoofySpeedway : '',
	    ToontownGlobals.BossbotHQ : '',
	    ToontownGlobals.SellbotHQ : '',
	    ToontownGlobals.CashbotHQ : '',
	    ToontownGlobals.LawbotHQ : '',
	    ToontownGlobals.Tutorial : '',
	    ToontownGlobals.MyEstate : ''
	}
	
	def __init__(self):
		self.__expectedCount = 0
		self.__count = 0
		self.gui = loader.loadModel('phase_3/models/gui/progress-background.bam')
		self.title = DirectLabel(guiId='ToontownLoadingScreenTitle', parent=self.gui, relief=None, pos=(base.a2dTopCenter+0, 0, 0.235), text='', textMayChange=1, text_scale=0.1, text_fg=(0.00, 0.58, 0.996, 1), text_align=TextNode.ACenter, text_font=ToontownGlobals.getSignFont())
		self.waitBar = DirectWaitBar(guiId='ToontownLoadingScreenWaitBar', parent=self.gui, frameSize=(-0.75, 0.75, -0.02, 0.02), pos=(0, 0, -0.85), text='')
		return
		
	def destroy(self):
		pass
		
	def getTip(self, todo):
		pass
		
	def begin(self, todo, todo1, todo2, todo3):
		pass
		
	def end(self):
		pass
		
	def abort(self):
		pass
		
	def tick(self):
		pass
