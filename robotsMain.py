from Field import Field

for games in range(0, 100, 1):
  field = Field()
  for Time in range(0,150,1):
    if Time <=15:
      field.auto_tick(Time)
      field.auto_cube_tracking_output()
      field.auto_time_controlled_output()
      field.auto_vault_output()
    else:
      field.tick(Time)
  
  field.baseline_points()  
  field.endgame_scoring()
  field.checkIfWin()

  #outputs
  field.powerup_output()
  field.set_output_skills()
  field.time_controlled_output()
  field.auto_time_controlled_output()
  field.vault_output()
  field.auto_vault_output()
  field.endgame_output()
  field.total_points()
  field.cube_tracking_output()
  field.auto_cube_tracking_output()
  

  #field.output.final_print()

  field.output.write_file()