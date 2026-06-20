import hashlib

def generate_hash(filepath):

    sha256 = hashlib.sha256()

    with open(filepath, 'rb') as file:

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()