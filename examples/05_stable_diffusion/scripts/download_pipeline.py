#  Copyright (c) Meta Platforms, Inc. and affiliates.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import click
import torch
from diffusers import StableDiffusionPipeline


@click.command()
@click.option(
    "--model-name",
    default="runwayml/stable-diffusion-v1-5",
    help="Pretrained Model name",
)
@click.option("--token", default="", help="access token")
@click.option(
    "--save-directory",
    default="./tmp/diffusers-pipeline/runwayml/stable-diffusion-v1-5",
    help="pipeline files local directory",
)
def download_pipeline_files(model_name, token, save_directory) -> None:
    StableDiffusionPipeline.from_pretrained(
        model_name,
        revision="fp16",
        torch_dtype=torch.float16,
        # use provided token or the one generated with `huggingface-cli login``
        use_auth_token=token if token != "" else False,
    ).save_pretrained(save_directory)


if __name__ == "__main__":
    download_pipeline_files()