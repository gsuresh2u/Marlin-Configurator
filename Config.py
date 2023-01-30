
import os
import configparser

import re

configfile = "Config.ini"


# Check if there is already a configurtion file
if not os.path.isfile(configfile):
    cfgfile = open(configfile, "w") # Create the configuration file as it doesn't exist yet

    # Add content to the file
    Config = configparser.ConfigParser()
    Config.add_section("platformio")
    Config.set("platformio", "default_envs          ", "mega2560")

    Config.add_section("Configuration.h")
    Config.set("Configuration.h","motherboard           ","FLYF407ZG")
    Config.set("Configuration.h","serial_port           ","-1")
    Config.set("Configuration.h","serial_port_2         ","none")
    Config.set("Configuration.h","serial_port_3         ","none")
    Config.set("Configuration.h","baudrate              ","250000")

    Config.set("Configuration.h","\nx_motors              ","1")
    Config.set("Configuration.h","y_motors              ","1")
    Config.set("Configuration.h","z_motors              ","1")
    Config.set("Configuration.h","extruders             ","1")

    Config.set("Configuration.h","\nx_driver_type         ","A4988")
    Config.set("Configuration.h","x2_driver_type        ","")
    Config.set("Configuration.h","y_driver_type         ","A4988")
    Config.set("Configuration.h","y2_driver_type        ","")
    Config.set("Configuration.h","z_driver_type         ","A4988")
    Config.set("Configuration.h","z2_driver_type        ","")
    Config.set("Configuration.h","z3_driver_type        ","")
    Config.set("Configuration.h","z4_driver_type        ","")
    Config.set("Configuration.h","e0_driver_type        ","A4988")
    Config.set("Configuration.h","e1_driver_type        ","")
    Config.set("Configuration.h","e2_driver_type        ","")
    Config.set("Configuration.h","e3_driver_type        ","")
    Config.set("Configuration.h","e4_driver_type        ","")
    Config.set("Configuration.h","e5_driver_type        ","")
    Config.set("Configuration.h","e6_driver_type        ","")
    Config.set("Configuration.h","e7_driver_type        ","")

    Config.set("Configuration.h","\ntemp_sensor_0        ","1")
    Config.set("Configuration.h","temp_sensor_1        ","0")
    Config.set("Configuration.h","temp_sensor_2        ","0")
    Config.set("Configuration.h","temp_sensor_3        ","0")
    Config.set("Configuration.h","temp_sensor_4        ","0")
    Config.set("Configuration.h","temp_sensor_5        ","0")
    Config.set("Configuration.h","temp_sensor_6        ","0")
    Config.set("Configuration.h","temp_sensor_bed      ","1")

    Config.set("Configuration.h","hotend_overshoot      ","15")
    Config.set("Configuration.h","bed_overshoot        ","10")
    Config.set("Configuration.h","cooler_overshoot     ","2")

    Config.set("Configuration.h","\nx_bed_size            ","235")
    Config.set("Configuration.h","y_bed_size            ","235")
    Config.set("Configuration.h","x_min_position        ","0")
    Config.set("Configuration.h","y_min_position        ","0")
    Config.set("Configuration.h","z_height              ","240")

    Config.set("Configuration.h","\nuse_xmin_plug          ","on")
    Config.set("Configuration.h","use_ymin_plug          ","on")
    Config.set("Configuration.h","use_zmin_plug          ","on")
    Config.set("Configuration.h","use_xmax_plug          ","on")
    Config.set("Configuration.h","use_ymax_plug          ","off")
    Config.set("Configuration.h","use_zmax_plug          ","off") 

    Config.set("Configuration.h","\nxmin_endstop_invert    ","true")
    Config.set("Configuration.h","ymin_endstop_invert    ","false")
    Config.set("Configuration.h","zmin_endstop_invert    ","false")
    Config.set("Configuration.h","xmax_endstop_invert    ","false")
    Config.set("Configuration.h","ymax_endstop_invert    ","false")
    Config.set("Configuration.h","zmax_endstop_invert    ","false")
    Config.set("Configuration.h","zprobe_invert          ","false")  

    Config.set("Configuration.h","\nxsteps_per_unit         ","80")  
    Config.set("Configuration.h","ysteps_per_unit         ","80")
    Config.set("Configuration.h","zsteps_per_unit         ","100")
    Config.set("Configuration.h","e0steps_per_unit        ","92") 

    Config.set("Configuration.h","\nx_max_feedrate          ","100") 
    Config.set("Configuration.h","y_max_feedrate          ","100") 
    Config.set("Configuration.h","z_max_feedrate          ","5") 
    Config.set("Configuration.h","e0_max_feedrate         ","25")  

    Config.set("Configuration.h","\nx_max_acceleration      ","500")  
    Config.set("Configuration.h","y_max_acceleration      ","500")  
    Config.set("Configuration.h","z_max_acceleration      ","80")  
    Config.set("Configuration.h","e0_max_acceleration     ","1000") 

    Config.set("Configuration.h","\ninvert_x_dir            ","false")  
    Config.set("Configuration.h","invert_y_dir            ","true")  
    Config.set("Configuration.h","invert_z_dir            ","false")  
    Config.set("Configuration.h","invert_e0_dir           ","false") 

    Config.set("Configuration.h","\nx_homing_position       ","min")  
    Config.set("Configuration.h","y_homing_position       ","min")  
    Config.set("Configuration.h","z_homing_position       ","min") 
    
    Config.set("Configuration.h","\nz_min_uses_zendstop_pin   ","on")
    Config.set("Configuration.h","use_probe_for_z_homing    ","off") 
    Config.set("Configuration.h","use_fixed_mounted_probe   ","off")
    Config.set("Configuration.h","use_nozzle_as_probe       ","off")
    Config.set("Configuration.h","use_bltouch               ","on")
    Config.set("Configuration.h","use_sensorless_probing    ","off")
    Config.set("Configuration.h","probing_margin            ","10")
    Config.set("Configuration.h","use_multiple_probing      ","on")
    Config.set("Configuration.h","use_extra_probing         ","off")
    Config.set("Configuration.h","probe_x_offset            ","-35")
    Config.set("Configuration.h","probe_y_offset            ","-18")
    Config.set("Configuration.h","probe_z_offset            ","0")
    Config.set("Configuration.h","use_probing_heaters_off   ","off")
    Config.set("Configuration.h","use_preheat_before_home   ","off")
    Config.set("Configuration.h","use_z_safe_homing         ","on")

    Config.set("Configuration.h","\nleveling_3point        ","off") 
    Config.set("Configuration.h","leveling_linear        ","off")
    Config.set("Configuration.h","leveling_bilinear      ","off")
    Config.set("Configuration.h","leveling_ubl           ","on")
    Config.set("Configuration.h","leveling_mesh          ","off")
    Config.set("Configuration.h","linear_points          ","3")
    Config.set("Configuration.h","ubl_points             ","5")
    Config.set("Configuration.h","mesh_points            ","5") 
    Config.set("Configuration.h","restore_after_g28      ","on")
    Config.set("Configuration.h","preheat_before_level   ","off")
    Config.set("Configuration.h","g26_mesh_validation    ","off")
    Config.set("Configuration.h","lcd_bed_levelling      ","off")

    Config.set("Configuration.h","\nuse_single_nozzle      ","off")
    Config.set("Configuration.h","use_switching_extruder ","off")
    Config.set("Configuration.h","use_switching_nozzle   ","off")
    Config.set("Configuration.h","use_parking_extruder   ","off")
    Config.set("Configuration.h","use_mixing_extruder    ","off")
    Config.set("Configuration.h","mixing_extruder_no     ","2")
    Config.set("Configuration.h","nozzle_park_feature    ","off")
    Config.set("Configuration.h","nozzle_clean_feature   ","off")

    Config.set("Configuration.h","\nuse_psu_conrol         ","off")
    Config.set("Configuration.h","psu_state              ","high")
    Config.set("Configuration.h","wait_for_cooldown      ","off")
    Config.set("Configuration.h","auto_power_control     ","off")
    Config.set("Configuration.h","power_timeout          ","30")
    Config.set("Configuration.h","poweroff_temparature   ","50")

    Config.set("Configuration.h","\nenable_eeprom          ","on")
    Config.set("Configuration.h","reset_on_errors        ","off")
    Config.set("Configuration.h","clear_old_values       ","off")
    Config.set("Configuration.h","use_print_counter      ","off")
    Config.set("Configuration.h","use_sd_support         ","on")
    Config.set("Configuration.h","individial_home_menu   ","on")
    Config.set("Configuration.h","use_speaker            ","on")
    Config.set("Configuration.h","use_filament_sensor    ","off")
    Config.set("Configuration.h","filament_sensor_state  ","high")

    Config.set("Configuration.h","display_type           ","REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER")
    Config.set("Configuration.h","printer_type           ","Cartesian")
    



    Config.add_section("Configuration_adv.h") # Advanced

    Config.set("Configuration_adv.h","extruder_runout_prevent      ","off")
    Config.set("Configuration_adv.h","use_controller_fan           ","off")
    Config.set("Configuration_adv.h","fast_pwm_fan                 ","off")
    Config.set("Configuration_adv.h","extruder_auto_fan_temp       ","50")
    Config.set("Configuration_adv.h","use_bltouch_high_speed       ","off")
    Config.set("Configuration_adv.h","use_z_steppers_auto_align    ","off")
    Config.set("Configuration_adv.h","use_adaptive_step_smoothing  ","off")
    Config.set("Configuration_adv.h","use_powerloss_recovery       ","on")

    Config.set("Configuration_adv.h","\nuse_linear_advance           ","off")
    Config.set("Configuration_adv.h","linear_advance_kfactor       ","0.22")
    Config.set("Configuration_adv.h","use_g29_retry_recover        ","off")
    Config.set("Configuration_adv.h","long_filename_support        ","on")
    Config.set("Configuration_adv.h","scroll_long_filename         ","on")

    Config.set("Configuration_adv.h","\nenable_baby_stepping         ","off")
    Config.set("Configuration_adv.h","inegrated_baby_stepping      ","off")
    Config.set("Configuration_adv.h","baby_step_without_homing     ","off")
    Config.set("Configuration_adv.h","baby_step_always_available   ","off")
    Config.set("Configuration_adv.h","baby_step_on_xy              ","off")

    Config.set("Configuration_adv.h","\nenable_dual_x_carriage       ","off")
    Config.set("Configuration_adv.h","dualx_x2_min_position        ","80")
    Config.set("Configuration_adv.h","dualx_x2_max_position        ","353")
    Config.set("Configuration_adv.h","dualx_duplication_offset     ","100")

    Config.set("Configuration_adv.h","\nenable_x_input_shapping      ","off")
    Config.set("Configuration_adv.h","x_input_shapping_frequency   ","40")
    Config.set("Configuration_adv.h","x_input_shapping_zeta        ","0.15f")
    Config.set("Configuration_adv.h","enable_y_input_shapping      ","off")
    Config.set("Configuration_adv.h","y_input_shapping_frequency   ","40")
    Config.set("Configuration_adv.h","y_input_shapping_zeta        ","0.15f")

    Config.set("Configuration_adv.h","\ntx_buffer_size         ","0")
    Config.set("Configuration_adv.h","use_emergency_parcer    ","off")
    Config.set("Configuration_adv.h","use_advanced_ok         ","off")
    Config.set("Configuration_adv.h","advanced_pause_feature  ","off")
    Config.set("Configuration_adv.h","monitor_driver_status   ","off")
    Config.set("Configuration_adv.h","sensorless_homing       ","off")
    Config.set("Configuration_adv.h","use_tmc_debugging       ","off")
    Config.set("Configuration_adv.h","chopper_voltage         ","CHOPPER_DEFAULT_24V")

    Config.set("Configuration_adv.h","\nx_current            ","800")
    Config.set("Configuration_adv.h","x_micro_steps        ","16")
    Config.set("Configuration_adv.h","x_rense              ","0.11")
    Config.set("Configuration_adv.h","x2_current           ","800")
    Config.set("Configuration_adv.h","x2_micro_steps       ","16")
    Config.set("Configuration_adv.h","x2_rense             ","0.11")
    Config.set("Configuration_adv.h","y_current            ","800")
    Config.set("Configuration_adv.h","y_micro_steps        ","16")
    Config.set("Configuration_adv.h","y_rense              ","0.11")
    Config.set("Configuration_adv.h","y2_current           ","800")
    Config.set("Configuration_adv.h","y2_micro_steps       ","16")
    Config.set("Configuration_adv.h","y2_rense             ","0.11")
    Config.set("Configuration_adv.h","z_current            ","800")
    Config.set("Configuration_adv.h","z_micro_steps        ","16")
    Config.set("Configuration_adv.h","z_rense              ","0.11")
    Config.set("Configuration_adv.h","z2_current           ","800")
    Config.set("Configuration_adv.h","z2_micro_steps       ","16")
    Config.set("Configuration_adv.h","z2_rense             ","0.11")
    Config.set("Configuration_adv.h","z3_current           ","800")
    Config.set("Configuration_adv.h","z3_micro_steps       ","16")
    Config.set("Configuration_adv.h","z3_rense             ","0.11")
    Config.set("Configuration_adv.h","z4_current           ","800")
    Config.set("Configuration_adv.h","z4_micro_steps       ","16")
    Config.set("Configuration_adv.h","z4_rense             ","0.11")

    Config.set("Configuration_adv.h","\ne0_current           ","800")
    Config.set("Configuration_adv.h","e0_micro_steps       ","16")
    Config.set("Configuration_adv.h","e0_rense             ","0.11")
    Config.set("Configuration_adv.h","e1_current           ","800")
    Config.set("Configuration_adv.h","e1_micro_steps       ","16")
    Config.set("Configuration_adv.h","e1_rense             ","0.11")
    Config.set("Configuration_adv.h","e2_current           ","800")
    Config.set("Configuration_adv.h","e2_micro_steps       ","16")
    Config.set("Configuration_adv.h","e2_rense             ","0.11")
    Config.set("Configuration_adv.h","e3_current           ","800")
    Config.set("Configuration_adv.h","e3_micro_steps       ","16")
    Config.set("Configuration_adv.h","e3_rense             ","0.11")
    Config.set("Configuration_adv.h","e4_current           ","800")
    Config.set("Configuration_adv.h","e4_micro_steps       ","16")
    Config.set("Configuration_adv.h","e4_rense             ","0.11")
    Config.set("Configuration_adv.h","e5_current           ","800")
    Config.set("Configuration_adv.h","e5_micro_steps       ","16")
    Config.set("Configuration_adv.h","e5_rense             ","0.11")
    Config.set("Configuration_adv.h","e6_current           ","800")
    Config.set("Configuration_adv.h","e6_micro_steps       ","16")
    Config.set("Configuration_adv.h","e6_rense             ","0.11")
    Config.set("Configuration_adv.h","e7_current           ","800")
    Config.set("Configuration_adv.h","e7_micro_steps       ","16")
    Config.set("Configuration_adv.h","e7_rense             ","0.11")

    
    Config.write(cfgfile)
    cfgfile.close()

if os.path.isfile(configfile):
    Config = configparser.ConfigParser()
    Config.read(configfile)
    #print(Config.get("platformio", "default_envs"))
    #print(Config.get("Configuration.h", "x_driver_type"))
    default_envs = Config.get("platformio", "default_envs")

    motherboard = Config.get("Configuration.h", "motherboard")
    serial_port = Config.get("Configuration.h", "serial_port")
    serial_port_2 = Config.get("Configuration.h", "serial_port_2")
    serial_port_3 = Config.get("Configuration.h", "serial_port_3")
    baudrate = Config.get("Configuration.h", "baudrate")
    x_motors = Config.get("Configuration.h", "x_motors")
    y_motors = Config.get("Configuration.h", "y_motors")
    z_motors = Config.get("Configuration.h", "z_motors")
    extruders = Config.get("Configuration.h", "extruders")

    x_driver_type = Config.get("Configuration.h", "x_driver_type")
    x2_driver_type = Config.get("Configuration.h", "x2_driver_type")
    y_driver_type = Config.get("Configuration.h", "y_driver_type")
    y2_driver_type = Config.get("Configuration.h", "y2_driver_type")
    z_driver_type = Config.get("Configuration.h", "z_driver_type")
    z2_driver_type = Config.get("Configuration.h", "z2_driver_type")
    z3_driver_type = Config.get("Configuration.h", "z3_driver_type")
    z4_driver_type = Config.get("Configuration.h", "z4_driver_type")
    e0_driver_type = Config.get("Configuration.h", "e0_driver_type")
    e1_driver_type = Config.get("Configuration.h", "e1_driver_type")
    e2_driver_type = Config.get("Configuration.h", "e2_driver_type")
    e3_driver_type = Config.get("Configuration.h", "e3_driver_type")
    e4_driver_type = Config.get("Configuration.h", "e4_driver_type")
    e5_driver_type = Config.get("Configuration.h", "e5_driver_type")
    e6_driver_type = Config.get("Configuration.h", "e6_driver_type")
    e7_driver_type = Config.get("Configuration.h", "e7_driver_type")

    temp_sensor_0   = Config.get("Configuration.h", "temp_sensor_0")
    temp_sensor_1   = Config.get("Configuration.h", "temp_sensor_1")
    temp_sensor_2   = Config.get("Configuration.h", "temp_sensor_2")
    temp_sensor_3   = Config.get("Configuration.h", "temp_sensor_3")
    temp_sensor_4   = Config.get("Configuration.h", "temp_sensor_4")
    temp_sensor_5   = Config.get("Configuration.h", "temp_sensor_5")
    temp_sensor_6   = Config.get("Configuration.h", "temp_sensor_6")
    temp_sensor_bed = Config.get("Configuration.h", "temp_sensor_bed")

    hotend_overshoot = Config.get("Configuration.h", "hotend_overshoot")
    bed_overshoot = Config.get("Configuration.h", "bed_overshoot")
    cooler_overshoot = Config.get("Configuration.h", "cooler_overshoot")


    use_xmin_plug = Config.get("Configuration.h", "use_xmin_plug")
    use_ymin_plug = Config.get("Configuration.h", "use_ymin_plug")
    use_zmin_plug = Config.get("Configuration.h", "use_zmin_plug")
    use_xmax_plug = Config.get("Configuration.h", "use_xmax_plug")
    use_ymax_plug = Config.get("Configuration.h", "use_ymax_plug")
    use_zmax_plug = Config.get("Configuration.h", "use_zmax_plug")

    xmin_endstop_invert = Config.get("Configuration.h", "xmin_endstop_invert") #true
    ymin_endstop_invert = Config.get("Configuration.h", "ymin_endstop_invert") #false
    zmin_endstop_invert = Config.get("Configuration.h", "zmin_endstop_invert") #false
    xmax_endstop_invert = Config.get("Configuration.h", "xmax_endstop_invert") #false
    ymax_endstop_invert = Config.get("Configuration.h", "ymax_endstop_invert") #false
    zmax_endstop_invert = Config.get("Configuration.h", "zmax_endstop_invert") #false
    zprobe_invert       = Config.get("Configuration.h", "zprobe_invert") #false

    xsteps_per_unit     = Config.get("Configuration.h", "xsteps_per_unit")
    ysteps_per_unit     = Config.get("Configuration.h", "ysteps_per_unit")
    zsteps_per_unit     = Config.get("Configuration.h", "zsteps_per_unit")
    e0steps_per_unit    = Config.get("Configuration.h", "e0steps_per_unit")

    x_max_feedrate  = Config.get("Configuration.h", "x_max_feedrate")
    y_max_feedrate  = Config.get("Configuration.h", "y_max_feedrate")
    z_max_feedrate  = Config.get("Configuration.h", "z_max_feedrate")
    e0_max_feedrate = Config.get("Configuration.h", "e0_max_feedrate")

    x_max_acceleration  = Config.get("Configuration.h", "x_max_acceleration")
    y_max_acceleration  = Config.get("Configuration.h", "y_max_acceleration")
    z_max_acceleration  = Config.get("Configuration.h", "z_max_acceleration")
    e0_max_acceleration = Config.get("Configuration.h", "e0_max_acceleration")

    invert_x_dir    = Config.get("Configuration.h", "invert_x_dir")
    invert_y_dir    = Config.get("Configuration.h", "invert_y_dir")
    invert_z_dir    = Config.get("Configuration.h", "invert_z_dir")
    invert_e0_dir   = Config.get("Configuration.h", "invert_e0_dir")

    x_homing_position = Config.get("Configuration.h", "x_homing_position")
    y_homing_position = Config.get("Configuration.h", "y_homing_position")
    z_homing_position = Config.get("Configuration.h", "z_homing_position")

    x_bed_size      = Config.get("Configuration.h", "x_bed_size")
    y_bed_size      = Config.get("Configuration.h", "y_bed_size")
    x_min_position  = Config.get("Configuration.h", "x_min_position")
    y_min_position  = Config.get("Configuration.h", "y_min_position")
    z_height        = Config.get("Configuration.h", "z_height")

    # Z-Probe Tab Options ~~~~~~~~~~~~~~~~~
    z_min_uses_zendstop_pin     = Config.get("Configuration.h", "z_min_uses_zendstop_pin")
    use_probe_for_z_homing      = Config.get("Configuration.h", "use_probe_for_z_homing")
    use_fixed_mounted_probe     = Config.get("Configuration.h", "use_fixed_mounted_probe")
    use_nozzle_as_probe         = Config.get("Configuration.h", "use_nozzle_as_probe")
    use_bltouch                 = Config.get("Configuration.h", "use_bltouch")
    use_sensorless_probing      = Config.get("Configuration.h", "use_sensorless_probing")
    probing_margin              = Config.get("Configuration.h", "probing_margin")
    use_multiple_probing        = Config.get("Configuration.h", "use_multiple_probing")
    use_extra_probing           = Config.get("Configuration.h", "use_extra_probing")
    probe_x_offset              = Config.get("Configuration.h", "probe_x_offset")
    probe_y_offset              = Config.get("Configuration.h", "probe_y_offset")
    probe_z_offset              = Config.get("Configuration.h", "probe_z_offset")
    use_probing_heaters_off     = Config.get("Configuration.h", "use_probing_heaters_off")
    use_preheat_before_home     = Config.get("Configuration.h", "use_preheat_before_home")
    use_z_safe_homing           = Config.get("Configuration.h", "use_z_safe_homing")

    leveling_3point         = Config.get("Configuration.h", "leveling_3point")
    leveling_linear         = Config.get("Configuration.h", "leveling_linear")
    leveling_bilinear       = Config.get("Configuration.h", "leveling_bilinear")
    leveling_ubl            = Config.get("Configuration.h", "leveling_ubl")
    leveling_mesh           = Config.get("Configuration.h", "leveling_mesh")
    linear_points           = Config.get("Configuration.h", "linear_points")
    ubl_points              = Config.get("Configuration.h", "ubl_points")
    mesh_points             = Config.get("Configuration.h", "mesh_points")
    restore_after_g28       = Config.get("Configuration.h", "restore_after_g28")
    preheat_before_level    = Config.get("Configuration.h", "preheat_before_level")
    g26_mesh_validation     = Config.get("Configuration.h", "g26_mesh_validation")
    lcd_bed_levelling       = Config.get("Configuration.h", "lcd_bed_levelling")

    use_single_nozzle       = Config.get("Configuration.h", "use_single_nozzle")    
    use_switching_extruder  = Config.get("Configuration.h", "use_switching_extruder")
    use_switching_nozzle    = Config.get("Configuration.h", "use_switching_nozzle")
    use_parking_extruder    = Config.get("Configuration.h", "use_parking_extruder")
    use_mixing_extruder     = Config.get("Configuration.h", "use_mixing_extruder")
    mixing_extruder_no      = Config.get("Configuration.h", "mixing_extruder_no")
    nozzle_park_feature     = Config.get("Configuration.h", "nozzle_park_feature")
    nozzle_clean_feature    = Config.get("Configuration.h", "nozzle_clean_feature")

    use_psu_conrol          = Config.get("Configuration.h", "use_psu_conrol")
    psu_state               = Config.get("Configuration.h", "psu_state")
    wait_for_cooldown       = Config.get("Configuration.h", "wait_for_cooldown")
    auto_power_control      = Config.get("Configuration.h", "auto_power_control")
    power_timeout           = Config.get("Configuration.h", "power_timeout")
    poweroff_temparature    = Config.get("Configuration.h", "poweroff_temparature")

    enable_eeprom           = Config.get("Configuration.h", "enable_eeprom")
    reset_on_errors         = Config.get("Configuration.h", "reset_on_errors")
    clear_old_values        = Config.get("Configuration.h", "clear_old_values")
    use_print_counter       = Config.get("Configuration.h", "use_print_counter")
    use_sd_support          = Config.get("Configuration.h", "use_sd_support")
    individial_home_menu    = Config.get("Configuration.h", "individial_home_menu")
    use_speaker             = Config.get("Configuration.h", "use_speaker")
    use_filament_sensor     = Config.get("Configuration.h", "use_filament_sensor")
    filament_sensor_state   = Config.get("Configuration.h", "filament_sensor_state")

    display_type            = Config.get("Configuration.h", "display_type")
    printer_type            = Config.get("Configuration.h", "printer_type")





    # Read from Configuration_adv.h
    extruder_runout_prevent         = Config.get("Configuration_adv.h", "extruder_runout_prevent")
    use_controller_fan              = Config.get("Configuration_adv.h", "use_controller_fan")
    fast_pwm_fan                    = Config.get("Configuration_adv.h", "fast_pwm_fan")
    extruder_auto_fan_temp          = Config.get("Configuration_adv.h", "extruder_auto_fan_temp")
    use_bltouch_high_speed          = Config.get("Configuration_adv.h", "use_bltouch_high_speed")
    use_z_steppers_auto_align       = Config.get("Configuration_adv.h", "use_z_steppers_auto_align")
    use_adaptive_step_smoothing     = Config.get("Configuration_adv.h", "use_adaptive_step_smoothing")
    use_powerloss_recovery          = Config.get("Configuration_adv.h", "use_powerloss_recovery")

    use_linear_advance              = Config.get("Configuration_adv.h", "use_linear_advance")
    linear_advance_kfactor          = Config.get("Configuration_adv.h", "linear_advance_kfactor")
    use_g29_retry_recover           = Config.get("Configuration_adv.h", "use_g29_retry_recover")
    long_filename_support           = Config.get("Configuration_adv.h", "long_filename_support")
    scroll_long_filename            = Config.get("Configuration_adv.h", "scroll_long_filename")

    enable_baby_stepping            = Config.get("Configuration_adv.h", "enable_baby_stepping")
    inegrated_baby_stepping         = Config.get("Configuration_adv.h", "inegrated_baby_stepping")
    baby_step_without_homing        = Config.get("Configuration_adv.h", "baby_step_without_homing")
    baby_step_always_available      = Config.get("Configuration_adv.h", "baby_step_always_available")
    baby_step_on_xy                 = Config.get("Configuration_adv.h", "baby_step_on_xy")

    enable_dual_x_carriage          = Config.get("Configuration_adv.h", "enable_dual_x_carriage")
    dualx_x2_min_position           = Config.get("Configuration_adv.h", "dualx_x2_min_position")
    dualx_x2_max_position           = Config.get("Configuration_adv.h", "dualx_x2_max_position")
    dualx_duplication_offset        = Config.get("Configuration_adv.h", "dualx_duplication_offset")

    enable_x_input_shapping        = Config.get("Configuration_adv.h", "enable_x_input_shapping")
    x_input_shapping_frequency      = Config.get("Configuration_adv.h", "x_input_shapping_frequency")
    x_input_shapping_zeta           = Config.get("Configuration_adv.h", "x_input_shapping_zeta")
    enable_y_input_shapping         = Config.get("Configuration_adv.h", "enable_y_input_shapping")
    y_input_shapping_frequency      = Config.get("Configuration_adv.h", "y_input_shapping_frequency")
    y_input_shapping_zeta           = Config.get("Configuration_adv.h", "y_input_shapping_zeta")

    tx_buffer_size         = Config.get("Configuration_adv.h", "tx_buffer_size")
    use_emergency_parcer    = Config.get("Configuration_adv.h", "use_emergency_parcer")
    use_advanced_ok         = Config.get("Configuration_adv.h", "use_advanced_ok")
    advanced_pause_feature  = Config.get("Configuration_adv.h", "advanced_pause_feature")
    monitor_driver_status   = Config.get("Configuration_adv.h", "monitor_driver_status")
    sensorless_homing       = Config.get("Configuration_adv.h", "sensorless_homing")
    use_tmc_debugging       = Config.get("Configuration_adv.h", "use_tmc_debugging")
    chopper_voltage         = Config.get("Configuration_adv.h", "chopper_voltage")
    
    x_current           = Config.get("Configuration_adv.h", "x_current")
    x_micro_steps       = Config.get("Configuration_adv.h", "x_micro_steps")
    x_rense             = Config.get("Configuration_adv.h", "x_rense")
    x2_current          = Config.get("Configuration_adv.h", "x2_current")
    x2_micro_steps      = Config.get("Configuration_adv.h", "x2_micro_steps")
    x2_rense            = Config.get("Configuration_adv.h", "x2_rense")
    y_current           = Config.get("Configuration_adv.h", "y_current")
    y_micro_steps       = Config.get("Configuration_adv.h", "y_micro_steps")
    y_rense             = Config.get("Configuration_adv.h", "y_rense")
    y2_current          = Config.get("Configuration_adv.h", "y2_current")
    y2_micro_steps      = Config.get("Configuration_adv.h", "y2_micro_steps")
    y2_rense            = Config.get("Configuration_adv.h", "y2_rense")
    z_current           = Config.get("Configuration_adv.h", "z_current")
    z_micro_steps       = Config.get("Configuration_adv.h", "z_micro_steps")
    z_rense             = Config.get("Configuration_adv.h", "z_rense")
    z2_current          = Config.get("Configuration_adv.h", "z2_current")
    z2_micro_steps      = Config.get("Configuration_adv.h", "z2_micro_steps")
    z2_rense            = Config.get("Configuration_adv.h", "z2_rense")
    z3_current          = Config.get("Configuration_adv.h", "z3_current")
    z3_micro_steps      = Config.get("Configuration_adv.h", "z3_micro_steps")
    z3_rense            = Config.get("Configuration_adv.h", "z3_rense")
    z4_current          = Config.get("Configuration_adv.h", "z4_current")
    z4_micro_steps      = Config.get("Configuration_adv.h", "z4_micro_steps")
    z4_rense            = Config.get("Configuration_adv.h", "z4_rense")

    e0_current          = Config.get("Configuration_adv.h", "e0_current")
    e0_micro_steps      = Config.get("Configuration_adv.h", "e0_micro_steps")
    e0_rense            = Config.get("Configuration_adv.h", "e0_rense")
    e1_current          = Config.get("Configuration_adv.h", "e1_current")
    e1_micro_steps      = Config.get("Configuration_adv.h", "e1_micro_steps")
    e1_rense            = Config.get("Configuration_adv.h", "e1_rense")
    e2_current          = Config.get("Configuration_adv.h", "e2_current")
    e2_micro_steps      = Config.get("Configuration_adv.h", "e2_micro_steps")
    e2_rense            = Config.get("Configuration_adv.h", "e2_rense")
    e3_current          = Config.get("Configuration_adv.h", "e3_current")
    e3_micro_steps      = Config.get("Configuration_adv.h", "e3_micro_steps")
    e3_rense            = Config.get("Configuration_adv.h", "e3_rense")
    e4_current          = Config.get("Configuration_adv.h", "e4_current")
    e4_micro_steps      = Config.get("Configuration_adv.h", "e4_micro_steps")
    e4_rense            = Config.get("Configuration_adv.h", "e4_rense")
    e5_current          = Config.get("Configuration_adv.h", "e5_current")
    e5_micro_steps      = Config.get("Configuration_adv.h", "e5_micro_steps")
    e5_rense            = Config.get("Configuration_adv.h", "e5_rense")
    e6_current          = Config.get("Configuration_adv.h", "e6_current")
    e6_micro_steps      = Config.get("Configuration_adv.h", "e6_micro_steps")
    e6_rense            = Config.get("Configuration_adv.h", "e6_rense")
    e7_current          = Config.get("Configuration_adv.h", "e7_current")
    e7_micro_steps      = Config.get("Configuration_adv.h", "e7_micro_steps")
    e7_rense            = Config.get("Configuration_adv.h", "e7_rense")










    









