import unreal

def export_to_vr(metahuman_name):
    """
    Esporta il MetaHuman in un ambiente VR in Unreal Engine.
    """
    asset_path = f"/Game/MetaHumans/{metahuman_name}"
    asset = unreal.EditorAssetLibrary().load_asset(asset_path)

    if asset:
        unreal.AssetToolsHelpers.get_asset_tools().export_assets([asset], "C:/Users/Surplus/Desktop/NIA/VR_Export/")
        print(f"✅ MetaHuman {metahuman_name} esportato in VR con successo.")
    else:
        print(f"❌ MetaHuman {metahuman_name} non trovato.")

# Test manuale:
# export_to_vr("MH_Example")


