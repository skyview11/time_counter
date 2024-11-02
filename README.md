# Time counter

## Introduction
While 문 안에서 시간 기록할 때 쓰셈. 

## How to use

### import the module first
``` python
from time_counter import TimeCounter
```

### initialize the object 
``` python
counter = TimeCounter(name:"example", record_past=True, n_record=10000)
```
#### `name`: name of the counter, not used in code, but for utilization for your implementation
#### `record_past`: option for record past checkpoints. If do, you can use more features of the module
#### `n_record`: The maximum history number you can record. Not used if use set `record_past` false

### Record
while 문 안에서 특정 동작을 반복하는 코드를 작성하는 상황 가정. 

```python
counter = TimeCounter
while True:
    counter.record_start(name="ex1", make_new=True)
    time.sleep(0.5)
    counter.record_stop(name="ex1")

counter.print_ckpt(mode="period")
counter.save_history(path="example.json")
```
#### `counter.record_start`: start record with name "ex1" you may stop the record by using the name defined here
#### `counter.record_stop`: stop the record named "ex1"
#### `counter.print_ckpt`: print all recorded time (started + stopped)
#### `counter.save_history`: save the record history. Ths method can be used only when `record_past` option is true