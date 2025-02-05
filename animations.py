import unreal

def apply_animation(metahuman_name, animation_asset):
    """
    Applica un'animazione a un MetaHuman in Unreal Engine.
    """
    editor_asset_lib = unreal.EditorAssetLibrary()
    skel_mesh_component = editor_asset_lib.load_asset(f"/Game/MetaHumans/{metahuman_name}")

    if skel_mesh_component:
        animation = editor_asset_lib.load_asset(f"/Game/Animations/{animation_asset}")
        if animation:
            skel_mesh_component.set_editor_property("AnimationMode", unreal.AnimationMode.ANIMATION_SINGLE_NODE)
            skel_mesh_component.set_editor_property("AnimationAsset", animation)
            print(f"✅ Animazione {animation_asset} applicata a {metahuman_name}.")
        else:
            print(f"❌ Animazione {animation_asset} non trovata.")
    else:
        print(f"❌ MetaHuman {metahuman_name} non trovato.")

# Test manuale:
# apply_animation("MH_Example", "Wave")

