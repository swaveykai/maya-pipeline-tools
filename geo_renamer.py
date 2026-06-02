"""
GEO Renamer Tool
Author: Kaillou Lai
Description:
    Adds a 'GEO_' prefix to all selected objects in Maya.
    Built to enforce naming conventions before handing
    off layout scenes to Animation and Lighting departments.

Usage:
    Select objects in Maya, then run in Script Editor (Python tab).
"""

import maya.cmds as cmds


def add_geo_prefix():
    # Get whatever the artist has selected in the viewport
    selected = cmds.ls(selection=True)

    # If nothing is selected, warn and stop
    if not selected:
        cmds.warning("Nothing selected. Please select objects to rename.")
        return

    renamed = []

    for obj in selected:
        # Only rename if it doesn't already start with GEO_
        if not obj.startswith("GEO_"):
            new_name = "GEO_" + obj
            cmds.rename(obj, new_name)
            renamed.append(new_name)
        else:
            print(f"[Renamer] '{obj}' already has GEO_ prefix, skipping.")

    print(f"[Renamer] Renamed {len(renamed)} object(s):")
    for name in renamed:
        print(f"  + {name}")


add_geo_prefix()
