from __future__ import division
from . import base


class Dataset(
    base.AdaMixin('gesture'),
    base.PrevMixin,
    base.StepMixin,
    base.SDataDataset
):
    pass
