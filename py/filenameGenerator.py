import string
import random


class FilenameGenerator:

    def generate_name(self):
        filename = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
        return filename
