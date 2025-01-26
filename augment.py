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
import shortuuid

def augment(source_dir, dest_dir, target_qty, target_length, debug, noise_dir, noise_vol, noise_percent):

  if not os.path.exists(source_dir):
    print("Source_dir = " + source_dir + " does not exist!")
    exit()
  if debug == 0:  
    logging.getLogger('sox').setLevel(logging.ERROR)
  else:
    logging.getLogger('sox').setLevel(logging.DEBUG)
    
  sample_rate = 16000
  #dirpath = os.path.abspath(source_dir)
  #all_files = ( os.path.join(basedir, filename) for basedir, dirs, files in os.walk(dirpath) for filename in files   )
  #sorted_files = sorted(all_files, key = os.path.getsize, reverse = True)
  samples = glob.glob(os.path.join(source_dir, '*.wav'))
  source_qty = len(samples)
  noise_samples = glob.glob(os.path.join(noise_dir, '*.wav'))
  noise_qty = len(noise_samples)  
  print(source_qty, noise_qty)
  sample_qty = math.ceil(target_qty / source_qty)
  if source_qty < 1:
    print("No source files found *.wav")
    exit()
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
  for target_wav in samples:
    qty = 0
    while qty < sample_qty:
      if os.path.splitext(target_wav)[1] == ".wav":
        noise_wav = noise_samples[int(noise_qty * random.random())]
        augment_wav(target_wav, dest_dir, cfg, sample_rate, target_length, qty + 1, noise_wav, noise_vol, noise_percent)
        qty += 1
      else:
        print(target_wav + ' is not a .wav')

def augment_wav(wav, dest_dir, cfg, sample_rate, target_length, version, noise_wav, noise_vol, noise_percent):

    rand_effect = random.random()
    #wav_length = sox.file_info.duration(wav)
    target_samples = int(sample_rate * target_length)
    tfm1 = sox.Transformer()
    tfm1.clear_effects()
    tfm1.norm(-2)
    str_effect = ""
    if rand_effect < 0.33:
      pitch = random.randrange(int(cfg['pitch']['n_semitones_min']), int(cfg['pitch']['n_semitones_max'])) / 1000
      tfm1.pitch(n_semitones=pitch)
      str_effect = str_effect + "-pit"

    elif rand_effect < 0.66:
      tempo = random.randrange(int(cfg['tempo']['factor_min']), int(cfg['tempo']['factor_max'])) / 1000
      tfm1.tempo(factor=tempo, audio_type='s')
      str_effect = str_effect + "-tem"

    elif rand_effect < 1:
      speed = random.randrange(int(cfg['speed']['factor_min']), int(cfg['speed']['factor_max'])) / 1000
      tfm1.speed(factor=speed)
      str_effect = str_effect + "-spd"

    else:
      str_effect =""
    rand_effect = random.random()
    if rand_effect < 0.5:
      gain = random.randrange(int(cfg['treble']['gain_min']), int(cfg['treble']['gain_max'])) / 1000
      freq = random.randrange(int(cfg['treble']['freq_min']), int(cfg['treble']['freq_max'])) / 10
      slope = random.randrange(int(cfg['treble']['slope_min']), int(cfg['treble']['slope_max'])) / 1000
      tfm1.treble(gain_db=gain, frequency=freq, slope=slope)
      str_effect = str_effect + "-t"

    rand_effect = random.random()
    if rand_effect < 0.5:
      gain = random.randrange(int(cfg['bass']['gain_min']), int(cfg['bass']['gain_max'])) / 1000
      freq = random.randrange(int(cfg['bass']['freq_min']), int(cfg['bass']['freq_max'])) / 100
      slope = random.randrange(int(cfg['bass']['slope_min']), int(cfg['bass']['slope_max'])) / 1000
      tfm1.bass(gain_db=gain, frequency=freq, slope=slope)
      str_effect = str_effect + "-b"
           
    array_out1 = tfm1.build_array(input_filepath=wav, sample_rate_in=sample_rate)
    #print(len(array_out1) / 16000)
    tfm1.clear_effects()
    tfm1.fade(fade_in_len=0.02, fade_out_len=0.02)
    if len(array_out1) <= target_samples:
      target_pad = ((target_samples - len(array_out1)) / 2) / sample_rate
      tfm1.pad(start_duration = target_pad, end_duration = target_length + 0.1)
    tfm1.trim(0, target_length)
    tfm1.norm(-0.1)
    if random.random() < noise_percent:    
      out = os.path.splitext(wav)[0] + '-cbn-' + str(version) + str_effect + '.wav'
      out = dest_dir + "/" + shortuuid.uuid() + '_' + os.path.basename(out)
      tfm1.build_file(input_array=array_out1, sample_rate_in=sample_rate, output_filepath='/tmp/sample.wav')
      noise_length = sox.file_info.duration(noise_wav)
      if noise_length > target_length:
        offset = (noise_length - target_length) * random.random()
      else:
        print("Noise file to short for target length")
      tfm2 = sox.Transformer()
      tfm2.clear_effects()
      tfm2.trim(offset, target_length + offset)
      tfm2.fade(fade_in_len=0.02, fade_out_len=0.02)
      tfm2.norm(-0.1)
      tfm2.build_file(noise_wav, '/tmp/noise.wav')
      noise_lvl = noise_vol * random.random()
      cbn = sox.Combiner()
      cbn.build(['/tmp/sample.wav', '/tmp/noise.wav'], out, 'mix', [1.0, noise_lvl])
    else:
      out = os.path.splitext(wav)[0] + '-bld-' + str(version) + str_effect + '.wav'
      out = dest_dir + "/" + shortuuid.uuid() + '_' + os.path.basename(out)
      tfm1.build_file(input_array=array_out1, sample_rate_in=sample_rate, output_filepath=out)
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

