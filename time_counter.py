import time

class TimeCounter:
    def __init__(self, name:str, record_past=True, n_record=10000):
        self.name = name
        self.count_ckpts = {} ## [ckpt_name: (ckpt_id, captured time)]
        self.count_history = {}
        self.record_past = record_past
        self.n_record = n_record
        self.id = 0
    def make_ckpt(self, name):
        assert name not in self.count_ckpts.keys(), "Duplicated name!"
        self.count_ckpts[name] = [self.id, -1]
        
    def record_start(self, name, make_new=False):
        if name in self.count_ckpts.keys():
            self.count_ckpts[name][1] = time.time()
        elif make_new:
            self.count_ckpts[name] = [self.id, time.time()]
            self.id += 1
            self.count_history[name] = []
        else:
            raise RuntimeError
    def record_stop(self, name):
        assert name in self.count_ckpts, "No matching checkpoint"
        assert self.count_history[name][1] != -1, "Start the record first"
        if self.record_past:
            self.count_history[name].append(time.time()-self.count_ckpts[name][1])
            if len(self.count_history[name]) > self.n_record:
                self.count_history[name] = self.count_history[name][-self.n_record:]
        else:
            self.count_history[name] = [time.time()-self.count_ckpts[name][1]]
        
    def print_ckpt(self, mode="period"):
        if mode == "period":
            msg = "Time cost(period): "
            for name, history in self.count_history.items():
                msg = msg + f"{name}: {round(history[-1], 3)} "
        elif mode == "frequency":
            msg = "Time cost(freqency): "
            for name, history in self.count_history.items():
                msg = msg + f"{name}: {round(1/history[-1], 3)} "
        else:
            raise ValueError ("Invalid mode input, mode is 'period' or 'frequency'")
        
        print(msg)
    def save_history(self, path:str):
        assert self.record_past, "No record setting"
        import json
        assert path.endswith(".json"), "Not a json format path"
        with open(path, "w") as f:
            json.dump(self.count_history, f, indent=4, ensure_ascii=False)