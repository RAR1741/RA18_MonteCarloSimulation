from Field import Field

for games in range(1, 5, 1):
  field = Field()
  for Time in range(0,150,1):
    if Time <=15:
      field.auto_tick(Time)
    else:
      field.tick(Time)
  field.endgame_scoring()
  field.checkIfWin()
  field.baseline_points()

