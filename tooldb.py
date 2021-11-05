from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class ToolModel(Model):
    """
    Tool Table
    """
    class Meta:
        table_name = 'tool-lib'
        region = 'us-east-1'
    email = UnicodeAttribute(hash_key=True)
    tool_number = UnicodeAttribute()
    tool = UnicodeAttribute() 
    desc = UnicodeAttribute() 
    comment = UnicodeAttribute() 
    diam = UnicodeAttribute() 
    flutes = UnicodeAttribute() 
    stickout = UnicodeAttribute() 
    lead_ang = UnicodeAttribute() 
    nose_rad = UnicodeAttribute() 
    cut_lenght = UnicodeAttribute() 
    overall_length = UnicodeAttribute() 
    shank_size = UnicodeAttribute() 
    geometry = UnicodeAttribute() 
    coating = UnicodeAttribute() 
    tool_material = UnicodeAttribute() 
    helix_angle = UnicodeAttribute() 
    tool_family = UnicodeAttribute() 
    x_comp = UnicodeAttribute() 
    z_comp = UnicodeAttribute() 
    z_geom = UnicodeAttribute() 
    holder_type = UnicodeAttribute() 
    holder_desc = UnicodeAttribute() 
    holder_len = UnicodeAttribute() 
    clockwise = UnicodeAttribute() 
    shoulder_len = UnicodeAttribute() 
    taper_angle_2 = UnicodeAttribute() 
    tip_len = UnicodeAttribute() 
    tip_diam = UnicodeAttribute() 
    thread_pitch = UnicodeAttribute() 
    serail_num = UnicodeAttribute() 
    vendor = UnicodeAttribute() 
    product = UnicodeAttribute() 
    id_num = UnicodeAttribute() 
    ins_num = UnicodeAttribute() 
    product_link = UnicodeAttribute() 
    job_code = UnicodeAttribute() 
    price_paid = UnicodeAttribute() 
    status = UnicodeAttribute() 
    field_1 = UnicodeAttribute() 
    field_2 = UnicodeAttribute() 
    field_3 = UnicodeAttribute() 
    field_4 = UnicodeAttribute() 
    guid = UnicodeAttribute() 
