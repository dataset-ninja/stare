import gzip
import os
import shutil
from urllib.parse import unquote, urlparse

import cv2
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    mkdir,
    remove_dir,
    silent_remove,
)
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    temp_path = "/home/alex/DATASETS/TODO/STARE/temp"
    images_path = "/home/alex/DATASETS/TODO/STARE/all-images"
    ah_masks_path = "/home/alex/DATASETS/TODO/STARE/labels-ah"
    vk_masks_path = "/home/alex/DATASETS/TODO/STARE/labels-vk"
    results_4_masks_path = "/home/alex/DATASETS/TODO/STARE/results-4"
    diagnoses_path = "/home/alex/DATASETS/TODO/STARE/diagnoses.txt"
    batch_size = 30
    ds_name = "ds"
    arch_path_to_ext = {
        ah_masks_path: ".ah.ppm.gz",
        vk_masks_path: ".vk.ppm.gz",
        results_4_masks_path: "-vessels4.ppm.gz",
    }

    images_ext = ".png"

    mkdir(temp_path)

    def create_ann(image_path):
        labels = []
        tags = []

        img_height = 605  # mask_np.shape[0]
        img_wight = 700  # mask_np.shape[1]

        diagnos_value = im_name_to_diagnos.get(get_file_name(image_path))
        if diagnos_value is not None:
            if len(diagnos_value) > 0:
                diagnos = sly.Tag(diagnoses_meta, value=diagnos_value)
                tags.append(diagnos)

        for arch_path, arch_ext in arch_path_to_ext.items():
            curr_arch_path = os.path.join(arch_path, get_file_name(image_path) + arch_ext)
            if file_exists(curr_arch_path):
                labeller_meta = arch_path_to_meta[arch_path]
                labeller = sly.Tag(labeller_meta)
                curr_image_path = curr_arch_path[: -1 * len(arch_ext)] + images_ext
                with gzip.open(curr_arch_path, "rb") as f_in:
                    with open(curr_image_path, "wb") as f_out:
                        shutil.copyfileobj(f_in, f_out)
                        mask_np = cv2.imread(curr_image_path)[:, :, 0]
                        obj_mask = mask_np == 255
                        curr_bitmap = sly.Bitmap(obj_mask)
                        curr_label = sly.Label(curr_bitmap, obj_class, tags=[labeller])
                        labels.append(curr_label)
                silent_remove(curr_image_path)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    obj_class = sly.ObjClass("vessels", sly.Bitmap)

    ah_meta = sly.TagMeta("adam hoover", sly.TagValueType.NONE)
    vk_meta = sly.TagMeta("valentina kouznetsova", sly.TagValueType.NONE)
    results_meta = sly.TagMeta("filter probing algorithm", sly.TagValueType.NONE)

    diagnoses_meta = sly.TagMeta("diagnos", sly.TagValueType.ANY_STRING)

    arch_path_to_meta = {
        ah_masks_path: ah_meta,
        vk_masks_path: vk_meta,
        results_4_masks_path: results_meta,
    }

    im_name_to_diagnos = {}

    with open(diagnoses_path) as f:
        content = f.read().split("\n")
        for row in content:
            data = row.split("\t")
            im_name_to_diagnos[data[0]] = data[-1]

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class], tag_metas=[ah_meta, vk_meta, results_meta, diagnoses_meta]
    )
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_names = os.listdir(images_path)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        new_im_names_batch = []
        images_pathes_batch = []
        for im_name in img_names_batch:
            im_path = os.path.join(images_path, im_name)
            new_im_name = get_file_name(im_name) + images_ext
            new_im_names_batch.append(new_im_name)
            new_im_path = os.path.join(temp_path, new_im_name)
            images_pathes_batch.append(new_im_path)

            curr_image_np = cv2.imread(im_path)
            cv2.imwrite(new_im_path, curr_image_np)

        img_infos = api.image.upload_paths(dataset.id, new_im_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(img_names_batch))

    remove_dir(temp_path)

    return project
