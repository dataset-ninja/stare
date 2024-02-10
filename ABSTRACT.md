The **STARE: Structured Analysis of the Retina Dataset** concerns a system to automatically diagnose diseases of the human eye. It was conceived and initiated in 1975. During its history, over thirty people contributed to the project, with backgrounds ranging from medicine to science to engineering. Images and clinical data were provided by the Shiley Eye Center at the University of California, San Diego, and by the Veterans Administration Medical Center in San Diego.


## Motivation

Blood vessel appearance is an important indicator for many diagnoses, including diabetes, hypertension, and arteriosclerosis. Vessels and arteries have many observable features, including diameter, color, tortuosity (relative curvature), and opacity (reflectivity). Artery-vein crossings and patterns of small vessels can also serve as diagnostic indicators. An accurate delineation of the boundaries of blood vessels makes precise measurements of these features possible. These measurements may then be applied to a variety of tasks, including diagnosis, treatment evaluation, and clinical study.


## Dataset description

The authors present an automated approach for identifying and delineating blood vessels within ocular fundus images. This tool offers the potential to facilitate broader screenings for vessel abnormalities among populations by eyecare specialists. Additionally, it enables more precise measurements, which are crucial for treatment evaluation and clinical research. Moreover, utilizing such a tool ensures a more systematic and reproducible approach to observations. Unlike previous methods that focused mainly on local attributes, this method considers various characteristics of vessels such as color, shape, gradient, and contrast with the background.

<img src="https://github.com/dataset-ninja/stare/assets/120389559/a1b4b6c2-4ffa-4344-80b7-fcfc6bd999fa" alt="image" width="500">

<span style="font-size: smaller; font-style: italic;">In a healthy retina, the optic nerve has a readily identifiable size, shape, color, and location relative to the blood vessels.</span>

The optic nerve appears toward the of this image as a circular area, roughly one-sixth the width of the image in diameter, brighter than the surrounding area, as the convergent area of the blood vessel network. In an image of a healthy retina, all these properties (shape, color, size, convergence) help contribute to
the identification of the nerve. However, these features show a large variance that makes simple detection methods brittle, particularly in the presence of retinal disease.

<img src="https://github.com/dataset-ninja/stare/assets/120389559/fbbff8da-9e19-484a-be52-75c09825876d" alt="image" width="500">

<span style="font-size: smaller; font-style: italic;">Retina containing lesions of the same brightness as the nerve.</span>

This image of the retina containing drusen. The brightness of these lesions overlaps the brightness of the nerve, so that using brightness as a lone feature for detection is difficult.

<img src="https://github.com/dataset-ninja/stare/assets/120389559/a7e0dda6-b072-4323-bced-82a3f8e65cb6d" alt="image" width="500">

<span style="font-size: smaller; font-style: italic;">Swollen nerve, showing a distorted size and shape.</span>

<img src="https://github.com/dataset-ninja/stare/assets/120389559/6f86b87d-c360-40ae-9901-3e3b4d6d9845" alt="image" width="500">

<span style="font-size: smaller; font-style: italic;">Bright circular lesion that looks similar to an optic nerve.</span>

<img src="https://github.com/dataset-ninja/stare/assets/120389559/5f5e6cce-6c26-4577-b9a2-2e8976f67f84" alt="image" width="500">

<span style="font-size: smaller; font-style: italic;">Nerve that is completely obscured by hemorrhaging.</span>

These cases underscore the challenge in detecting the optic nerve and emphasize the necessity for a robust method capable of functioning effectively in the presence of various retinal diseases. Since the optic nerve's most consistent feature is its role as the convergence point of the blood vessel network, the authors have developed a method for optic nerve detection based on identifying this convergence. When a unique and strongly identifiable convergence isn't present, brightness serves as a secondary feature for optic nerve detection.

The authors employ multiple vessel segmentations of the same image to enhance the detection of convergent points. The concept is that the convergence should be discernible across vessel segmentations at different scales. To locate the convergence of the vessel network, they introduce a novel algorithm named "fuzzy convergence." This algorithm operates as a voting-type method within the spatial domain of the image. The input consists of a binary segmentation of the blood vessels, with each vessel being represented by a fuzzy segment contributing to a cumulative voting image. The algorithm outputs a convergence image, which is then thresholded to identify the most prominent point(s) of convergence.

<img src="https://github.com/dataset-ninja/stare/assets/120389559/417a23a1-efdf-4242-938f-9f0d7a79b4dc" alt="image" width="500">

<span style="font-size: smaller; font-style: italic;">Binary segmentation of blood vessels. (a) Sparser scale. (b) Denser scale.</span>

The authors rely primarily on a pioneering algorithm dubbed "fuzzy convergence" for optic nerve detection. This innovative approach pinpoints the optic nerve as the central hub of the blood vessel network. When a distinct convergence point is lacking, the authors' method identifies the optic nerve as the brightest area in the image following illumination equalization.

