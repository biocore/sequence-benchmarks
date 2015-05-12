import pandas as pd

class Benchmark(dict):
    def __init__(self, category):
        self.category = category
        super(Benchmark, self).__init__()

    def __call__(self, func):
        name = func.__name__
        get_ipython().user_global_ns[name] = func
        self[name] = get_ipython().magic("%%timeit -o %s()" % name).best
        return func

    def record(self, fp):
        return pd.concat([pd.Series(self, name=self.category)], axis=1).to_csv(fp)
