Dataset **STARE** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/K/o/wi/UWDOE0nkS6IFtMZnsKTGi61unsJfRR2mbRw3LS00mrk2F6RMPtjWj3SLwg03Hzyrv5pKRCmt81hvAgVsO927l7vp2dGRJJdDBxl5hmaBY0lkFmr0SvxUbhqBwQZL.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='STARE', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Images](https://cecas.clemson.edu/~ahoover/stare/images/all-images.zip)
- [Adam Hoover labelled data](https://cecas.clemson.edu/~ahoover/stare/probing/labels-ah.tar)
- [Valentina Kouznetsova labelled data](https://cecas.clemson.edu/~ahoover/stare/probing/labels-vk.tar)
- [Spatial filter probing algorithm labelled data](https://cecas.clemson.edu/~ahoover/stare/probing/results-4.tar)
