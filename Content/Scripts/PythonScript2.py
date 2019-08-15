import unreal_engine as ue

print("Ola este é seu pipeline automator")

class Hero:
    # Chamada do Game Start
    def begin_play(self):
        ue.log("Inicia play na class Hero")

    # Chamada do evento 'tick'
    def tick(self, delta_time):
        # le a corrente locação
        location = self.uobject.get_actor_location()

        # incrementa X honouring delta_time
        location.z += 100 * delta_time

        # set nova locação
        self.uobject.set_actor_location(location)