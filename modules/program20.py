import hashlib
from tqdm import tqdm

# List of supported hash types
hash_names = [
    'blake2b', 
    'blake2s', 
    'md5', 
    'sha1', 
    'sha224', 
    'sha256', 
    'sha384', 
    'sha3_224', 
    'sha3_256', 
    'sha3_384', 
    'sha3_512', 
    'sha512',
]

def crack_hash(hash, wordlist, hash_type=None):
    hash_fn = getattr(hashlib, hash_type, None)
    if hash_fn is None or hash_type not in hash_names:
        # not supported hash type
        raise ValueError(f'[!] Invalid hash type: {hash_type}, supported are {hash_names}')
    # Count the number of lines in the wordlist to set the total
    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:  # Specify encoding and handle errors
        total_lines = sum(1 for line in f)
    print(f"[*] Cracking hash {hash} using {hash_type} with a list of {total_lines} words.")
    # open the wordlist
    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:  # Specify encoding and handle errors
        # iterate over each line
        for line in tqdm(f, desc='Cracking hash', total=total_lines):
            if hash_fn(line.strip().encode()).hexdigest() == hash:
                return line
    
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Crack a hash using a wordlist.')
    parser.add_argument('hash', help='The hash to crack.')
    parser.add_argument('wordlist', help='The path to the wordlist.')
    parser.add_argument('--hash-type', help='The hash type to use.', default='md5')
    args = parser.parse_args()
    print()
    print("[+] Found password:", crack_hash(args.hash, args.wordlist, args.hash_type))
