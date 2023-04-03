# Notebook runner

Automate the execution of notebooks against different deployments using a simple
[config.yaml](config.yaml).

The configured notebooks should be able to read the DS authentication config file from env
var `DS_CONFIG_FILE` when that is set.

## Usage
```shell
python nb_runner.py
```

An execution can look like the following:
```console
$ python nb_runner.py
run_id='d753cda279d541078178788ec50bd9d9', cfg={'path': './sample_input/example_1.ipynb', 'ds_config': '../ds-auth.ext-v2.json'}
run_id='89995914d9c34e80b990150754d822d2', cfg={'path': './sample_input/example_2.ipynb', 'ds_config': '../ds-auth.ext-v2.json'}
=> Error during 89995914d9c34e80b990150754d822d2; check out/example_2_89995914d9c34e80b990150754d822d2.ipynb for traceback
run_id='94639a84bb7042da943b85816b3b8176', cfg={'path': './sample_input/example_1.ipynb', 'ds_config': '../ds-auth.foc.json'}
--------------------------------------------------------------------------------
Successful runs: 2/3
--------------------------------------------------------------------------------
$
```
