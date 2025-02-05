import unreal

def create_metahuman(description):
    """
    Crea un MetaHuman in Unreal Engine 5 con le caratteristiche descritte.
    """
    factory = unreal.MetaHumanIdentityFactory.new()
    metahuman = factory.create_new_meta_human_identity()
    metahuman.set_editor_property("Description", description)

    unreal.EditorAssetLibrary().save_loaded_asset(metahuman)
    print(f"✅ MetaHuman creato con descrizione: {description}")
    return metahuman

# Test manuale:
# create_metahuman("Uomo con capelli castani e occhi verdi")

