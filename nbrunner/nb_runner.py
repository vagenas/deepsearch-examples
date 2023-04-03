import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

import yaml
from pathlib import Path

import os

import uuid

# constants
RUNNER_CONFIG = Path(__file__).parent / "config.yaml"
OUTPUT_DIR = Path(__file__).parent / "out"
PATH_YAML_KEY = "path"
DS_CFG_YAML_KEY = "ds_config"
DS_CFG_ENV_KEY = "DS_CONFIG_FILE"  # the one used in the notebooks


def execute_notebook(run_id, notebook_path, ds_auth_path, output_dir_path):

    os.environ[DS_CFG_ENV_KEY] = str(ds_auth_path)

    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")

    output_filename = output_dir_path / f"{Path(notebook_path.name).stem}_{run_id}.ipynb"
    try:
        out = ep.preprocess(nb, {'metadata': {'path': notebook_path.parent}})
    except CellExecutionError:
        print(f"=> Error during {run_id}; check {output_filename} for traceback")
        out = None
    finally:
        with open(output_filename, mode='w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        del os.environ[DS_CFG_ENV_KEY]
    return out


def run():
    with open(RUNNER_CONFIG, "r") as f:
        configs = yaml.safe_load(f)

    output_dir_path = Path(OUTPUT_DIR)
    output_dir_path.mkdir(parents=True, exist_ok=True)
    n_success = 0
    n_total = len(configs)

    for cfg in configs:
        run_id = uuid.uuid4().hex
        print(f"{run_id=}, {cfg=}")
        res = execute_notebook(
            run_id=run_id,
            notebook_path=Path(cfg[PATH_YAML_KEY]).resolve(),
            ds_auth_path=Path(cfg[DS_CFG_YAML_KEY]).resolve(),
            output_dir_path=output_dir_path,
        )
        if res is not None:
            n_success += 1

    print(80*"-")
    print(f"Successful runs: {n_success}/{n_total}")
    print(80*"-")


if __name__ == "__main__":
    run()
