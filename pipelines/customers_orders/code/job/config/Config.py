from prophecy.config import ConfigBase


class Sdfsdf(ConfigBase):
    def __init__(self, prophecy_spark=None, asdf: str="sdf", **kwargs):
        self.asdf = asdf
        pass


class Config(ConfigBase):

    def __init__(self, sdfsdf: dict=None, anot: str=None, spexpr: str=None, anotherstr: str=None, **kwargs):
        self.spark = None
        self.update(sdfsdf, anot, spexpr, anotherstr)

    def update(
            self,
            sdfsdf: dict={},
            anot: str="asdf",
            spexpr: str="concat(a,b)",
            anotherstr: str="Config.anot",
            **kwargs
    ):
        prophecy_spark = self.spark
        self.sdfsdf = self.get_config_object(prophecy_spark, Sdfsdf(prophecy_spark = prophecy_spark), sdfsdf, Sdfsdf)
        self.anot = anot
        self.spexpr = spexpr
        self.anotherstr = anotherstr
        pass
