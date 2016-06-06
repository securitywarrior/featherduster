import cryptanalib as ca
import feathermodules

ecb_cpa_decrypt_attack_script_skeleton = """# Generated by FeatherDuster
import cryptanalib as ca

def encryption_oracle(text):
   # TODO: Write a function to interact with the ECB encryption oracle
   # Pseudocode:
   # Send text to the encryption oracle
   # Retrieve ciphertext from encryption oracle response
   # Decode ciphertext if encoded
   # return ciphertext

ca.ecb_cpa_decrypt(encryption_oracle=encryption_oracle, block_size=%r, verbose=True, hollywood=%r)

"""

def generate_ecb_cpa_decrypt_attack_script(ciphertexts):
   arguments = get_arguments(ciphertexts)
   while True:
      filename = raw_input('Please enter a file name for the ECB secret suffix decryption script: ')
      try:
         print '[+] Attempting to write script...'
         fh = open(filename, 'w')
         fh.write(ecb_cpa_decrypt_attack_script_skeleton % (arguments['blocksize'],arguments['hollywood']))
         fh.close()
         break
      except:
         print '[*] Couldn\'t write to the file with the name provided. Please try again.'
         continue
   print '[+] Done! Your script is available at %s' % filename

def get_arguments(ciphertexts):
   arguments = {}
   arguments['ciphertexts'] = ciphertexts
   analysis_results = ca.analyze_ciphertext(ciphertexts)
   blocksize = analysis_results['blocksize']
   while True:
      print '[+] Block size detected as %d' % blocksize
      blocksize_answer = raw_input('Is this correct (yes)? ')
      if blocksize_answer.lower() in ['', 'yes', 'y']:
         arguments['blocksize'] = blocksize
         break
      else:
         blocksize_answer = raw_input('Please enter the correct blocksize: ')
         try:
            arguments['blocksize'] = int(blocksize_answer)
            break
         except:
            print '[*] Answer could not be interpreted as a number. Defaulting to detected block size.'
            arguments['blocksize'] = blocksize
            continue
   
   hollywood_answer = raw_input('Do you want hacker movie style output at a minor cost to performance (no I am lame)? ')
   arguments['hollywood'] = (hollywood_answer.lower() in ['','n','no','no i am lame'])
 
   return arguments


feathermodules.module_list['ecb_cpa_decrypt'] = {
   'attack_function':generate_ecb_cpa_decrypt_attack_script,
   'type':'block',
   'keywords':['ecb'],
   'description':'Generate an attack script to decrypt a secret suffix added to data by an ECB mode encryption oracle.',
   'options':{}
}
