class HolderSegments:
    def __init__(self, height,
                       upper_diam,
                       lower_diam):
        self.height = height
        self.upper_diam = upper_diam
        self.lower_diam = lower_diam
        

class Holder:
    def __init__(self, description,
                       product_id,
                       product_link,
                       segments,
                       unit,
                       holder_type,
                       vendor):
        self.description = description
        self.product_id = product_id
        self.product_link = product_link
        self.segments = segments
        self.unit = unit
        self.holder_type = holder_type
        self.vendor = vendor


class ToolGeometry:
    def __init__(self csp,
                      dc,
                      hand,
                      lb,
                      lcf,
                      nof,
                      oal,
                      sfdm,
                      shoulder_lenght):
        self.csp = csp
        self.dc = dc
        self.hand = hand
        self.lb = lb
        self.lcf = lcf
        self.nof = nof
        self.oal = oal
        self.sfdm = sfdm
        self.shoulder_lenght = shoulder_lenght  


class  Preset: 
    def __init__(self, name="Defualt", 
                       f_n,
                       f_z,
                       n,
                       n_ramp,
                       tool_coolant,
                       use_stepdown,
                       use_stepover,
                       v_c,
                       v_f,
                       v_f_leadIn,
                       v_f_leadOut,
                       v_f_plunge,
                       v_f_ramp):
        self.name = name  
        self.f_n = f_n
        self.f_z =  f_z
        self.n = n
        self.n_ramp = n_ramp
        self.tool_coolant = tool_coolant
        self.use_stepdown = use_stepdown
        self.use_stepover = use_stepover
        self.v_c = v_c
        self.v_f = v_f
        self.v_f_leadIn = v_f_leadIn
        self.v_f_leadOut = v_f_leadOut
        self.v_f_plunge = v_f_plunge
        self.v_f_ramp = v_f_ramp


class  PostProcessor: 
    def __init__(self,  tool_number=1,
                        live = True,
                        manual_tool_change=False,
                        turret = 0):
        self.brake_control = False
        self.tool_number = tool_number
        self.comment = self.tool_number
        self.diameter_offset = self.tool_number
        self.live = = live
        self.manual_tool_change = manual_tool_change
        self.turret = turret


class Tool:
    def __init__(self, description,
                       vendor,
                       product_id,
                       product_link,
                       tool_type,
                       unit,
                       material,
                       tool_geometry, 
                       presets, 
                       post_processor, 
                       holder):
        self.description = description
        self.vendor = vendor
        self.product_id = product_id
        self.product_link = product_link
        self.tool_type = tool_type
        self.unit = unit
        self.material = material       
        self.tool_geometry = tool_geometry
        self.presets = presets
        self.post_processor = post_processor
        self.holder = holder

    def to_json(self):
        #TODO: 
        pass
        
