"""
Freeze & Clean Selected
Author: Kaillou Lai
Description:
    Freezes transforms and deletes construction history
    on all selected objects. A one-click prep tool before
    handing geometry off to rigging or animation — prevents
    transform offset issues downstream.

Usage:
    Select objects in Maya, then run in Script Editor (Python tab).
"""

import maya.cmds as cmds


def freeze_and_clean():
    # Get selected objects
    selected = cmds.ls(selection=True, type='transform')

    if not selected:
        cmds.warning("Nothing selected. Please select objects to freeze and clean.")
        return

    for obj in selected:
        # Freeze transforms — sets translate/rotate/scale to 0/0/1
        # apply=True means actually bake it in, not just display
        try:
            cmds.makeIdentity(
                obj,
                apply=True,
                translate=True,   # freeze position back to 0,0,0
                rotate=True,      # freeze rotation back to 0,0,0
                scale=True,       # freeze scale back to 1,1,1
                normal=False      # don't touch normals
            )
        except Exception as e:
            print(f"[FreezeClean] Could not freeze {obj}: {e}")
            continue

        # Delete construction history — removes all the 'how it was made' data
        # This reduces scene weight and prevents issues in animation
        try:
            cmds.delete(obj, constructionHistory=True)
        except Exception as e:
            print(f"[FreezeClean] Could not delete history on {obj}: {e}")

    print(f"[FreezeClean] Done — frozen and cleaned {len(selected)} object(s):")
    for obj in selected:
        print(f"  ✓ {obj}")


freeze_and_clean()
