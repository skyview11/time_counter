from time_counter import TimeCounter
import time
import random

def main() :
    counter = TimeCounter(name="example", record_past=True)
    t0 = time.time()
    while time.time()-t0 < 1:
        for i in range(10000):
            counter.record_start(f"ex{i}", make_new=True)
        for i in range(10000):
            counter.record_stop(f"ex{i}")
    counter.save_history("example.json")
if __name__ == "__main__":
    main()