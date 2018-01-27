from Field import Field


Field = Field()

for Time in range(0,150,1):
  if Time <=15:
    pass
    ##add in auto points
   #Field.auto_tick(Time)
  else:
    Field.tick(Time)

Field.endgame_scoring()
Field.checkIfWin()


  