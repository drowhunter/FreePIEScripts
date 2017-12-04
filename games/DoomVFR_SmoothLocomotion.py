if starting:
	deadzone=0.2
w=oculusVR.leftStickY < -deadzone
s=oculusVR.leftStickY > deadzone
a=oculusVR.leftStickX < -deadzone
d=oculusVR.leftStickX > deadzone
lookleft=oculusVR.rightStickX < -deadzone
lookright=oculusVR.rightStickX > deadzone
turnaround=oculusVR.x or oculusVR.a

keyboard.setKey(Key.W, w)
keyboard.setKey(Key.S, s)
keyboard.setKey(Key.A, a)
keyboard.setKey(Key.D, d)
keyboard.setKey(Key.O, lookleft)
keyboard.setKey(Key.P, lookright)
keyboard.setKey(Key.U, turnaround)

diagnostics.watch(w)
diagnostics.watch(s)
diagnostics.watch(a)
diagnostics.watch(d)
diagnostics.watch(lookleft)
diagnostics.watch(lookright)
diagnostics.watch(turnaround)