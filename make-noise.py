#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import argparse
import glob
import os, operator, sys
import random
import soundfile as sf
import uuid
import sox
import configparser as CP
import math

def augment(source_dir, dest_dir, target_qty, target_length, debug, noise_dir, noise_vol, noise_percent):

  if not os.path.exists(source_dir):
    print("Source_dir = " + source_dir + " does not exist!")
    exit()
  if debug == 0:  
    logging.getLogger('sox').setLevel(logging.ERROR)
  else:
    logging.getLogger('sox').setLevel(logging.DEBUG)
    
  sample_rate = 16000
  noise_samples = glob.glob(os.path.join(noise_dir, '*.wav'))
  noise_qty = len(noise_samples)  
  sample_qty = math.ceil(target_qty / noise_qty)
  print(sample_qty)
  #exit()
  if noise_qty < 1:
    print("No noise files found *.wav")
    exit()
  if not os.path.exists(dest_dir):
    print("dest dir is missing")
    exit()
  if not os.path.exists('effects.ini'):
    print("effects.ini is missing")
    exit()
  
  cfg = CP.ConfigParser()
  cfg.read('effects.ini')
  qty = 0
  for noise_wav in noise_samples:
    while qty < sample_qty:
      if os.path.splitext(noise_wav)[1] == ".wav":
        augment_wav(noise_wav, dest_dir, cfg, sample_rate, target_length, qty + 1, noise_wav, noise_vol, noise_percent)
        qty += 1
      else:
        print(noise_wav + ' is not a .wav')
    qty = 0

def augment_wav(wav, dest_dir, cfg, sample_rate, target_length, version, noise_wav, noise_vol, noise_percent):

    target_samples = int(sample_rate * target_length)
    noise_length = sox.file_info.duration(noise_wav)
    if noise_length > target_length:
      offset = (noise_length - target_length) * random.random()
    else:
      print("Noise file to short for target length")
    tfm2 = sox.Transformer()
    tfm2.clear_effects()
    tfm2.norm(-0.1)
    tfm2.trim(offset, target_length + offset)
    tfm2.fade(fade_in_len=0.02, fade_out_len=0.02)
    out = os.path.splitext(noise_wav)[0] + '-bld-' + str(version) + '.wav'
    out = dest_dir + "/" + os.path.basename(out)
    tfm2.build_file(noise_wav, out)
    print(out)
    
def main_body():
  parser = argparse.ArgumentParser()
  parser.add_argument('--source_dir', default='./kw', help='source dir location')
  parser.add_argument('--dest_dir', default='./dest', help='dest dir location')
  parser.add_argument('--target_qty', type=int, default=4000, help='Final qty of augmented audio files')
  parser.add_argument('--target_length', type=float, default=1.0, help='Target length of audio files to be trimmed to (s)')
  parser.add_argument('--debug', help='debug effect settings to cli', action="store_true")
  parser.add_argument('--noise_dir', default='./noise', help='noise dir location')
  parser.add_argument('--noise_vol', type=float, default=0.3, help='Max Vol of noise background mix (0.3)')
  parser.add_argument('--noise_percent', type=float, default=0.9, help='Percent of KW to add noise to (0.9)')
  args = parser.parse_args()
  
  augment(args.source_dir, args.dest_dir, args.target_qty, args.target_length, args.debug, args.noise_dir, args.noise_vol, args.noise_percent)
    
if __name__ == '__main__':
  main_body()

