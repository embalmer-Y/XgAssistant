import time

from tqdm import tqdm


def process_bar():
    for _ in tqdm(range(100)):
        time.sleep(0.06)
