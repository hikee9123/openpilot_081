import json
import os


json_file_name = '/data/openpilot/atom_3.json'

class kegman_conf():
  def __init__(self, CP=None):
    self.config = None
    self.init = { 
        "learnerParams": 1,
        "ap_autoReasume": 1,
        "ap_autoScnOffTime": 10,
        "tun_type": "lqr",
        "cv_KPH": [10,60],
        "cv_BPV": [[100,255],[100,255]],
        "cv_sMaxV": [[500,500],[500,500]],
        "cv_sdDNV": [[2,1],[5,1]],
        "cv_sdUPV": [[1,1],[3,1]],
        "sR_KPH": [10,60],
        "sR_BPV": [[100,255],[100,255]],
        "sR_lqr_kiV": [[0.02,0.01],[0.02,0.01]],
        "sR_lqr_scaleV": [[1850,1950],[1850,1950]],
        "sR_pid_KpV": [[0.25,0.25],[0.25,0.25]],
        "sR_pid_KiV": [[0.02,0.02],[0.02,0.02]],
        "sR_pid_KdV": [[1.5,1.5],[1.5,1.5]],
        "sR_pid_deadzone": 0.1,
        "sR_steerRatioV": [[17.5,15.0],[17.5,15.0]],
        "sR_ActuatorDelayV": [[0.1,0.2]],
        "steerLimitTimer": 0.8,
        "steerOffset": 0.0,
        "steerRateCost": 0.8,
        "cameraOffset": 0.00
         }


  def data_check(self, name, value ):
    if name not in self.config:
        self.config.update({name:value})
        self.element_updated = True


  def read_config(self):
    self.element_updated = False

    if os.path.isfile( json_file_name ):
      with open( json_file_name, 'r') as f:
        str_kegman = f.read()
        print( str_kegman )
        self.config = json.loads(str_kegman)

      for name in self.init:
        self.data_check( name, self.init[name] )

      if self.element_updated:
        print("updated")
        self.write_config(self.config)

    else:
      self.config = self.init      
      self.write_config(self.config)

    return self.config

  def write_config(self, config):
    try:
      with open( json_file_name, 'w') as f:
        json.dump(self.config, f, indent=2, sort_keys=True)
        os.chmod( json_file_name, 0o764)
    except IOError:
      os.mkdir('/data')
      with open( json_file_name, 'w') as f:
        json.dump(self.config, f, indent=2, sort_keys=True)
        os.chmod( json_file_name, 0o764)
