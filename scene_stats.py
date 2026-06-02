"""
Scene Stats Printer
Author: Kaillou Lai
Description:
    Prints a quick health summary of the current Maya scene.
    Useful at the start of a shot to understand what you're
    working with before making changes — mesh count, poly count,
    cameras, and referenced files.

Usage:
    Run in Maya's Script Editor (Python tab) at any time.
"""

import maya.cmds as cmds


def print_scene_stats():
    # Get all mesh shapes in the scene (the actual geometry nodes)
    all_meshes = cmds.ls(type='mesh')

    # Count total polygons across all meshes
    total_polys = 0
    for mesh in all_meshes:
        poly_count = cmds.polyEvaluate(mesh, face=True)
        # polyEvaluate returns an int but can return 0 on empty mesh
        if isinstance(poly_count, int):
            total_polys += poly_count

    # Get all cameras in the scene
    all_cameras = cmds.ls(type='camera')

    # Get any referenced files (assets brought in from outside)
    referenced = cmds.file(query=True, reference=True) or []

    # Get unknown nodes (leftover from other software versions)
    unknown = cmds.ls(type='unknown')

    print("\n========== Scene Stats ==========")
    print(f"  Meshes:           {len(all_meshes)}")
    print(f"  Total polygons:   {total_polys:,}")
    print(f"  Cameras:          {len(all_cameras)}")
    print(f"  Referenced files: {len(referenced)}")
    print(f"  Unknown nodes:    {len(unknown)}")
    print("=================================\n")

    if unknown:
        print("[Warning] Unknown nodes detected — consider cleaning before handoff:")
        for node in unknown:
            print(f"  - {node}")


print_scene_stats()
