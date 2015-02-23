from pandac.PandaModules import Vec4

from toontown.safezone import CPSafeZoneLoader
from toontown.town import CPTownLoader
from toontown.toonbase import ToontownGlobals
from toontown.hood.ToonHood import ToonHood


class CPHood(ToonHood):
    notify = directNotify.newCategory('DGHood')
    
    ID = ToontownGlobals.ChestnutPark
    TOWNLOADER_CLASS = CPTownLoader
    SAFEZONELOADER_CLASS = CPSafeZoneLoader
    STORAGE_DNA = 'phase_6/dna/storage_CP.pdna'
    SKY_FILE = 'phase_6/models/modules/unpainted_sky'
    SPOOKY_SKY_FILE = 'phase_3.5/models/props/BR_sky'
    TITLE_COLOR = (1.0, 0.5, 0.4, 1.0)
    
    HOLIDAY_DNA = {
      ToontownGlobals.HALLOWEEN_PROPS: ['phase_6/dna/halloween_props_storage_CP.dna'],
      ToontownGlobals.SPOOKY_PROPS: ['phase_6/dna/halloween_props_storage_CP.dna']}

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodID):
        ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        
        # Load content pack ambience settings:
        ambience = contentPacksMgr.getAmbience('chestnut-park')
        
        color = ambience.get('underwater-color')
        if color is not None:
    	    try:
    	        self.underwaterColor = Vec4(color['r'], color['g'], color['b'], color['a'])
    	    except Exception, e:
    	        raise ContentPackError(e)
        elif self.underwaterColor is None:
		    self.underwaterColor = Vec4(0.0, 0.0, 0.6, 1.0)

    def load(self):
        ToonHood.ToonHood.load(self)
        
        self.fog = Fog('CPFog')

    def enter(self, *args):
        ToonHood.ToonHood.enter(self, requestStatus)
        
        base.camLens.setNearFar(ToontownGlobals.SpeedwayCameraNear, ToontownGlobals.SpeedwayCameraFar)

    def exit(self):
	    base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
	    
        ToonHood.ToonHood.exit(self)
    
