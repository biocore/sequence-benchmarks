import pandas as pd

class Benchmark(dict):
    def __init__(self, category):
        self.category = category
        super(Benchmark, self).__init__()

    def __call__(self, func):
        name = func.__name__
        if name in self:
            raise Exception("%s is already defined as a benchmark." % name)
        get_ipython().user_global_ns[name] = func
        self[name] = get_ipython().magic("%%timeit -o %s()" % name).best
        return func

    def as_series(self):
        return pd.Series(self, name=self.category)
