from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "STARE"
PROJECT_NAME_FULL: str = "STARE: Structured Analysis of the Retina Dataset"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.PubliclyAvailable(
    source_url="https://www.uhu.es/retinopathy/General/030801IEEETransMedImag.pdf"
)
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Research.Medical()]
CATEGORY: Category = Category.Medical()

CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2000

HOMEPAGE_URL: str = "https://cecas.clemson.edu/~ahoover/stare/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 13323368
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/stare"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Images": "https://cecas.clemson.edu/~ahoover/stare/images/all-images.zip",
    "Adam Hoover labelled data": "https://cecas.clemson.edu/~ahoover/stare/probing/labels-ah.tar",
    "Valentina Kouznetsova labelled data": "https://cecas.clemson.edu/~ahoover/stare/probing/labels-vk.tar",
    "Spatial filter probing algorithm labelled data": "https://cecas.clemson.edu/~ahoover/stare/probing/results-4.tar",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = {
    "Research Paper 1": "https://ieeexplore.ieee.org/abstract/document/845178",
    "Research Paper 2": "https://ieeexplore.ieee.org/abstract/document/1216219",
}
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {
    "Academic Torrents": "https://academictorrents.com/details/e4554cd63400dc13b74477efe98032c10757c269",
}

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = ["A. Hoover", "V. Kouznetsova", "M. Goldbaum"]
AUTHORS_CONTACTS: Optional[List[str]] = ["mgoldbaum@ucsd.edu"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "University of California, USA"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://ucsd.edu/"

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "labelers": [
        "filter probing algorithm",
        "adam hoover",
        "valentina kouznetsova",
    ],
    "__POSTTEXT__": "Additionally, every image contains information about patient ***diagnos***. Explore it in supervisely labeling tool",
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
