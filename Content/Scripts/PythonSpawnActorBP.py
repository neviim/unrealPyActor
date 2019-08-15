import unreal_engine as ue

from unreal_engine.classes import BlueprintGeneratedClass
from unreal_engine import FVector, FRotator

#
# Spawn um actor num BP
#

# Cherche o editor UE4
world = ue.get_editor_world()

# Load o Blueprint BP_Spiral
#bp_actor = ue.load_object(BlueprintGeneratedClass, '/Game/Jads/Blueprints/BP_Spiral.BP_Spiral')

# Spawn o BP na coordenadas localizadas em, FVector e rotasao FRotator
#actor0 = world.actor_spawn(bp_actor, FVector(0, 0, 0), FRotator(0, 0, 0))
