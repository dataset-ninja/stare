Dataset **STARE** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzM0NTVfU1RBUkUvc3RhcmUtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiY09nZXdIZWovd0VUUWZlUFVVSTZDS3JMWEhLWVRLUEhLY1dXSzRwY21SND0ifQ==)

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
