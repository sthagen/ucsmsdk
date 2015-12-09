"""This module contains the general information for SwExtUtilityFsmStage ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class SwExtUtilityFsmStageConsts():
    LAST_UPDATE_TIME_ = ""
    NAME_CONF_PORT_BREAKOUT_BEGIN = "ConfPortBreakoutBegin"
    NAME_CONF_PORT_BREAKOUT_CONFIG_SW_A = "ConfPortBreakoutConfigSwA"
    NAME_CONF_PORT_BREAKOUT_CONFIG_SW_B = "ConfPortBreakoutConfigSwB"
    NAME_CONF_PORT_BREAKOUT_FAIL = "ConfPortBreakoutFail"
    NAME_CONF_PORT_BREAKOUT_PORT_INVENTORY_SW_A = "ConfPortBreakoutPortInventorySwA"
    NAME_CONF_PORT_BREAKOUT_PORT_INVENTORY_SW_B = "ConfPortBreakoutPortInventorySwB"
    NAME_CONF_PORT_BREAKOUT_SUCCESS = "ConfPortBreakoutSuccess"
    NAME_CONF_PORT_BREAKOUT_VERIFY_BREAKOUT_CONFIG = "ConfPortBreakoutVerifyBreakoutConfig"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class SwExtUtilityFsmStage(ManagedObject):
    """This is SwExtUtilityFsmStage class."""

    consts = SwExtUtilityFsmStageConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("SwExtUtilityFsmStage", "swExtUtilityFsmStage", "stage-[name]", None, "OutputOnly", 0xfL, [], [""], [u'swExtUtilityFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "name": MoPropertyMeta("name", "name", "string", None, MoPropertyMeta.NAMING, None, None, None, None, ["ConfPortBreakoutBegin", "ConfPortBreakoutConfigSwA", "ConfPortBreakoutConfigSwB", "ConfPortBreakoutFail", "ConfPortBreakoutPortInventorySwA", "ConfPortBreakoutPortInventorySwB", "ConfPortBreakoutSuccess", "ConfPortBreakoutVerifyBreakoutConfig", "nop"], []), 
        "order": MoPropertyMeta("order", "order", "ushort", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retry": MoPropertyMeta("retry", "retry", "byte", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.sacl = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "SwExtUtilityFsmStage", parent_mo_or_dn, **kwargs)
